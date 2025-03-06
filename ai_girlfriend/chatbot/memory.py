class ConversationMemory:
    def __init__(self):
        """Initialize the conversation memory manager."""
        self.users = {}
    
    def initialize_user(self, user_id):
        """Initialize a new user in the memory system."""
        if user_id not in self.users:
            self.users[user_id] = {
                'conversation': [],
                'profile': {
                    'name': None,
                    'interests': [],
                    'mood': 'neutral'
                }
            }
    
    def add_message(self, user_id, role, content):
        """Add a message to the conversation history."""
        if user_id in self.users:
            self.users[user_id]['conversation'].append({
                'role': role,
                'content': content
            })
    
    def get_conversation_history(self, user_id):
        """Get the conversation history for a user."""
        if user_id in self.users:
            return self.users[user_id]['conversation']
        return []
    
    def get_user_profile(self, user_id):
        """Get the user profile information."""
        if user_id in self.users:
            return self.users[user_id]['profile']
        return {}
    
    def update_user_profile(self, user_id, user_message, ai_response):
        """
        Update user profile based on conversation.
        Uses simple heuristics to extract information.
        """
        if user_id not in self.users:
            return
        
        profile = self.users[user_id]['profile']
        
        # Extract name if not already known
        if profile['name'] is None and "my name is" in user_message.lower():
            name_part = user_message.lower().split("my name is")[1].strip()
            # Take the first word after "my name is"
            profile['name'] = name_part.split()[0].capitalize()
        
        # Extract interests
        interest_keywords = ["like", "enjoy", "love", "hobby", "interested in"]
        for keyword in interest_keywords:
            if keyword in user_message.lower():
                # Simple extraction - could be enhanced with NLP
                parts = user_message.lower().split(keyword)[1].strip()
                potential_interest = parts.split('.')[0].split(',')[0].strip()
                if potential_interest and len(potential_interest) > 2:
                    profile['interests'].append(potential_interest)
                    # Remove duplicates
                    profile['interests'] = list(set(profile['interests']))
        
        # Determine mood from message
        mood_indicators = {
            'happy': ['happy', 'glad', 'joy', 'excited', ':)', '😊'],
            'sad': ['sad', 'unhappy', 'disappointed', ':(', '😢'],
            'angry': ['angry', 'mad', 'frustrated', 'upset', '😠'],
            'curious': ['curious', 'wondering', 'question', '?']
        }
        
        for mood, indicators in mood_indicators.items():
            for indicator in indicators:
                if indicator in user_message.lower():
                    profile['mood'] = mood
                    break
    
    def clear_conversation(self, user_id):
        """Clear the conversation history for a user."""
        if user_id in self.users:
            self.users[user_id]['conversation'] = []
