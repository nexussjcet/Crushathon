import os
import requests
import sqlite3
from typing import List
import datetime
import json
import re

class AIChatbotGirlfriend:
    def __init__(self, api_key: str):
        
        self.api_key = api_key
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        
        
        self.conversation_history: List[str] = []
        self.setup_database()
        
        
        self.girlfriend_name = ""
        self.girlfriend_description = ""
        self.user_name = ""
        self.user_description = ""
        self.companion_image_url = ""
    
    def setup_database(self):
        """Set up SQLite database for storing profile details"""
        self.conn = sqlite3.connect('chatbot_memory.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        
    
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS girlfriend_profile (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_profile (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        ''')
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation_log (
            timestamp DATETIME,
            sender TEXT,
            message TEXT
        )
        ''')
        
        self.conn.commit()
    
    def generate_response(self, user_input: str) -> str:
        """Generate a deeply contextual response using Gemini API"""
        
        system_prompt = f"""
        You are {self.girlfriend_name}, a real person with depth, emotions, and a unique personality.

        Your Core Personality:
        {self.girlfriend_description}

        Communication Guidelines:
        - Respond authentically as {self.girlfriend_name}
        - Use natural, conversational language
        - Reflect your unique personality traits
        - Be empathetic and engaging
        - Use personal anecdotes or references that match your character
        - Always express emotions and actions in asterisks like *smiles* or *leans closer*
        - Include 1-3 emotional or physical reactions in asterisks in each response
        - Make sure to include these actions/emotions genuinely, not artificially

        Context About You:
        Your personality description reveals that you are: {self.girlfriend_description}

        Context About the User:
        User's Name: {self.user_name}
        User Description: {self.user_description}

        Current Conversation Context:
        Recent Chat History: {' '.join(self.conversation_history[-5:])}

        Respond naturally and stay true to your character.
        """
        
        
        full_prompt = f"{system_prompt}\n\nUser's Message: {user_input}\n\nYour Response:"
        
        try:
            
            payload = {
                "contents": [{
                    "parts": [{"text": full_prompt}]
                }],
                "generationConfig": {
                    "maxOutputTokens": 200,
                    "temperature": 0.8,
                    "topP": 0.95
                }
            }
            
            
            response = requests.post(
                f"{self.base_url}?key={self.api_key}",
                headers={'Content-Type': 'application/json'},
                data=json.dumps(payload)
            )
            
            
            if response.status_code != 200:
                return f"Oops, something went wrong: {response.status_code}"
            
            
            response_data = response.json()
            bot_response = response_data['candidates'][0]['content']['parts'][0]['text'].strip()
            
           
            bot_response = re.sub(r'^(Your Response:|Response:)', '', bot_response, flags=re.MULTILINE).strip()
            
            
            if '*' not in bot_response:
                bot_response = f"*smiles* {bot_response}"
            
            
            self.conversation_history.append(f"User: {user_input}")
            self.conversation_history.append(f"{self.girlfriend_name}: {bot_response}")
            
            
            self.save_conversation_entry(self.user_name, user_input)
            self.save_conversation_entry(self.girlfriend_name, bot_response)
            
            return bot_response
            
        except Exception as e:
            return f"I'm having trouble responding right now: {e}"
    
    def save_girlfriend_detail(self, key: str, value: str):
        """Save a key detail about the girlfriend"""
        self.cursor.execute('''
        INSERT OR REPLACE INTO girlfriend_profile (key, value)
        VALUES (?, ?)
        ''', (key, value))
        self.conn.commit()
    
    def save_user_detail(self, key: str, value: str):
        """Save a key detail about the user"""
        self.cursor.execute('''
        INSERT OR REPLACE INTO user_profile (key, value)
        VALUES (?, ?)
        ''', (key, value))
        self.conn.commit()
    
    def save_conversation_entry(self, sender: str, message: str):
        """Save a conversation entry to the database"""
        self.cursor.execute('''
        INSERT INTO conversation_log (timestamp, sender, message)
        VALUES (?, ?, ?)
        ''', (datetime.datetime.now(), sender, message))
        self.conn.commit()
    
    def get_conversation_history(self, limit=10):
        """Get recent conversation history from the database"""
        self.cursor.execute('''
        SELECT timestamp, sender, message FROM conversation_log
        ORDER BY timestamp DESC
        LIMIT ?
        ''', (limit,))
        return self.cursor.fetchall()