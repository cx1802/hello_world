"""
Peidi Xie
February 1 th, 2019
Introduction to Programming, Section 03
Problem 3: NYU Calendar
"""

# prompt the user to enter the number of the month
# and the number of the day of the user's intended date
n_month = int(input("Enter a month (1-12): "))
n_day = int(input("Enter a day (1-31): "))

# define a varible for months that links the number of the month with its English expression
if n_month == 1:
    w_month = "January"
elif n_month == 2:
    w_month = "February"
elif n_month == 3:
    w_month = "March"
elif n_month == 4:
    w_month = "April"
elif n_month == 5:
    w_month = "May"
elif n_month == 6:
    w_month = "June"
elif n_month == 7:
    w_month = "July"
elif n_month == 8:
    w_month = "August"
elif n_month == 9:
    w_month = "September"
elif n_month == 10:
    w_month = "October"
elif n_month == 11:
    w_month = "November"
elif n_month == 12:
    w_month = "December"
else:
    w_month = "unknown"

# define a variable for days that adds appropriate descriptor to the numerical value of the day
if n_day % 10 == 1:
    w_day = str(n_day) + "st"
elif n_day % 10 == 2:
    w_day = str(n_day) + "nd"
elif n_day % 10 == 3:
    w_day = str(n_day) + "rd"
else:
    w_day = str(n_day) + "th"

# tell the user if the user enter an invalid date according to the law of calendar
if n_month < 1 or n_month >12:
    print("Sorry, that's not a valid date")
elif n_day < 1 or n_day > 31:
    print("Sorry, that's not a valid date")
elif n_month == 2 and n_day > 28:
    print("Sorry, that's not a valid date")
elif (n_month // 8 + n_month % 2) % 2 == 0 and n_day > 30:
    print("Sorry, that's not a valid date")
# tell the user if the date the user enter is within the range of the Spring 2019 term,
# an NYU holiday, one of the special days such as final exams or reading day, or not
else:
    date = int(str(n_month) + str(n_day))
    if date < 128:
        print(w_month, w_day, end="")
        print(", 2019 is before the start of the Spring 2019 term.")
    elif date == 218:
        print(w_month, w_day, end="")
        print(", 2019 is President's Day. NYU is not open on this day.")
    elif date >= 318 and date <= 324:
        print(w_month, w_day, end="")
        print(", 2019 is in Spring Break. NYU is not open on this day.")
    elif date > 521:
        print(w_month, w_day, end="")
        print(", 2019 is after the end of the Spring 2019 term.")
    elif date == 514:
        print(w_month, w_day, end="")
        print(", 2019 is the reading day.")
    elif date >= 515 and date <= 521:
        print(w_month, w_day, end="")
        print(", 2019 has final exams.")
    else:
        print(w_month, w_day, end="")
        print(", 2019 is not a holiday at NYU. NYU is open on this day.")



