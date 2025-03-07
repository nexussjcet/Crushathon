import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from chatbot import AIChatbotGirlfriend
import traceback
from datetime import datetime
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_latest_generated_image():
    """Get the most recently generated image from the static/generated_images folder"""
    image_dir = 'static/generated_images'
    if not os.path.exists(image_dir):
        return None
    
    
    image_files = [
        os.path.join(image_dir, f) for f in os.listdir(image_dir)
        if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')
    ]
    
    if not image_files:
        return None
    
    
    latest_image = max(image_files, key=os.path.getctime)
    
    
    return latest_image.replace('static/', '')

def generate_companion_image(description):
    """Generate companion image using pollinations.ai API"""
    try:
        
        os.makedirs('static/generated_images', exist_ok=True)
        
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f'companion_image_{timestamp}.jpg'
        image_path = os.path.join('static/generated_images', image_filename)
        
        
        prompt = f"realistic portrait of a person: {description}"
        
        
        encoded_prompt = requests.utils.quote(prompt)
        
        
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&model=flux"
        response = requests.get(url)
        
        # Save the image
        with open(image_path, 'wb') as file:
            file.write(response.content)
            
        return f'generated_images/{image_filename}'
    except Exception as e:
        print(f"Image Generation Error: {e}")
        traceback.print_exc()
        return None

@app.route('/')
def home():
   
    if 'api_key' in session and 'girlfriend_name' in session:
        return redirect(url_for('chat_interface'))
    return render_template('index.html')

@app.route('/chat-interface')
def chat_interface():
    
    if 'api_key' not in session or 'girlfriend_name' not in session:
        return redirect(url_for('setup_api'))
    
    
    companion_image = session.get('companion_image', '')
    
    
    if companion_image and not companion_image.startswith('generated_images/'):
        companion_image = f'generated_images/{os.path.basename(companion_image)}'
    
    return render_template('chat.html',
                          girlfriend_name=session['girlfriend_name'],
                          companion_image=companion_image)

@app.route('/setup/girlfriend', methods=['GET', 'POST'])
def setup_girlfriend():
    if 'api_key' not in session:
        return redirect(url_for('setup_api'))
    
    if request.method == 'POST':
        girlfriend_name = request.form.get('girlfriend_name')
        girlfriend_description = request.form.get('girlfriend_description')
        
        if not girlfriend_name or not girlfriend_description:
            return render_template('setup_girlfriend.html', error="All fields are required!")
        
        
        companion_image = generate_companion_image(girlfriend_description)
        
       
        session['girlfriend_name'] = girlfriend_name
        session['girlfriend_description'] = girlfriend_description
        session['companion_image'] = companion_image or ''
        
        return redirect(url_for('setup_user'))
    
    return render_template('setup_girlfriend.html')

@app.route('/setup/api', methods=['GET', 'POST'])
def setup_api():
    if request.method == 'POST':
        api_key = request.form.get('api_key')
        
        if not api_key:
            return render_template('setup_api.html', error="API Key is required!")
        
        
        session['api_key'] = api_key
        return redirect(url_for('setup_girlfriend'))
    
    return render_template('setup_api.html')

@app.route('/setup/user', methods=['GET', 'POST'])
def setup_user():
    if 'api_key' not in session or 'girlfriend_name' not in session:
        return redirect(url_for('setup_api'))
    
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        user_description = request.form.get('user_description')
        
        if not user_name or not user_description:
            return render_template('setup_user.html', error="All fields are required!")
        
        
        session['user_name'] = user_name
        session['user_description'] = user_description
        
       
        chatbot = AIChatbotGirlfriend(session['api_key'])
        chatbot.girlfriend_name = session['girlfriend_name']
        chatbot.girlfriend_description = session['girlfriend_description']
        chatbot.user_name = session['user_name']
        chatbot.user_description = session['user_description']
        
        # Save to database
        chatbot.save_girlfriend_detail('name', chatbot.girlfriend_name)
        chatbot.save_girlfriend_detail('description', chatbot.girlfriend_description)
        chatbot.save_user_detail('name', chatbot.user_name)
        chatbot.save_user_detail('description', chatbot.user_description)
        
        return redirect(url_for('chat_interface'))
    
    
    companion_image = session.get('companion_image', '')
    
    return render_template('setup_user.html', 
                          girlfriend_name=session['girlfriend_name'],
                          companion_image=companion_image)


@app.route('/index')
def index():
    return redirect(url_for('chat_interface'))

@app.route('/chat', methods=['POST'])
def chat():
    
    if 'api_key' not in session:
        return jsonify({'response': 'Please complete setup first.'})
    
    
    chatbot = AIChatbotGirlfriend(session['api_key'])
    chatbot.girlfriend_name = session['girlfriend_name']
    chatbot.girlfriend_description = session['girlfriend_description']
    chatbot.user_name = session['user_name']
    chatbot.user_description = session['user_description']
    
    user_input = request.json.get('message', '')
    
    if user_input.lower() == 'reset':
        return jsonify({'response': 'Conversation reset!'})
    
    try:
        response = chatbot.generate_response(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

@app.route('/reset', methods=['GET'])
def reset():
    
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)