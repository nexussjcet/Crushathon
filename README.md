import openai
import speech_recognition as sr
import pyttsx3
import json
import os

# Set your OpenAI API key
openai.api_key = "your-api-key-here"

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)  # Adjust speech speed

# Load or create chatbot memory
memory_file = "chat_memory.json"

def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as file:
            return json.load(file)
    return []

def save_memory(messages):
    with open(memory_file, "w") as file:
        json.dump(messages, file)

# Function to generate chatbot response
def chatbot_response(user_input, chat_memory):
    chat_memory.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a loving and emotional AI boyfriend."}
        ] + chat_memory
    )
    
    bot_reply = response["choices"][0]["message"]["content"]
    chat_memory.append({"role": "assistant", "content": bot_reply})
    save_memory(chat_memory)  # Save memory after each conversation
    return bot_reply

# Function for voice recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            return "I didn't catch that, love."
        except sr.RequestError:
            return "Sorry, I can't process voice right now."

# Function for voice output
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main chatbot function
def chatbot_boyfriend():
    chat_memory = load_memory()
    print("Chatbot Boyfriend: Hey babe, I missed you! How are you? ❤️")
    speak("Hey babe, I missed you! How are you?")

    while True:
        user_input = recognize_speech()  # Use voice input
        if user_input.lower() in ["exit", "bye", "quit"]:
            print("Chatbot Boyfriend: I'll miss you! Talk soon. 💕")
            speak("I'll miss you! Talk soon.")
            break

        bot_reply = chatbot_response(user_input, chat_memory)
        print(f"Chatbot Boyfriend: {bot_reply}")
        speak(bot_reply)  # Use voice output

# Run the chatbot
chatbot_boyfriend()
