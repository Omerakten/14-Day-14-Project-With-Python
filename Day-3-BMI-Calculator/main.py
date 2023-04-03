#Colors
Red = "\u001b[31m"
Green="\u001b[32m"
Yellow="\u001b[33m"
Magenta="\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Black = "\u001b[30m"
# Body Mass Index Calculator
print(f"{Cyan}█████████████{Yellow} Welcome to the Body Mass Index Calculator {Cyan}█████████████{Black}")
height = float(input(f"{Red}Please enter your height(cm): {Black}"))
weight = float(input(f"{Red}Please enter your weight(kg): {Black}"))
result =  weight/ (height*height)
print(f"{Yellow}Body Mass Index: {Cyan}" + str(result))
bmi = int(result)
if bmi <= 18:
    print("Thin")
if bmi >= 18 and bmi <= 24:
    print("Normal")
if bmi >= 25 and bmi < 29:
    print("Fat")
if bmi >= 30 and bmi <= 34:
    print("1.degree obesity")
if bmi >= 35 and bmi <= 39:
    print("2.degree obesity")
if bmi >= 40:
    print("3.degree obesity")
