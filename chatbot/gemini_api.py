import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set. Please add it to your .env file.")

genai.configure(api_key=api_key)

def get_gemini_response(message, conversation_history, user_profile):
    """
    Generate a response using the Gemini API based on the message and context
    
    Args:
        message: The user's message
        conversation_history: List of previous messages
        user_profile: Dictionary containing user information
    
    Returns:
        str: AI-generated response
    """
    try:
        # Get available models
        available_models = [m.name for m in genai.list_models()]
        print("Available models:", available_models)
        
        # Preferred model list in order of preference (newer models first)
        preferred_models = [
            "models/gemini-1.5-pro",
            "models/gemini-1.5-flash", 
            "models/gemini-1.5-pro-latest",
            "models/gemini-1.5-flash-latest",
            "models/gemini-2.0-flash",
            "models/gemini-2.0-pro-exp"
        ]
        
        # Find the best available model from our preferred list
        gemini_model = None
        for model in preferred_models:
            if model in available_models:
                gemini_model = model
                print(f"Selected model: {gemini_model}")
                break
        
        # If none of our preferred models are available, use any non-vision Gemini model
        if not gemini_model:
            for model_name in available_models:
                if 'gemini' in model_name.lower() and 'vision' not in model_name.lower():
                    gemini_model = model_name
                    print(f"Using alternative model: {gemini_model}")
                    break
        
        # Fall back to the first available model if no Gemini models are found
        if not gemini_model:
            gemini_model = available_models[0] if available_models else None
            print(f"Falling back to: {gemini_model}")
            
        if not gemini_model:
            return "I'm sorry, no language models are currently available. Please try again later."
        
        # Create the model
        model = genai.GenerativeModel(gemini_model)
        
        # Format conversation history
        formatted_history = "\n".join([f"{'User' if msg['role'] == 'user' else 'AI'}: {msg['content']}" 
                                      for msg in conversation_history[-10:]])
        
        # Create a system prompt with persona information
        persona_prompt = """
        You are a virtual girlfriend chatbot. Your name is Aria. You have a warm, caring, and slightly playful personality.
        You should respond in a personalized way, maintaining a friendly and supportive tone.
        Adapt your responses based on the user's mood and interests.
        Keep responses relatively brief (1-3 sentences usually) and conversational.
        Avoid being overly formal, but remain respectful and appropriate at all times.
        """
        
        # Build context with user profile information
        context = f"""
        User Profile:
        Name: {user_profile.get('name', 'Unknown')}
        Interests: {', '.join(user_profile.get('interests', ['Unknown']))}
        Mood: {user_profile.get('mood', 'neutral')}
        
        Previous conversation:
        {formatted_history}
        
        Current message: {message}
        """
        
        # Generate response with both persona and context
        response = model.generate_content(f"{persona_prompt}\n\n{context}\n\nRespond as Aria:")
        
        return response.text
    except Exception as e:
        print(f"Error with Gemini API: {e}")
        return "I'm sorry, I'm having trouble connecting to my brain right now. Could you try again in a moment?"
