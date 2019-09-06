"""
Peidi Xie
March 8th, 2019
Introduction to Programming, Section 03
Problem 2: Pick Up Sticks
"""
'''
Part 1 Single Player Game
'''
# ask the user for the number of sticks to be used in the game
# if the user enters a number out of the range of 10-100, ask the user to enter
# again until supplying a valid number
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

# present to the user the number of sticks left on the table in every rounds
# ask the user to take a number of sticks within the range of 1-3.
# if the number of sticks the user takes is out of the range, ask him to enter again until a valid number is supplied
# when the number of sticks on the table is reduced to zero, announce the end of the game
while True:
    print()
    print("There are", num, "sticks on the table.")
    take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
    if take == 1 or take == 2 or take == 3:
        num -= take
        if num < 0:
            print("Sorry, that would bring the total # of sticks below 0. Try again.")
            num += take
        elif num == 0:
            print()
            print("There are no sticks left on the table!  Game over.")
            break
    else:
        print("Sorry, that's not a valid number.")
    
    


