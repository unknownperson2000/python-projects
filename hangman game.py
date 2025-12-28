import random

words = ["python", "flask", "hangman", "developer", "computer"]
word = random.choice(words)

guessed_letters = []
tries = 5

print("🎯 Welcome to Hangman!")
print("Guess the word!")

while tries > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Tries left:", tries)

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter ONE letter only.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        print("❌ Wrong guess!")
        tries -= 1
    else:
        print("✅ Good guess!")

    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break
else:
    print("\n💀 Game Over! The word was:", word)
