from flask import Flask, render_template, request, jsonify, session
import os
import uuid
import traceback
from chatbot.gemini_api import get_gemini_response
from chatbot.memory import ConversationMemory

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize conversation memory
memory_manager = ConversationMemory()

@app.route('/')
def index():
    # Set up a unique session ID if one doesn't exist
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
        memory_manager.initialize_user(session['session_id'])
    
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_message = request.json['message']
        session_id = session.get('session_id')
        
        # Add user message to memory
        memory_manager.add_message(session_id, "user", user_message)
        
        # Get conversation history
        conversation_history = memory_manager.get_conversation_history(session_id)
        user_profile = memory_manager.get_user_profile(session_id)
        
        # Get response from Gemini API
        response = get_gemini_response(user_message, conversation_history, user_profile)
        
        # Add bot response to memory
        memory_manager.add_message(session_id, "assistant", response)
        
        # Update user profile based on the conversation
        memory_manager.update_user_profile(session_id, user_message, response)
        
        return jsonify({"message": response})
    except Exception as e:
        print(f"Error in send_message: {e}")
        traceback.print_exc()
        return jsonify({"message": "I'm sorry, something went wrong. Please try again later."}), 500

@app.route('/reset_conversation', methods=['POST'])
def reset_conversation():
    session_id = session.get('session_id')
    memory_manager.clear_conversation(session_id)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
