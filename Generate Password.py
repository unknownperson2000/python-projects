import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Enter a positive number")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# GUI setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")

tk.Label(root, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

root.mainloop()
