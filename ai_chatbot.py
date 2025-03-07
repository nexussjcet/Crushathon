import openai
import pyttsx3
import speech_recognition as sr

# ✅ Set up OpenAI client with your API key
client = openai.OpenAI(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")  # 🔴 Replace this

def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Captures voice input and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Speech recognition service error."

def chat_with_ai(prompt, personality="romantic"):
    """Sends user input to OpenAI and returns AI-generated response."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": f"You are a {personality} AI partner. Be engaging and expressive."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

def main():
    print("AI Partner Activated! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye, love!")
            break
        response = chat_with_ai(user_input)
        print(f"AI: {response}")
        speak(response)

if __name__ == "__main__":
    main()
