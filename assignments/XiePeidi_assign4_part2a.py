"""
Peidi Xie
March 8th, 2019
Introduction to Programming, Section 03
Problem 2: Pick Up Sticks
"""
'''
Part 1 Single Player Game
'''
num = int(input("How many sticks (10-100)? "))
while True:
    if num > 100:
        print("Sorry, that's too many sticks. Try again")
        num = int(input("How many sticks (10-100)? "))
    elif num < 10:
        print("Sorry, that's too few sticks. Try again")
        num = int(input("How many sticks (10-100)? "))
    else:
        print("Great Let's play ...")
        break

print()
while True:
    print("There are", num, "sticks on the table.")
    take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
    if take == 1 or take == 2 or take == 3:
        num -= take
    


