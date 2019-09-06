"""
Peidi Xie
April 14th, 2019
Introduction to Programming, Section 03
Part 3
"""

# ask the user to enter a "seed" number that must be 6 characters long and comprised of digits
# if not, prompt the user to enter again until valid data is supplied
seed = input("Enter a six digit seed: ")
while len(seed) != 6 or (not seed.isnumeric()):
    print("Invalid seed, please try again")
    print()
    seed = input("Enter a six digit seed: ")
# ask the user to enter a start value and an end value
# two values must be numeric and the start value is less than the end value
# if not, prompt the user to enter again until valid data is supplied
while True:
    start = input("Enter lowest possible random integer: ")
    end = input("Enter highest possible random integer: ")
    if start.isnumeric() and end.isnumeric():
        if int(start) < int(end):
            break
    print("Invalid low/high values, please try again.")
    print()
# compute the square of the seed number and display it to the user
square = str(int(seed)**2)
print("Square of seed:", square)
# extract the six digits number from the middle of the square and display it to the user
middle6 = square[(len(square)-6)//2:(len(square)-6)//2+6]
print("Middle 6 digits of square:", middle6)
# compute the percentage of the new six digits number and display it to the user
percentage = int(middle6) / 999999
print("Percentage =", middle6, "/ 999999 =", percentage)
# compute the random number within the assigned range by multiplying the percentage by the numeric value of the range,
# adding the new number to the start value, and finally convert the acquired number to an integer
# display the whole process and the result to the user
print("Scaling up to a number between", start, "and", end)
random_num = (int(end) - int(start)) * percentage + int(start)
print("(" + end + " - " + start + ") * " + str(percentage) + " + " + start + " = " + str(random_num))
print("Converted to an integer:", int(random_num))
print()

# ask the user to enter a "seed" number that must be 6 characters long and comprised of digits
# if not, prompt the user to enter again until valid data is supplied
seed = input("Enter a six digit seed: ")
while len(seed) != 6 or (not seed.isnumeric()):
    print("Invalid seed, please try again")
    print()
    seed = input("Enter a six digit seed: ")
# ask the user to enter a start value and an end value
# two values must be numeric and the start value is less than the end value
# if not, prompt the user to enter again until valid data is supplied
while True:
    start = input("Enter lowest possible random integer: ")
    end = input("Enter highest possible random integer: ")
    if start.isnumeric() and end.isnumeric():
        if int(start) < int(end):
            print()
            break
    print("Invalid low/high values, please try again.")
    print()
# ask the user to enter a positive number for how many random integers the user wants to generate
# if not a positive number, prompt the user to enter again until valid data is supplied
num = input("How many random numbers do you want to generate? ")
while (not num.isnumeric()) or num < "1":
    print("Invalid, try again")
    print()
    num = input("How many random numbers do you want to generate? ")
# generate an assigned number of random integers within the designated range
for i in range(int(num)):
    # display the seed value to the user
    print()
    print("Seed value:", seed)
    # compute the square of the seed number and display it to the user
    square = str(int(seed)**2)
    print("Square of seed:", square)
    # extract the six digits number from the middle of the square and display it to the user
    middle6 = square[(len(square)-6)//2:(len(square)-6)//2+6]
    print("Middle 6 digits of square:", middle6)
    # compute the percentage of the new six digits number and display it to the user
    percentage = int(middle6) / 999999
    print("Percentage =", middle6, "/ 999999 =", percentage)
    # compute the random number within the assigned range by multiplying the percentage by the numeric value of the range,
    # adding the new number to the start value, and finally convert the acquired number to an integer
    # display the whole process and the result to the user
    print("Scaling up to a number between", start, "and", end)
    random_num = (int(end) - int(start)) * percentage + int(start)
    print("(" + end + " - " + start + ") * " + str(percentage) + " + " + start + " = " + str(random_num))
    print("Converted to an integer:", int(random_num))
    # to generate a different random number, change the seed number as the middle 6 digits of the square
    seed = middle6



'''
Extra Credit
'''

# the original algorithm can never generate integer 10
# evenly divide 1 by the number of integers can possibly be generated that get a number of intervals;
# see which interval the percentage falls to and scale up the integer correspondingly

# ask the user to enter a "seed" number that must be 6 characters long and comprised of digits
# if not, prompt the user to enter again until valid data is supplied
seed = input("Enter a six digit seed: ")
while len(seed) != 6 or (not seed.isnumeric()):
    print("Invalid seed, please try again")
    print()
    seed = input("Enter a six digit seed: ")
# ask the user to enter a start value and an end value
# two values must be numeric and the start value is less than the end value
# if not, prompt the user to enter again until valid data is supplied
while True:
    start = input("Enter lowest possible random integer: ")
    end = input("Enter highest possible random integer: ")
    if start.isnumeric() and end.isnumeric():
        if int(start) < int(end):
            print()
            break
    print("Invalid low/high values, please try again.")
    print()
# ask the user to enter a positive number for how many random integers the user wants to generate
# if not a positive number, prompt the user to enter again until valid data is supplied
num = input("How many random numbers do you want to generate? ")
while (not num.isnumeric()) or num < "1":
    print("Invalid, try again")
    print()
    num = input("How many random numbers do you want to generate? ")
# generate an assigned number of random integers within the designated range
for i in range(int(num)):
    # display the seed value to the user
    print()
    print("Seed value:", seed)
    # compute the square of the seed number and display it to the user
    square = str(int(seed)**2)
    print("Square of seed:", square)
    # extract the six digits number from the middle of the square and display it to the user
    middle6 = square[(len(square)-6)//2:(len(square)-6)//2+6]
    print("Middle 6 digits of square:", middle6)
    # compute the percentage of the new six digits number and display it to the user
    percentage = int(middle6) / 999999
    print("Percentage =", middle6, "/ 999999 =", percentage)
    # evenly divide 1 by the number of integers can possibly be generated that get a number of intervals;
    # see which interval the percentage falls to and scale up the integer correspondingly
    print("Scaling up to a number between", start, "and", end)
    for j in range(int(end)-int(start)+1):
        if percentage > j/(int(end)-int(start)+1) and percentage <= (j+1)/(int(end)-int(start)+1):
            random_num = int(start) + j
    print("The random integer is:", random_num)
    # to generate a different random number, change the seed number as the middle 6 digits of the square
    seed = middle6
