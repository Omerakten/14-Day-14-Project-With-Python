#Inch Calculator
while True:
    choice = input("Which conversion do you want to make? Type 'cm' for centimeters to inches, or 'in' for inches to centimeters: ")
    if choice == "cm":
        cm = float(input("Enter the length in centimeters: "))
        inch = cm / 2.54
        print(f"{cm} centimeters is equal to {inch:.2f} inches.")
        break
    elif choice == "in":
        inch = float(input("Enter the length in inches: "))
        cm = inch * 2.54
        print(f"{inch} inches is equal to {cm:.2f} centimeters.")
        break
    else:
        print("Invalid choice. Please try again.")
