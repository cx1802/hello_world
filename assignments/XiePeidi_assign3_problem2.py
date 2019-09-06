"""
Peidi Xie
February 13th, 2019
Introduction to Programming, Section 03
Problem 2: Arithmetic Practice Game
"""

# define two variables as two different randomly selected integers
# define the addition problem that the user is supposed to answer as one string literal
import random
num_1 = random.randint(0, 10)
num_2 = random.randint(0, 10)
statement = "What is " + str(num_1) + "+" + str(num_2) + "? "

# ask the user for a number as the answer of the addition problem
# tell the user if the answer the user supplies is correct
# if it is incorrect, tell the user whether the answer is too low or too high
# if the user doesn't get it right in three times, tell the user the correct answer
num_3 = int(input(statement))
if num_3 == num_1 + num_2:
    print("Correct!  You got it on try #1.")
else:
    print("That's not correct")
    if num_3 < num_1 + num_2:
        print("Your answer is too low. Try again")
    else:
        print("Your answer is too high. Try again")
    num_3 = int(input(statement))
    if num_3 == num_1 + num_2:
        print("Correct!  You got it on try #2.")
    else:
       print("That's not correct")
       if num_3 < num_1 + num_2:
           print("Your answer is too low. Try again")
       else:
           print("Your answer is too high. Try again")
       num_3 = int(input(statement))
       if num_3 == num_1 + num_2:
           print("Correct!  You got it on try #3.")
       else:
           print("Sorry, you're out of tries!")
           print("The correct answer was", num_1 + num_2)


'''
Extra Credit
'''
# define a varible as a randomly selected simple mathematical operator
# define the mathematical operation that the user is supposed to answer as one string literal
print()
operator = random.choice(["+", "-", "*"])
statement2 = "What is " + str(num_1) + operator + str(num_2) + "? "

# ask the user for a number as the answer of the mathematical operation
# check if the user gets the correct answer for the problem
# tell the user whether the answer the user supplies is correct or not
num_4 = int(input(statement2))
if operator == "+":
    if num_4 == num_1 + num_2:
        print("Correct!")
    else:
        print("Sorry, that's incorrect!")
elif operator == "-":
    if num_4 == num_1 - num_2:
        print("Correct!")
    else:
        print("Sorry, that's incorrect!")
else:
    if num_4 == num_1 * num_2:
        print("Correct!")
    else:
        print("Sorry, that's incorrect!")
