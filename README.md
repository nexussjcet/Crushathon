# CrushAI 💕

CrushAI is a **GenAI-based Virtual Crush Chatbot** that lets users experience fun, engaging, and emotional conversations with an AI partner. It can adapt personalities, handle mood swings, and provide human-like chat experiences.

## Features ✨

- Chat with your AI Crush 💬
- Personality Selection: Sweet, Sensitive, Moody, Funny
- Mood Swings 🌈
- Gemini AI Integration
- Customizable Emotional Responses
- Real-time Conversations
- Stores Last 10 Messages for Continuity 🔄
- Secure and Private Chats 🔒

## Tech Stack 🔥

- **Frontend:** Flutter (Material UI - Web Only)
- **Backend:** Python Flask API
- **AI Model:** Gemini AI

## Folder Structure 📁
```
Ai-ChatBot/
│
├─ app/                   # Flutter App Folder
│   ├─ main.dart          # Main Flutter App Code
│   └─ ...
│
├─ requirements.txt       # Backend Dependencies
└─ README.md             # Documentation
```

## Installation ⚙️

1. Clone the repository:
   ```bash
   git clone https://github.com/johanjoseph29/Ai-ChatBot.git
   cd Ai-ChatBot
   ```

2. Install Dependencies:
   ```bash
   cd app
   flutter pub get
   ```
   **Flutter Dependencies:**
   ```yaml
   http: ^0.13.6
   google_generative_ai: ^0.3.0
   provider: ^6.0.5
   ```

3. Run the app (Web Only):
   ```bash
   flutter run -d chrome
   ```

### Backend Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
**requirements.txt:**
```plaintext
Flask==3.0.0
Flask-Cors==4.0.0
requests==2.31.0
google-generativeai==0.4.1
textblob==0.18.0
```

2. Run Flask API:
   ```bash
   python app/api.py
   ```
   API URL: `http://127.0.0.1:5000/chat`

## How to Use 🔥

1. Install the app from the provided link.
2. Open the app and sign up with your email ID.
3. Choose your AI Crush personality (Sweet, Sensitive, Moody, Funny).
4. Start chatting and experience human-like conversations.
5. Enjoy mood swings, emotional talks, and funny replies.
6. The app automatically stores the **last 10 messages** to maintain chat continuity.
7. Use the settings to customize personality preferences.

## App Preview 📸

<img src="https://github.com/johanjoseph29/AI-ChatBot/blob/main/assets/gifmaker_me%20(2).gif" width="250" height="350"/>

## Developer Profile 👤

**Full Name:** Johan Joseph\
**Education/Profession:** CSEA @ AJCE (2024-2028)\
**Contact Details:** jithu197807@gmail.com

---

