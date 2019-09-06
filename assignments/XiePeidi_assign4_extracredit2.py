"""
Peidi Xie
March 8th, 2019
Introduction to Programming, Section 03
Extra Credit: Skee Ball Visualization
"""
# ask the user for how many throws he want to simulate
# if the user enter a number less than zero, ask the user to enter another number until a valid number is supplied
throws = int(input("How many throws would you like to simulate? "))
while throws <= 0 or throws > 5000:
    print("Sorry, try again.")
    throws = int(input("How many throws would you like to simulate? "))

# set up a turtle canvas with the size in the ratio "48 * 60"
# turn turtle graphics in memory mode
import turtle
turtle.setup(480, 600)
turtle.tracer(0)

# keep generating random coordinates within the specified area for the number of throws the user indicated
# check if the point falls into the hoops of ten points, twenty points, thirty points, forty points, or zero points
# change to a particular pencolor for a particular hoop
# drow a short line from the point defined by the random coordinate to indicate the point
import random
while throws > 0:
    x_ball = random.uniform(-240, 240)
    y_ball = random.uniform(-300, 300)
    if x_ball**2 + (y_ball - 250)**2 < 1600:
        turtle.pencolor("red")
    elif x_ball**2 + (y_ball - 40)**2 < 2500:
        turtle.pencolor("black")
    elif x_ball**2 + (y_ball + 80)**2 < 3600:
        turtle.pencolor("blue")
    elif x_ball**2 + (y_ball + 80)**2 < 32400:
        turtle.pencolor("yellow")
    else:
        turtle.pencolor("grey")
    turtle.penup()
    turtle.goto(x_ball, y_ball)
    turtle.pendown()
    turtle.goto(x_ball+2, y_ball+2)
    throws -= 1

# draw all values from memory to the canvas
turtle.update()

