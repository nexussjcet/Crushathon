from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_session import Session
import os
import google.generativeai as genai
import json

# Configure Gemini AI
genai.configure(api_key='AIzaSyBfLgClw1r2Qd3Ps1GhOThHn_P0eOeo-tw')

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = True  # Changed to True for persistent sessions
app.config["PERMANENT_SESSION_LIFETIME"] = 60 * 60 * 24 * 7  # 7 days
app.config["SECRET_KEY"] = os.urandom(24)
Session(app)

# Ensure directories exist
UPLOAD_FOLDER = 'static/uploads'
DATA_FOLDER = 'user_data'
for folder in [UPLOAD_FOLDER, DATA_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

DEFAULT_BOT = {
    "name": "MyCrush",
    "dp": "static/default_avatar.png",
    "traits": "Caring, Funny",
    "gender": "Neutral"
}

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-pro')

# Max number of messages to keep in memory context
MAX_CONTEXT_MESSAGES = 15

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/customize", methods=["GET", "POST"])
def customize():
    if request.method == "POST":
        # Get unique user ID (create one if not exists)
        user_id = session.get("user_id")
        if not user_id:
            import uuid
            user_id = str(uuid.uuid4())
            session["user_id"] = user_id
        
        session["bot_name"] = request.form["bot_name"]
        session["bot_traits"] = request.form["bot_traits"]
        session["bot_gender"] = request.form["bot_gender"]
       
        # Handle DP upload
        file = request.files.get("bot_dp")
        if file and file.filename:
            # Secure the filename and save
            filename = f"{user_id}_{os.path.basename(file.filename)}"
            dp_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(dp_path)
            session["bot_dp"] = dp_path
        else:
            session["bot_dp"] = DEFAULT_BOT["dp"]
       
        # Initialize or maintain chat history
        if "chat_history" not in session:
            session["chat_history"] = []
        
        # Save bot configuration to disk for persistence
        save_user_data(user_id)
       
        return redirect(url_for("chat"))
   
    return render_template("customize.html")

@app.route('/chat')
def chat():
    # Load user data if exists but not in session
    user_id = session.get("user_id")
    if user_id and "bot_name" not in session:
        load_user_data(user_id)
    
    # Check if bot is configured, redirect to customize if not
    if "bot_name" not in session:
        return redirect(url_for("customize"))
       
    bot_name = session.get("bot_name", DEFAULT_BOT["name"])
    bot_dp = session.get("bot_dp", DEFAULT_BOT["dp"])
    bot_traits = session.get("bot_traits", DEFAULT_BOT["traits"])
    chat_history = session.get("chat_history", [])
   
    return render_template("chat.html", bot_name=bot_name, bot_dp=bot_dp,
                          bot_traits=bot_traits, chat_history=chat_history)

@app.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.json.get("message", "")
    if not user_message.strip():
        return jsonify({"bot_response": "Say something interesting! 😆"})
   
    chat_history = session.get("chat_history", [])
   
    # Prepare context for AI response
    bot_name = session.get("bot_name", DEFAULT_BOT["name"])
    bot_traits = session.get("bot_traits", DEFAULT_BOT["traits"])
    bot_gender = session.get("bot_gender", DEFAULT_BOT["gender"])
   
    # Create context from previous messages
    conversation_context = ""
    if chat_history:
        # Get last few messages for context
        context_messages = chat_history[-MAX_CONTEXT_MESSAGES:]
        for msg in context_messages:
            conversation_context += f"You: {msg['bot']}\nUser: {msg['user']}\n"
    
    # AI Response with context
    try:
        prompt = f"""You are roleplaying as {bot_name}, who has these traits: {bot_traits}.
        Your gender is {bot_gender}. Respond to this message as if you were someone's crush with those traits.
        
        Previous conversation:
        {conversation_context}
        
        Remember important details the user has shared about themselves and reference them naturally in your responses.
        Keep responses conversational, flirty but appropriate, and under 3 sentences.
        
        User's message: {user_message}"""
       
        response = model.generate_content(prompt)
        bot_response = response.text.strip()
    except Exception as e:
        bot_response = f"Oops! I'm having a brain freeze. Try again! 🥶 (Error: {str(e)})"
   
    # Update chat history
    chat_history.append({"user": user_message, "bot": bot_response})
    
    # Keep only the most recent messages in session
    if len(chat_history) > MAX_CONTEXT_MESSAGES * 2:
        chat_history = chat_history[-(MAX_CONTEXT_MESSAGES * 2):]
        
    session["chat_history"] = chat_history
    
    # Save updated chat history to disk
    user_id = session.get("user_id")
    if user_id:
        save_user_data(user_id)
   
    return jsonify({"bot_response": bot_response})

@app.route("/clear_chat")
def clear_chat():
    session.pop("chat_history", None)
    
    # Also clear saved chat history on disk
    user_id = session.get("user_id")
    if user_id:
        user_data_path = os.path.join(DATA_FOLDER, f"{user_id}.json")
        if os.path.exists(user_data_path):
            data = load_json(user_data_path)
            data["chat_history"] = []
            save_json(user_data_path, data)
    
    return redirect(url_for("customize"))

# Helper functions for data persistence
def save_user_data(user_id):
    """Save user data and chat history to disk"""
    data = {
        "bot_name": session.get("bot_name"),
        "bot_traits": session.get("bot_traits"),
        "bot_gender": session.get("bot_gender"),
        "bot_dp": session.get("bot_dp"),
        "chat_history": session.get("chat_history", [])
    }
    save_json(os.path.join(DATA_FOLDER, f"{user_id}.json"), data)

def load_user_data(user_id):
    """Load user data and chat history from disk"""
    user_data_path = os.path.join(DATA_FOLDER, f"{user_id}.json")
    if os.path.exists(user_data_path):
        data = load_json(user_data_path)
        for key, value in data.items():
            session[key] = value
        return True
    return False

def save_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    app.run(debug=True)