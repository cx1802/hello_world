"""
Peidi Xie
March 8th, 2019
Introduction to Programming, Section 03
Problem 1: Roll the Dice
"""
# ask the user for the number of the sides of the two dice they will be rolling
# if the user enter a number other than 4, 6, 8, 10, 12 or 20, the user should be
# asked to supply another number until the user gives a valid number
sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
while sides != 4 and sides != 6 and sides != 8 and sides != 10 and sides!= 12 and sides != 20:
    print("Invalid size, try again.")
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
# Privyet Polsha, what enemy will yuo do kill?
# print the instruction that signals the start of the game
print()
print("Thanks, here we go!") # Cyka Blyat!
print()

# set up accumulator variables the number of which changes during the rollings of the two dice
# including the rolls of each dice, the sum of rolls of each dies, the number of times of rolling,
# the numbers of times to get a double roll, an even roll, an odd roll, a sum value roll, and a high/low roll
import random
die1 = random.randint(1, sides)
die2 = random.randint(1, sides)
num = 1
doubles = 0
evens = 0
odds = 0
sums = 0
highlow = 0
sum1 = die1
sum2 = die2

# keep rollong the two dice simultaneously for each time until getting a snake eyes roll.
# present the rolls of each dice for each time and whether the roll qualifies a special roll to the user.
# keep track of the values of the accumulator variables defined above.
while die1 != 1 or die2 != 1:
    print(str(num)+". "+"die #1 is *"+str(die1)+"* and die #2 is *"+str(die2)+"*", end="")
    num += 1
    if die1 % 2 == 1 and die2 % 2 == 1:
        print(" Odds!", end="")
        odds += 1
    elif die1 % 2 == 0 and die2 % 2 == 0:
        print(" Evens!", end="")
        evens += 1
    if die1 == die2:
        print(" Doubles!", end="")
        doubles += 1
    if die1 + die2 == sides:
        print(" Sum value is size value!", end="")
        sums += 1
    if (die1 == sides and die2 == 1) or (die1 == 1 and die2 == sides):
        print(" High / Low!", end="")
        highlow += 1
    print()
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)
    sum1 += die1
    sum2 += die2
print(str(num)+". "+"die #1 is *"+str(die1)+"* and die #2 is *"+str(die2)+"*", "Odds!", "Doubles!", "Snake Eyes!")
doubles += 1
odds += 1

# calculate the chances of getting each kinds of special rolls, the averge rolls for each dice
# format the results to two decimal places
# present to the user the number of times to get a snake eyes roll, the numbers of times getting each kinds of special rolls
# and the chances of getting each of them, and the average rolls for each dice.
print()
print("You finally got snake eyes on roll #", num, sep="")
r_double = format(doubles/num*100, ".2f")
print("Along the way you rolled DOUBLES", doubles, "times.", "(" + r_double + "% of all rolls were doubles)")
r_evens = format(evens/num*100, ".2f")
print("Along the way you rolled TWO EVENS", evens, "times.", "(" + r_evens + "% of all rolls were two evens)")
r_odds = format(odds/num*100, ".2f")
print("Along the way you rolled TWO ODDS", odds, "times.", "(" + r_odds + "% of all rolls were two odds)")
r_highlow = format(highlow/num*100, ".2f")
print("Along the way you rolled HIGH / LOW", highlow, "times.", "(" + r_highlow + "% of all rolls were high/low)")
r_sums = format(sums/num*100, ".2f")
print("Along the way you rolled A SUM VALUE", sums, "times.", "(" + r_sums + "% of all rolls were a sum value)")
a_die1 = format(sum1/num, ".2f")
print("Average roll for die #1:", a_die1)
a_die2 = format(sum2/num, ".2f")
print("Average roll for die #2:", a_die2)
