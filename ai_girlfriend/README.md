# Crushathon - AI Virtual Girlfriend

An AI-powered virtual girlfriend chatbot built with Flask and Google's Gemini API. The application provides engaging, context-aware conversations with personalized responses.


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

- Christin Jose Biju
- I am a student pursuing computer science and design at viswajyothi college of engineering and technologies, vazhakulam

- email: christinjb100@gmail.com

--- 


