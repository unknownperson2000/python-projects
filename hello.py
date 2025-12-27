import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hello World GUI")
window.geometry("300x150")

# Create a label
label = tk.Label(window, text="Hello, World! THIS IS ENGINEER NOUR", font=("Arial", 16))
label.pack(expand=True)

# Run the app
window.mainloop()
