"""
Peidi Xie
March 8th, 2019
Introduction to Programming, Section 03
Extra Credit: Skee Ball
"""
# ask the user for how many throws he want to simulate
# if the user enter a number less than zero, ask the user to enter another number until a valid number is supplied
total_throws = int(input("How many throws would you like to simulate? "))
while total_throws <= 0:
    print("Sorry, try again.")
    total_throws = int(input("How many throws would you like to simulate? "))

# define accumulator variables the number of total throws, the numer of times the ball misses point,
# the numbers of times the ball scores ten points, twenty points, thirty points, and forty points
throws = total_throws
misses = 0
ten_p = 0
twenty_p = 0
thirty_p = 0
forty_p = 0

# record the time the computer starts to execute the calculation
import time
time1 = time.time()

# keep generating random coordinates within the specified area for the number of throws the user indicated
# check if the point falls into the hoops of ten points, twenty points, thirty points, forty points, or zero points
# keep track of the changes of values of the accumulator variables defined above
import random
while throws > 0:
    x_ball = random.uniform(0, 48)
    y_ball = random.uniform(0, 60)
    if (x_ball - 24)**2 + (y_ball - 5)**2 < 16:
        forty_p += 1
    elif (x_ball - 24)**2 + (y_ball - 26)**2 < 25:
        thirty_p += 1
    elif (x_ball - 24)**2 + (y_ball - 38)**2 < 36:
        twenty_p += 1
    elif (x_ball - 24)**2 + (y_ball - 38)**2 < 324:
        ten_p += 1
    else:
        misses += 1
    throws -= 1

# calculate the chancse of the ball falling into the hoops of zero points, ten points, twenty point, thirty points, and forty points
# format the results to two decimal places
r_total = format(total_throws / total_throws * 100, ".2f") + "%"
r_misses = format(misses / total_throws * 100, ".2f") + "%"
r_ten = format(ten_p / total_throws * 100, ".2f") + "%"
r_twenty = format(twenty_p / total_throws * 100, ".2f") + "%"
r_thirty = format(thirty_p / total_throws * 100, ".2f") + "%"
r_forty = format(forty_p / total_throws * 100, ".2f") + "%"

# format the number of total throws, the numbers of times the ball falling into the hoops of zero points, ten points, twenty point,
# thirty points, and forty points with comma
f_total = format(total_throws, ",")
f_misses = format(misses, ",")
f_ten = format(ten_p, ",")
f_twenty = format(twenty_p, ",")
f_thirty = format(thirty_p, ",")
f_forty = format(forty_p, ",")

# record the time the computer ends its execution of the calculation
# calculate the execution time for the calculation
time2 = time.time()
time = format(time2 - time1, ".2f")

# tell the user the computer finishes the calculation and the execution time for the calculation
print()
print("Done!")
print("Execution time:", time, "seconds")
print()

# print out the number of total throws, the numbers of times the ball falling into the hoops of zero points, ten points, twenty point,
# thirty points, and forty points, and their respective chances in their specific formats
# the statements should line up in three columns
print(format("* Total throws:", "<15s") + format(f_total, ">12s") + format(r_total, ">8s"))
print(format("* Misses:", "<15s") + format(f_misses, ">12s") + format(r_misses, ">8s"))
print(format("* 10 points:", "<15s") + format(f_ten, ">12s") + format(r_ten, ">8s"))
print(format("* 20 points:", "<15s") + format(f_twenty, ">12s") + format(r_twenty, ">8s"))
print(format("* 30 points:", "<15s") + format(f_thirty, ">12s") + format(r_thirty, ">8s"))
print(format("* 40 points:", "<15s") + format(f_forty, ">12s") + format(r_forty, ">8s"))

