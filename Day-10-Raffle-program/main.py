#Draw Program

import random

num_of_winners = int(input("How many winners do you want to choose? "))
participants = []

for i in range(1, num_of_winners + 1):
    name = input(f"Please enter the name of the {i}. winner: ")
    participants.append(name)

print("\nThe draw is starting...\n")

winners = random.sample(participants, num_of_winners)

for i, winner in enumerate(winners):
    print(f"{i+1}. winner: {winner}")

print("\nThe draw is complete. Congratulations!")
