#Desi Calculator
while True:
    name = input("Please enter the name of the item to be calculated : ")
    width = int(input("Please enter the width of the item (in cm): "))
    length = int(input("Please enter the length of the item (in cm): "))
    height = int(input("Please enter the height of the item (in cm): "))
    result = width * length * height
    result2 = result / 3000
    rounded_result = round(result2) if result2 != int(result2) else int(result2)
    print(f"{name} is {rounded_result} desi.")

    choice = input("Enter 'r' to rerun or 'e' to exit: ")
    if choice == 'e':
        print("System Shut Down..")
        break
