
import sys
import os
import tkinter as tk
from tkinter import scrolledtext, PhotoImage

# ✅ Ensure `tamara.py` can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import tamara  # Import Tamara's chatbot logic
except ImportError:
    print("Error: tamara.py not found! Make sure it's in the same folder as tamara_gui.py.")
    exit()

# 🎨 Trendy Theme
BG_COLOR = "#1E1E2E"  # Dark Purple
TEXT_COLOR = "#E1E1E6"  # Light Grey
USER_COLOR = "#82AAFF"  # Bright Blue
BOT_COLOR = "#FF79C6"  # Pink
ENTRY_BG = "#2E2E3E"  # Dark Grey
BTN_BG = "#FF4081"  # Vibrant Pink
BTN_HOVER = "#E73370"  # Darker Pink
FONT_MAIN = ("Helvetica", 13, "bold")
FONT_TEXT = ("Arial", 12)

# 🔥 Send Message Function
def send_message(event=None):
    """ Get user input, show it in chat, and display Tamara's response. """
    user_input = entry_box.get().strip()
    
    if user_input:  
        chat_display.insert(tk.END, f"\nYou: {user_input}\n", "user")
        chat_display.yview(tk.END)  # Auto-scroll
        entry_box.delete(0, tk.END)

        try:
            bot_reply = tamara.chat_with_tamara(user_input)  # Get Tamara's response
            chat_display.insert(tk.END, f"Tamara: {bot_reply}\n", "bot")
            chat_display.yview(tk.END)  # Auto-scroll
        except Exception as e:
            chat_display.insert(tk.END, f"Error: {e}\n\n", "error")
            chat_display.yview(tk.END)

# 🔥 Hover Effect for Button
def on_hover(event):
    send_button.config(bg=BTN_HOVER)

def on_leave(event):
    send_button.config(bg=BTN_BG)

# 🔥 Create GUI Window
root = tk.Tk()
root.title("Tamara - AI Life Partner 💖")
root.geometry("600x600")  # Window size
root.configure(bg=BG_COLOR)  # Background color

# 🔥 Chat Display Box (Better Styling)
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15, font=FONT_TEXT, bg=BG_COLOR, fg=TEXT_COLOR, bd=0)
chat_display.tag_configure("user", foreground=USER_COLOR)
chat_display.tag_configure("bot", foreground=BOT_COLOR)
chat_display.tag_configure("error", foreground="red")
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 🔥 Input Frame (Modern Look)
input_frame = tk.Frame(root, bg=BG_COLOR)
input_frame.pack(pady=5, fill=tk.X)

# 🔥 Input Box (Rounded & Stylish)
entry_box = tk.Entry(input_frame, width=40, font=FONT_MAIN, bg=ENTRY_BG, fg=TEXT_COLOR, bd=2, relief=tk.FLAT, insertbackground="white")
entry_box.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)
entry_box.bind("<Return>", send_message)  # Press Enter to send message

# 🔥 Send Button (Gradient & Icon)
send_button = tk.Button(input_frame, text="➤", command=send_message, font=("Arial", 14), bg=BTN_BG, fg="white", bd=0, relief=tk.FLAT, width=3)
send_button.pack(side=tk.RIGHT, padx=10)
send_button.bind("<Enter>", on_hover)
send_button.bind("<Leave>", on_leave)

# 🔥 Run GUI Loop
root.mainloop()
