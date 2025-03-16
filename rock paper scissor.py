import tkinter as tk
import random
from tkinter import messagebox
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a Tie! 😐"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "Computer Wins! 🤖"
        computer_score += 1
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result, fg="green" if "Win" in result else "red" if "Computer Wins" in result else "blue")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="Let's Play!", fg="black")
    score_label.config(text="Score - You: 0 | Computer: 0")
root = tk.Tk()
root.title("🎮 Rock-Paper-Scissors")
root.geometry("400x500")
root.config(bg="#FDEBD0") 
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#FDEBD0", fg="black")
title_label.pack(pady=10)
user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14), bg="#FDEBD0")
user_choice_label.pack()
computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14), bg="#FDEBD0")
computer_choice_label.pack()
result_label = tk.Label(root, text="Let's Play!", font=("Arial", 16, "bold"), bg="#FDEBD0")
result_label.pack(pady=10)
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 14, "bold"), bg="#FDEBD0")
score_label.pack(pady=10)
button_frame = tk.Frame(root, bg="#FDEBD0")
button_frame.pack(pady=10)
btn_font = ("Arial", 14, "bold")
btn_colors = {"Rock": "#3498DB", "Paper": "#E74C3C", "Scissors": "#2ECC71"}
for choice in choices:
    btn = tk.Button(button_frame, text=choice, font=btn_font, bg=btn_colors[choice], fg="white", width=10, height=2,
                    command=lambda c=choice: play_game(c))
    btn.pack(side="left", padx=5)
reset_button = tk.Button(root, text="Reset Score", font=btn_font, bg="#F39C12", fg="white", width=15, height=2, command=reset_game)
reset_button.pack(pady=10)
root.mainloop()
