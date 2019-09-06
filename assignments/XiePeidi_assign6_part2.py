"""
Peidi Xie
April 1st, 2019
Introduction to Programming, Section 03
Part 2
"""

# prompt the user to enter the number of problems
num_problems = int(input("How many numbers would you like to attempt? "))
# the number of problems has to be positive.
# if not, ask the user to enter again until valid data is supplied
while num_problems <= 0:
    print("Invalid number, try again")
    print()
    num_problems = int(input("How many numbers would you like to attempt? "))

# prompt the user to enter the width for the numbers
width = int(input("How wide do you want your digits to be? 5-10: "))
# the numerical value of the width has to be within the range of 5 to 10
# if not, ask the user to enter again until valid data is supplied
while width < 5 or width > 10:
    print("Invalid width, try again")
    print()
    width = int(input("How wide do you want your digits to be? 5-10: "))

# prompt the user to enter a single character to generate the numbers
print()
character = input("What character would you like to use? ")
# if the string has more than one character, ask the user to enter again until valid data is supplied
while len(character) > 1:
    print("String too long, try again")
    character = input("What character would you like to use? ")

# ask the user if he or she wants to activate the drill mode
drill = input("Would you like to activate 'drill' mode? yes or no: ")
# if the user answers neither "yes" nor "no", ask the user to answer again until valid data is supplied
while drill != "yes" and drill != "no":
    print("Invalid input, try again")
    print()
    drill = input("Would you like to activate 'drill' mode? yes or no: ")

# indicate the start of the game
print()
print("Here we go!")

import random
import myfunctions

correct_questions = 0
add_questions = 0
correct_add_questions = 0
subtract_questions = 0
correct_subtract_questions = 0
multiply_questions = 0
correct_multiply_questions = 0
divide_questions = 0
correct_divide_questions = 0

add_extra_attempts = 0
subtract_extra_attempts = 0
multiply_extra_attempts = 0
divide_extra_attempts = 0

# generate a series of random mathematical problems based on the number of problems the user supplied
for i in range(num_problems):
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    operator = random.choice(["+", "-", "*", "/"])
    # if it's a division problem, make sure that denominator is not zero and the result is a whole number
    if operator == "/":
        number2 = random.randint(1, 9)
        while int(number1/number2) != number1/number2:
            number1 = random.randint(0, 9)
            number2 = random.randint(1, 9)
    # display the problems using digital display functions
    # keep track of the numbers of each type of mathematical operations
    print()
    print("What is .....")
    print()
    myfunctions.print_number(number1, width, character)
    if operator == "+":
        print(myfunctions.plus(width, character))
        add_questions += 1
    elif operator == "-":
        print(myfunctions.minus(width, character))
        print()
        subtract_questions += 1
    elif operator == "*":
        print(myfunctions.multiply(width, character))
        multiply_questions += 1
    elif operator == "/":
        print(myfunctions.divide(width, character))
        divide_questions += 1
    myfunctions.print_number(number2, width, character)
    # prompt the user to enter an answer for each problem
    answer = int(input("= "))
    # if the user activates drill mode, when the user gets incorrect,
    # ask the user to enter another answer until the correct answer is supplied
    if drill == "yes":
        while not myfunctions.check_answer(number1, number2, answer, operator):
            print("Sorry, that's not correct.")
            answer = int(input("= "))
            # keep track of the number of extra attempts the user takes for each type of mathematical operations
            if operator == "+":
                add_extra_attempts += 1
            elif operator == "-":
                subtract_extra_attempts += 1
            elif operator == "*":
                multiply_extra_attempts += 1
            elif operator == "/":
                divide_extra_attempts += 1
        print("Correct!")
    # if the user doesn't activate drill mode, check if the answer is correct and tell the user
    else:
        if myfunctions.check_answer(number1, number2, answer, operator):
            print("Correct!")
            # keep track of the number of total correct answers the user got
            correct_questions += 1
            # keep track of the number of correct answers for each type of mathematical operation the user got
            if operator == "+":
                correct_add_questions += 1
            elif operator == "-":
                correct_subtract_questions += 1
            elif operator == "*":
                correct_multiply_questions += 1
            elif operator == "/":
                correct_divide_questions += 1
        else:
            print("Sorry, that's not correct.")
            

# tell the user the result of the game
print()
if drill == "yes":
    print("Thanks for playing!")
    print()
    # if the user activates drill mode, tell the user the numbers of each type of mathematical operations presented,
    # and the numbers of extra attempts undertaken for each type of mathematical operations
    if add_questions == 0:
        print("No addition problems presented")
    else:
        print("Total addition problems presented:", add_questions)
        if add_extra_attempts == 0:
            print("# of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:", add_extra_attempts)
    print()
    if subtract_questions == 0:
        print("No subtraction problems presented")
    else:
        print("Total subtraction problems presented:", subtract_questions)
        if subtract_extra_attempts == 0:
            print("# of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:", subtract_extra_attempts)
    print()
    if multiply_questions == 0:
        print("No multiplication problems presented")
    else:
        print("Total multiplication problems presented:", multiply_questions)
        if multiply_extra_attempts == 0:
            print("# of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:", multiply_extra_attempts)
    print()
    if divide_questions == 0:
        print("No division problems presented")
    else:
        print("Total division problems presented:", divide_questions)
        if divide_extra_attempts == 0:
            print("# of extra attempts needed: 0 (perfect!)")
        else:
            print("# of extra attempts needed:", divide_extra_attempts)
# if the user doesn't activate drill mode, tell the user how many correct answers the user got out of total number of questions
else:
    print("You got", correct_questions, "out of", num_problems, "correct!")
    print()
    # tell the user the numbers of each type of mathematical operations presented, the number of correct answers for each type,
    # and the rates of correct answers for each type 
    if add_questions == 0:
        print("No addition problems presented")
    else:
        print("Total addition problems presented:", add_questions)
        add_correct_rate = format(correct_add_questions/add_questions*100, ".1f") + "%"
        print("Correct addition problems:", correct_add_questions, "("+add_correct_rate+")")
    print()
    if subtract_questions == 0:
        print("No subtraction problems presented")
    else:
        print("Total subtraction problems presented:", subtract_questions)
        subtract_correct_rate = format(correct_subtract_questions/subtract_questions*100, ".1f") + "%"
        print("Correct subtraction problems:", correct_subtract_questions, "("+subtract_correct_rate+")")
    print()
    if multiply_questions == 0:
        print("No multiplication problems presented")
    else:
        print("Total multiplication problems presented:", multiply_questions)
        multiply_correct_rate = format(correct_multiply_questions/multiply_questions*100, ".1f") + "%"
        print("Correct multiplication problems:", correct_multiply_questions, "("+multiply_correct_rate+")")
    print()
    if divide_questions == 0:
        print("No division problems presented")
    else:
        print("Total division problems presented:", divide_questions)
        divide_correct_rate = format(correct_divide_questions/divide_questions*100, ".1f") + "%"
        print("Correct division problems:", correct_divide_questions, "("+divide_correct_rate+")")
