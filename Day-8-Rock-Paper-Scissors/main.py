#Rock Paper Scissors game
import random

print("Welcome to Rock Paper Scissors game!")

options = ["Rock", "Paper", "Scissors"]

while True:
    user_choice = input("Rock, Paper, or Scissors? (Enter Q to quit): ").capitalize()

    if user_choice == "Q":
        print("Exiting the game.")
        break

    if user_choice not in options:
        print("Please enter a valid choice!")
        continue

    computer_choice = random.choice(options)

    print(f"\nYou chose: {user_choice} \nComputer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Tie game!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (
            user_choice == "Paper" and computer_choice == "Rock") or (
            user_choice == "Scissors" and computer_choice == "Paper"):
        print("Congratulations, you win!")
    else:
        print("Sorry, you lose!")
