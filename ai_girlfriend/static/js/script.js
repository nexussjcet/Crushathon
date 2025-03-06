document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const resetBtn = document.getElementById('reset-btn');
    const chatContainer = document.querySelector('.chat-container');

    // Create rose petals
    function createRosePetals() {
        const totalPetals = 15;
        const viewport = document.querySelector('.chat-container');
        
        // Clear existing petals
        document.querySelectorAll('.rose-petal').forEach(petal => petal.remove());
        
        for (let i = 0; i < totalPetals; i++) {
            setTimeout(() => {
                const petal = document.createElement('div');
                petal.classList.add('rose-petal');
                
                // Randomly select one of three petal designs
                const petalType = Math.floor(Math.random() * 3) + 1;
                petal.classList.add(`petal-${petalType}`);
                
                // Random size between 20px and 40px
                const size = 20 + Math.random() * 20;
                petal.style.width = `${size}px`;
                petal.style.height = `${size}px`;
                
                // Random horizontal position
                const startPosX = Math.random() * 100;
                petal.style.left = `${startPosX}%`;
                
                // Random horizontal shift during fall
                const translateX = -50 + Math.random() * 100;
                petal.style.setProperty('--tx', `${translateX}px`);
                
                // Random rotation during fall
                const rotation = 360 + Math.random() * 360;
                petal.style.setProperty('--rt', `${rotation}deg`);
                
                // Random sway parameters
                petal.style.setProperty('--sway-x', `${10 + Math.random() * 20}px`);
                petal.style.setProperty('--sway-r', `${15 + Math.random() * 15}deg`);
                
                // Set animation properties
                const fallDuration = 8 + Math.random() * 10;
                const swayDuration = 2 + Math.random() * 4;
                
                petal.style.animation = `
                    fallingRotating ${fallDuration}s linear forwards,
                    sway ${swayDuration}s ease-in-out infinite alternate
                `;
                
                viewport.appendChild(petal);
                
                // Remove petal after animation completes
                setTimeout(() => {
                    petal.remove();
                }, fallDuration * 1000);
                
            }, i * 1000);
        }
    }
    
    // Create rose petals initially and then periodically
    createRosePetals();
    setInterval(createRosePetals, 15000);

    // Create floating hearts
    function createFloatingHearts() {
        const heartsCount = 10;
        
        for (let i = 0; i < heartsCount; i++) {
            setTimeout(() => {
                const heart = document.createElement('div');
                heart.classList.add('heart');
                
                // Random position
                heart.style.left = Math.random() * 100 + '%';
                
                // Random animation duration
                const duration = 5 + Math.random() * 10;
                heart.style.animationDuration = `${duration}s`;
                
                // Random size
                const size = 10 + Math.random() * 20;
                heart.style.width = `${size}px`;
                heart.style.height = `${size}px`;
                
                chatContainer.appendChild(heart);
                
                // Remove heart after animation completes
                setTimeout(() => {
                    heart.remove();
                }, duration * 1000);
            }, i * 800);
        }
    }
    
    // Create hearts initially and then every 10 seconds
    createFloatingHearts();
    setInterval(createFloatingHearts, 10000);

    // Function to add a message to the chat
    function addMessage(content, isUser) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        
        if (isUser) {
            messageDiv.classList.add('user-message');
        } else {
            messageDiv.classList.add('bot-message');
        }
        
        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content');
        
        const paragraph = document.createElement('p');
        paragraph.textContent = content;
        
        messageContent.appendChild(paragraph);
        messageDiv.appendChild(messageContent);
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to show typing indicator
    function showTypingIndicator() {
        const indicator = document.createElement('div');
        indicator.classList.add('message', 'bot-message', 'typing-indicator');
        indicator.id = 'typing-indicator';
        
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('span');
            indicator.appendChild(dot);
        }
        
        chatMessages.appendChild(indicator);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to remove typing indicator
    function removeTypingIndicator() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) {
            indicator.remove();
        }
    }
    
    // Function to send message
    async function sendMessage() {
        const message = userInput.value.trim();
        
        if (message === '') return;
        
        // Add user message to chat
        addMessage(message, true);
        
        // Clear input field
        userInput.value = '';
        
        // Show typing indicator
        showTypingIndicator();
        
        try {
            // Send the message to the server
            const response = await fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message }),
            });
            
            const data = await response.json();
            
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add bot response to chat
            addMessage(data.message, false);
            
        } catch (error) {
            console.error('Error:', error);
            removeTypingIndicator();
            addMessage('Sorry, I had trouble processing your message. Please try again.', false);
        }
    }
    
    // Event listener for send button
    sendBtn.addEventListener('click', sendMessage);
    
    // Event listener for Enter key
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    // Event listener for reset button
    resetBtn.addEventListener('click', async () => {
        try {
            await fetch('/reset_conversation', {
                method: 'POST',
            });
            
            // Clear chat messages
            chatMessages.innerHTML = '';
            
            // Add initial greeting
            addMessage('Hi there! I\'m Aria. What\'s your name?', false);
            
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
