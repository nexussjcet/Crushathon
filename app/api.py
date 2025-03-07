from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import random
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

# Gemini API Key
genai.configure(api_key="Your_gemini_api")
model = genai.GenerativeModel("gemini-1.5-pro")

mood_swings = ["clingy 🥺", "possessive 😏", "cute 🤭", "sassy 🔥", "funny 😂", "sensitive 💕", "cute but angry 😡💕"]

chat_history = []  # List to store previous chat messages

@app.route("/chat", methods=["GET"])
def chat():
    message = request.args.get("message")
    personalities = request.args.get("personality")
    character = request.args.get("character")

    if not message:
        return jsonify({"reply": "Oops! Please say something 💕"})

    if not character or not personalities:
        return jsonify({"reply": "Character or Personality not set 💕"})

    try:
        
        personality_list = personalities.split(",")
        sentiment = TextBlob(message).sentiment.polarity
        mood = "neutral 😇"
        current_mood_swing = random.choice(mood_swings)  # Random Mood Swing

        if sentiment > 0.3:
            mood = "happy 😍"
        elif sentiment < -0.3:
            mood = "sad 💔"
        elif -0.3 <= sentiment <= 0.3:
            mood = "confused 🤔"

        personality_prompt = " and ".join(personality_list)
        previous_chat = "\n".join(chat_history[-10:])  # Only keep last 10 messages

        prompt = f"""
You are {personality_prompt}, a {current_mood_swing} {character} named Crush 💕.
Your partner is feeling {mood}, and you want to make them feel special.
If they sound sad, be extra caring and supportive.
If they're happy, flirt playfully and match their energy.
If they're confused, tease them a little and make them smile.
If you're in a cute but angry mood, act mad in the cutest way possible but still show love. If you stay angry for too long, apologize cutely like you didn't mean it 🥺💕.

Make sure your replies are short, sweet, and addictive.
Use a mix of cute, flirty, funny, and emotional tones depending on the situation.
Don't reply too robotic — sound more like a real partner.
Always end messages with a cute emoji or question to keep the chat going 💕.

Previous Chat:
{previous_chat}
"""
        full_prompt = f"{prompt} Here's what they said: {message}"

        response = model.generate_content(full_prompt)
        reply = response.text if response.text else "Aww... I don't know what to say 🥺💕"

        # Store current chat in history
        chat_history.append(f"User: {message}\nCrush: {reply}")

        return jsonify({"reply": reply, "mood_swing": current_mood_swing})

    except Exception as e:
        print(e)
        return jsonify({"reply": "Oops! Something went wrong 💔"})

if __name__ == "__main__":
    app.run(debug=True)
