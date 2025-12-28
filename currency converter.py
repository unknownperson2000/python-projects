import tkinter as tk

# Exchange rate (1 USD = 0.71 JOD as an example)
exchange_rate = 0.71


def convert():
    try:
        # Get the amount entered by the user
        amount = float(amount_entry.get())
        direction = direction_var.get()

        if direction == "USD → JOD":
            result = amount * exchange_rate
            result_label.config(text=f"{amount} USD = {result:.2f} JOD")
        else:  # JOD → USD
            result = amount / exchange_rate
            result_label.config(text=f"{amount} JOD = {result:.2f} USD")
    except ValueError:
        result_label.config(text="❌ Please enter a valid number")


# GUI setup
root = tk.Tk()
root.title("USD ↔ JOD Converter")
root.geometry("300x200")

tk.Label(root, text="Enter the amount to convert:").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack()

# Conversion direction
direction_var = tk.StringVar(root)
direction_var.set("USD → JOD")
tk.OptionMenu(root, direction_var, "USD → JOD", "JOD → USD").pack(pady=5)

tk.Button(root, text="Convert", command=convert).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
