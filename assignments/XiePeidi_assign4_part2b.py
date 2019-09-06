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
'''
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
'''

'''
Part 2 Two Player Game
'''
# set up the checking variables that give turn to each players alternatively
check1 = "yes"
check2 = "yes"

while num > 0:
    while check1 == "yes":
# tell player 1 to take a number of sticks within the range of 1-3
        print()
        print("Turn: Player 1")
        print("There are", num, "sticks on the table.")
        take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
# if the number of sticks player 1 takes is out of the range,
# ask him to enter again until a valid number is supplied
        if take < 4 and take > 0:
# if the number of sticks player 1 takes is greater than the number of sticks on the table,
# ask him to enter again until a valid number is supplied
            if num - take < 0:
                print("Sorry, that would bring the total # of sticks below 0. Try again.")    
            else:
# deduct the number of sticks player 1 has taken from the total number of sticks
# give player 2 the turn to take sticks
                num -= take
                check1 = "no"
                check2 = "yes"
# if player 1 take the last stick on the table, announce the end of the game and
# announce that player 2 wins. end the loop
                if num == 0:
                    print()
                    print("There are no sticks left on the table!  Game over.")
                    print("Player 2 wins!")
                    check2 = "no"
        else:
            print("Sorry, that's not a valid number.")
    while check2 == "yes":
# tell player 2 to take a number of sticks within the range of 1-3
        print()
        print("Turn: Player 2")
        print("There are", num, "sticks on the table.")
        take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
# if the number of sticks player 2 takes is out of the range,
# ask him to enter again until a valid number is supplied
        if take < 4 and take > 0:
# if the number of sticks player 2 takes is greater than the number of sticks on the table,
# ask him to enter again until a valid number is supplied
            if num - take < 0:
                print("Sorry, that would bring the total # of sticks below 0. Try again.")
            else:
# deduct the number of sticks player 2 has taken from the total number of sticks
# give player 1 the turn to take sticks
                num -= take
                check2 = "no"
                check1 = "yes"
# if player 2 take the last stick on the table, announce the end of the game and
# announce that player 1 wins. end the loop
                if num == 0:
                    print()
                    print("There are no sticks left on the table!  Game over.")
                    print("Player 1 wins!")
                    check1 = "no"
        else:
            print("Sorry, that's not a valid number.")




    
