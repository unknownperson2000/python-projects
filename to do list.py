import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete")

# Main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

# Entry
entry = tk.Entry(root, width=25, font=("Arial", 12))
entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=30, height=15)
listbox.pack(pady=10)

root.mainloop()
