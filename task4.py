import tkinter as tk
import tkinter.messagebox as msgbox
import random


def determine_winner(user_choice, computer_choice):
    outcomes = {
        ("rock", "scissors"): "You win!",
        ("scissors", "paper"): "You win!",
        ("paper", "rock"): "You win!",
        ("scissors", "rock"): "Computer wins!",
        ("paper", "scissors"): "Computer wins!",
        ("rock", "paper"): "Computer wins!",
    }

    if user_choice == computer_choice:
        return "It's a tie!"

    return outcomes[(user_choice, computer_choice)]


def play():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)

    play_again = msgbox.askquestion("Play Again", "Do you want to play again?")
    if play_again == "no":
        window.destroy()
    else:
        user_choice_var.set(choices[0])
        user_choice_label.config(text="")
        computer_choice_label.config(text="")
        result_label.config(text="")


window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

choices = ["rock", "paper", "scissors"]

title_label = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Helvetica", 20))
title_label.pack(pady=20)

instructions_label = tk.Label(window, text="Choose your move:")
instructions_label.pack()

user_choice_var = tk.StringVar()
user_choice_var.set(choices[0])

user_choice_frame = tk.Frame(window)
user_choice_frame.pack()

for choice in choices:
    choice_radio = tk.Radiobutton(user_choice_frame, text=choice, variable=user_choice_var, value=choice)
    choice_radio.pack(side=tk.LEFT, padx=10)

play_button = tk.Button(window, text="Play", command=play, font=("Helvetica", 14))
play_button.pack(pady=20)

user_choice_label = tk.Label(window, text="", font=("Helvetica", 14))
user_choice_label.pack()

computer_choice_label = tk.Label(window, text="", font=("Helvetica", 14))
computer_choice_label.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 18), fg="blue")
result_label.pack()

window.mainloop()
