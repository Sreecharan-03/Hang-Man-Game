import tkinter as tk
import random

# Hangman ASCII Stages
stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

# Expanded Word Categories
categories = {
    "Animals": [
        "elephant", "tiger", "giraffe", "kangaroo", "dolphin", "penguin", "crocodile", "hippopotamus",
        "cheetah", "rhinoceros", "ostrich", "chameleon", "panda", "zebra", "leopard"
    ],
    "Fruits": [
        "apple", "banana", "cherry", "mango", "grape", "pineapple", "strawberry", "watermelon",
        "pomegranate", "blueberry", "raspberry", "peach", "coconut", "kiwi", "blackberry"
    ],
    "Countries": [
        "india", "canada", "germany", "brazil", "france", "argentina", "switzerland", "portugal",
        "australia", "singapore", "mexico", "netherlands", "thailand", "norway", "egypt"
    ],
    "Sports": [
        "football", "cricket", "tennis", "badminton", "hockey", "basketball", "volleyball",
        "baseball", "rugby", "cycling", "golf", "wrestling", "boxing", "swimming", "fencing"
    ]
}

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x550")

# UI Components
title_label = tk.Label(root, text="Hangman Game", font=("Arial", 20, "bold"))
title_label.pack()

category_label = tk.Label(root, text="Choose a Category:", font=("Arial", 14))
category_label.pack()

# Game Variables
selected_word = ""
hidden_word = []
attempts = 0
max_attempts = len(stages) - 1

word_display = tk.StringVar()
word_label = tk.Label(root, textvariable=word_display, font=("Arial", 24))
word_label.pack()

hangman_display = tk.StringVar()
hangman_label = tk.Label(root, textvariable=hangman_display, font=("Courier", 12), fg="red")
hangman_label.pack()

attempts_display = tk.StringVar()
attempts_label = tk.Label(root, textvariable=attempts_display, font=("Arial", 14))
attempts_label.pack()

message = tk.StringVar()
message_label = tk.Label(root, textvariable=message, font=("Arial", 16, "bold"), fg="blue")
message_label.pack()

letters_frame = tk.Frame(root)
letters_frame.pack()

category_frame = tk.Frame(root)
category_frame.pack()

# Function to Start the Game
def start_game(category):
    global selected_word, hidden_word, attempts
    selected_word = random.choice(categories[category])
    hidden_word = ["_"] * len(selected_word)
    attempts = 0
    word_display.set(" ".join(hidden_word))
    hangman_display.set(stages[attempts])
    attempts_display.set(f"Attempts Left: {max_attempts - attempts}")
    message.set("")

    # Clear existing buttons
    for widget in letters_frame.winfo_children():
        widget.destroy()

    # Create letter buttons
    for letter in "abcdefghijklmnopqrstuvwxyz":
        btn = tk.Button(letters_frame, text=letter, width=3, font=("Arial", 12),
                        command=lambda l=letter: guess_letter(l))
        btn.grid(row=ord(letter) // 10, column=ord(letter) % 10)

# Function to Handle Letter Guessing
def guess_letter(letter):
    global attempts
    if letter in selected_word:
        for i, char in enumerate(selected_word):
            if char == letter:
                hidden_word[i] = letter
        word_display.set(" ".join(hidden_word))

        if "_" not in hidden_word:
            message.set(" You Win! The word was: " + selected_word)
            replay_game()
    else:
        attempts += 1
        hangman_display.set(stages[attempts])
        attempts_display.set(f"Attempts Left: {max_attempts - attempts}")

        if attempts == max_attempts:
            message.set(" Game Over! The word was: " + selected_word)
            replay_game()

# Function to Replay the Game
def replay_game():
    replay_button = tk.Button(root, text=" Play Again", font=("Arial", 14), bg="blue", fg="white", command=reset_game)
    replay_button.pack()

def reset_game():
    for widget in root.winfo_children():
        widget.destroy()
    main_ui()

# Main UI Setup
def main_ui():
    global category_label, category_frame
    title_label.pack()
    category_label.pack()
    category_frame.pack()

    for category in categories.keys():
        btn = tk.Button(category_frame, text=category, font=("Arial", 14), width=10, bg="orange", fg="white",
                        command=lambda c=category: start_game(c))
        btn.pack(side=tk.LEFT, padx=5, pady=5)

    word_label.pack()
    hangman_label.pack()
    attempts_label.pack()
    message_label.pack()
    letters_frame.pack()

main_ui()
root.mainloop()