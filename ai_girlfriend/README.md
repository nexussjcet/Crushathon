# Crushathon - AI Virtual Girlfriend

An AI-powered virtual girlfriend chatbot built with Flask and Google's Gemini API. The application provides engaging, context-aware conversations with personalized responses.

## Features

- Personalized conversations based on user details
- Memory system to remember previous interactions
- Emotion recognition and appropriate responses
- User-friendly web interface
- Session management for multiple users

## Installation

1. Clone this repository
2. Install dependencies:

![Slice 6](https://github.com/user-attachments/assets/89e3f3e2-bcfa-4483-bfea-e3e2f5439c00)

Welcome to **Crushathon**, an exhilarating competition at **Asthra 2025**, where innovation meets creativity! This unique challenge invites participants to build an interactive AI boyfriend or girlfriend, capable of engaging conversations and unique features.

> Deadline for Submission: March 7, 2025

## How to Participate
### Step 1
- [Fork this repository](https://github.com/nexussjcet/Crushathon/fork) to your GitHub account.

### Step 2
- Develop an AI chatbot that can simulate conversations.
- Enhance it with creative and innovative features of your choice.
- Showcase your chatbot’s functionality and intelligence.
- Describe the working of your AI partner in _How to use_ placeholder in `README.md`.

### Step 3
- Complete your profile in the _Developer profile_ placeholder in `README.md` to get certificates.
- Once you are done, create a pull request.


### How to Use

### Setup and Installation

1. Ensure you have Python 3.8 or newer installed on your system.

2. Create and activate a virtual environment:
   
   **On Windows:**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   source venv/bin/activate
   ```
   
   You'll know the virtual environment is activated when you see `(venv)` at the beginning of your terminal prompt.

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Get a Google Gemini API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create or sign in to your Google account
   - Create a new API key
   - Copy your API key

5. Configure your API key:
   - Open the `.env` file
   - Replace the placeholder value with your Gemini API key:
     ```
     GEMINI_API_KEY=your_key_here
     ```

### Running the Application

1. Start the application by running:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

3. Now you can start chatting with Aria, your AI companion!

### Interacting with Aria

- Introduce yourself by telling Aria your name
- Share your interests and hobbies
- Discuss how you're feeling - Aria can adapt to your mood
- Ask questions about various topics
- Use the "Reset Conversation" button if you want to start fresh

### Troubleshooting

If you encounter errors when running the application:

1. **API Key Issues**: 
   - Make sure you have a valid Gemini API key in your `.env` file
   - Verify that you have access to the Gemini API (some regions may have restrictions)
   - Try regenerating a new API key if issues persist

2. **Model Not Found Error**:
   - The application will now automatically detect available models
   - Check the console output to see which model is being used
   - If no Gemini models are available, the application will fall back to another model or provide an error message

3. **Dependencies Issues**:
   - Make sure all dependencies are correctly installed:
   ```bash
   pip install -r requirements.txt
   ```
   - Try updating the google-generativeai package:
   ```bash
   pip install --upgrade google-generativeai
   ```

4. **Runtime Errors**:
   - Check the console for detailed error messages
   - Make sure your Python version is 3.8 or newer

### Developer Profile

- Enter your full name
- Write a brief paragraph about your current education/profession
- Add your projects and portfolio (optional)
- Add your profiles on HackerRank, Exercism, LinkedIn, Mulearn, etc (optional).
- Contact details: Email ID

--- 
> Note:
> This event has no prize pool. The best 3 projects will receive appreciation certificates, and all participants will receive a participation certificate.  
> If you have any doubts, feel free to contact [Pranav Sojan](https://wa.me/918113015528).

