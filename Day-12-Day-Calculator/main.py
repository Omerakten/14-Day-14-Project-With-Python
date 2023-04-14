#Day Calculator
import datetime

current_date = datetime.date.today()

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
target_date = datetime.date(year, month, day)
remaining_days = (target_date - current_date).days

print(f"There are {remaining_days} days until the target date.")
