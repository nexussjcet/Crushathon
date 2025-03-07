from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_session import Session
import os
import google.generativeai as genai

# Configure Gemini AI - You'll need to add your API key
genai.configure(api_key='AIzaSyBfLgClw1r2Qd3Ps1GhOThHn_P0eOeo-tw')

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SECRET_KEY"] = os.urandom(24)  # Added for security
Session(app)

# Ensure upload directory exists
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

DEFAULT_BOT = {
    "name": "MyCrush",
    "dp": "static/default_avatar.png",  # Default avatar
    "traits": "Caring, Funny",
    "gender": "Neutral"
}

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/customize", methods=["GET", "POST"])
def customize():
    if request.method == "POST":
        session["bot_name"] = request.form["bot_name"]
        session["bot_traits"] = request.form["bot_traits"]
        session["bot_gender"] = request.form["bot_gender"]
       
        # Handle DP upload
        file = request.files.get("bot_dp")
        if file and file.filename:
            # Secure the filename and save
            filename = f"{session['bot_name'].lower().replace(' ', '_')}_{os.path.basename(file.filename)}"
            dp_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(dp_path)
            session["bot_dp"] = dp_path
        else:
            session["bot_dp"] = DEFAULT_BOT["dp"]
        
        # Initialize empty chat history
        session["chat_history"] = []
        
        return redirect(url_for("chat"))
   
    return render_template("customize.html")

@app.route('/chat')
def chat():
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
    
    # AI Response
    try:
        prompt = f"""You are roleplaying as {bot_name}, who has these traits: {bot_traits}. 
        Your gender is {bot_gender}. Respond to this message as if you were someone's crush with those traits.
        Keep responses conversational, flirty but appropriate, and under 3 sentences. Message: {user_message}"""
        
        response = model.generate_content(prompt)
        bot_response = response.text.strip()
    except Exception as e:
        bot_response = f"Oops! I'm having a brain freeze. Try again! 🥶 (Error: {str(e)})"
    
    # Update chat history
    chat_history.append({"user": user_message, "bot": bot_response})
    session["chat_history"] = chat_history
    
    return jsonify({"bot_response": bot_response})

@app.route("/clear_chat")
def clear_chat():
    session.pop("chat_history", None)
    return redirect(url_for("customize"))

if __name__ == "__main__":
    app.run(debug=True)