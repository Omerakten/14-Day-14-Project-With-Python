#Dice Game
import random
while True:
    choice = input("Zar atmak için: x Kapatmak için: q\n")
    if choice == "x" or choice == "X":
        dice1 = random.randint(1 , 6)
        dice2 = random.randint(1 , 6)
        total = dice1+dice2
        print(f"Dice1: {dice1}, Dice2: {dice2}, Total:{total}")
    else:
        print("System Shut Down..")
        break


