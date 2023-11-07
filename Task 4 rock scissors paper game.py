import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def make_choice(choice):
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and configure labels
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16))
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Choose your move:")
instruction_label.pack()

# Create buttons for user's choice
rock_button = tk.Button(root, text="Rock", command=lambda: make_choice("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: make_choice("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: make_choice("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
