#Colors
Red = "\u001b[31m"
Green="\u001b[32m"
Yellow="\u001b[33m"
Magenta="\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Black = "\u001b[30m"

# Calculator Project
class Calculator():

    def app(self):
        print(f"{Cyan}█████████████{Yellow} Welcome To The Calculator {Cyan}█████████████{Black}")
    def select(self):
        input_1 = int(input(f"{Yellow}Please enter a number: "))
        input_2 = int(input("Please enter a number: "))

        print(    f"{Cyan}1- Plus          +\n"
                  "2- Minus         -\n"
                  "3- Divided By    /\n"
                  f"4- Multiplied By x\n{Black}")

        select = input(f"{Red}Please choose: {Magenta}")

        if select == "1":
            result = input_1 + input_2
            print("Result: {}".format(result))
            self.loop()
        if select == "2":
            result = input_1 - input_2
            print("Result: {}".format(result))
            self.loop()
        if select == "3":
            result = input_1 // input_2
            print("Result: {}".format(result))
            self.loop()
        if select == "4":
            result = input_1 * input_2
            print("Result: {}".format(result))
            self.loop()



    def loop(self):
        select = input(f"{Red}Please choose{Black}\n"
                       "c - Continue\n"
                       "q - System Shut Down\n"
                       "Select: ")
        if select == "c" or select == "C":
            self.select()
        if select == "q" or select == "Q":
            print("System Shut Down..")

if __name__ == '__main__':
    calc = Calculator()
    calc.app()
    calc.select()