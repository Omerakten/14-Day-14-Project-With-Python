#horoscope calculator
day = int(input("Enter your birth day (e.g. 24): "))
month = input("Enter your birth month (e.g. January): ")

months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
"July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

if month == "January":
    zodiac_sign = "Capricorn" if (day <= 20) else "Aquarius"
elif month == "February":
    zodiac_sign = "Aquarius" if (day <= 19) else "Pisces"
elif month == "March":
    zodiac_sign = "Pisces" if (day <= 20) else "Aries"
elif month == "April":
    zodiac_sign = "Aries" if (day <= 20) else "Taurus"
elif month == "May":
    zodiac_sign = "Taurus" if (day <= 21) else "Gemini"
elif month == "June":
    zodiac_sign = "Gemini" if (day <= 21) else "Cancer"
elif month == "July":
    zodiac_sign = "Cancer" if (day <= 22) else "Leo"
elif month == "August":
    zodiac_sign = "Leo" if (day <= 22) else "Virgo"
elif month == "September":
    zodiac_sign = "Virgo" if (day <= 22) else "Libra"
elif month == "October":
    zodiac_sign = "Libra" if (day <= 22) else "Scorpio"
elif month == "November":
    zodiac_sign = "Scorpio" if (day <= 21) else "Sagittarius"
elif month == "December":
    zodiac_sign = "Sagittarius" if (day <= 21) else "Capricorn"

print("Your zodiac sign is:", zodiac_sign)


