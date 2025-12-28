import tkinter as tk
from tkinter import scrolledtext

# Keyword-based responses
responses = {
    "hi": "Hello! How are you?",
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing fine! How about you?",
    "help": "I can chat with you! Try saying hi or asking how I am.",
    "bye": "Goodbye! Have a nice day!"
}

def get_response(user_msg):
    user_msg = user_msg.lower()
    for key in responses:
        if key in user_msg:
            return responses[key]
    return "Sorry, I didn't understand that."

def send_message(event=None):
    user_msg = user_entry.get().strip()
    if not user_msg:
        return

    chat_area.config(state="normal")
    chat_area.insert(tk.END, "You: " + user_msg + "\n", "user")
    user_entry.delete(0, tk.END)

    if "bye" in user_msg.lower():
        bot_msg = responses["bye"]
        chat_area.insert(tk.END, "Bot: " + bot_msg + "\n\n", "bot")
        chat_area.config(state="disabled")
        return

    bot_msg = get_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + bot_msg + "\n\n", "bot")
    chat_area.config(state="disabled")
    chat_area.yview(tk.END)

# Tkinter setup
root = tk.Tk()
root.title("Smart Chatbot")
root.geometry("450x500")

chat_area = scrolledtext.ScrolledText(root, state="disabled", wrap="word", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill="both", expand=True)

chat_area.tag_config("user", foreground="blue")
chat_area.tag_config("bot", foreground="green")

user_entry = tk.Entry(root, font=("Arial", 12))
user_entry.pack(side="left", fill="x", padx=10, pady=10, expand=True)
user_entry.focus()
user_entry.bind("<Return>", send_message)  # Press Enter to send

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side="right", padx=10, pady=10)

root.mainloop()
