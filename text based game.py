import tkinter as tk


# Function to update the story and choices
def update_story(text, options):
    story_label.config(text=text)

    # Clear previous buttons
    for btn in choice_buttons:
        btn.pack_forget()

    # Create new buttons for options
    choice_buttons.clear()
    for option_text, option_func in options:
        btn = tk.Button(root, text=option_text, command=option_func, width=30)
        btn.pack(pady=5)
        choice_buttons.append(btn)


# Game scenes
def start():
    text = "You are at a crossroad. Where do you want to go?"
    options = [("Go left into the forest", forest),
               ("Go right towards the mountains", mountains)]
    update_story(text, options)


def forest():
    text = "🌲 You entered the forest and see a wild wolf!"
    options = [("Fight the wolf", lambda: game_over("The wolf was too strong!")),
               ("Run away", lambda: win("You escaped safely and found a treasure chest!"))]
    update_story(text, options)


def mountains():
    text = "⛰️ You climb the mountain and find a river blocking your way."
    options = [("Swim across", lambda: game_over("The current was too strong!")),
               ("Look for a bridge", lambda: win("You found a bridge and safely crossed!"))]
    update_story(text, options)


def game_over(message):
    update_story(f"💀 Game Over! {message}", [("Restart", start)])


def win(message):
    update_story(f"🎉 You Win! {message}", [("Play Again", start)])


# Tkinter setup
root = tk.Tk()
root.title("Adventure Game")
root.geometry("400x300")

story_label = tk.Label(root, text="", wraplength=380, font=("Arial", 12))
story_label.pack(pady=20)

choice_buttons = []

# Start the game
start()

root.mainloop()
