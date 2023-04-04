#Colors
Red = "\u001b[31m"
Green="\u001b[32m"
Yellow="\u001b[33m"
Magenta="\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Black = "\u001b[30m"
#exam average calculation


print(f"{Cyan}█████████████{Yellow} Welcome to the Exam Average Calculation {Cyan}█████████████{Black}")
class App:
    def program(self):
        exam_size = int(input("How many exams do you have? "))
        exam_grades = []
        exam_percents = []

        for i in range(exam_size):
            grade = float(input(f"Grade for exam {i+1}: "))
            exam_grades.append(grade)
            percent = float(input(f"Percentage for exam {i+1}: "))
            exam_percents.append(percent)

        total_weighted = sum([grade * percent / 100 for grade, percent in zip(exam_grades, exam_percents)])
        average_grade = sum(exam_grades) / exam_size

        print(f"Your weighted average exam grade calculated with percentage weights: {total_weighted:.2f}")
        print(f"Your average exam grade is: {average_grade}")

        while True:
            choice = input("Would you like to run the program again? (y/n): ")
            if choice.lower() == "y":
                self.program()
            elif choice.lower() == "n":
                break
            else:
                print("Invalid choice. Please enter y or n.")

app = App()
app.program()


