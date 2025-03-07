import tkinter as tk
from llama_cpp import Llama
import threading

MODEL_PATH = "C:/models/llama-2-7b-chat.ggmlv3.q4_0.bin"

try:
    model = Llama(
        model_path=MODEL_PATH,
        n_ctx=2048,
        n_threads=4,
        verbose=False
    )
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def send_message():
    user_input = entry.get().strip()
    if not user_input or model is None:
        return
    entry.delete(0, tk.END)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_input}\n", "user")
    chat_log.config(state=tk.DISABLED)
    
    threading.Thread(target=generate_response, args=(user_input,)).start()

def generate_response(user_input):
    try:
        prompt = f"""### Instruction:
        You are a helpful AI assistant. Answer the user's question politely.

        ### User:
        {user_input}

        ### Assistant:"""
        
        response = model(prompt, max_tokens=200, stop=["### User"], echo=False)

        response_text = response.get('choices', [{}])[0].get('text', '').strip()
        
        root.after(0, display_response, response_text)
    
    except Exception as e:
        root.after(0, display_response, f"Error: {str(e)}")

def display_response(response_text):
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"Bot: {response_text}\n\n", "bot")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)


root = tk.Tk()
root.title("Crush")

chat_log = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
chat_log.tag_config("user", foreground="blue")
chat_log.tag_config("bot", foreground="green")
chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, command=chat_log.yview)
chat_log.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
