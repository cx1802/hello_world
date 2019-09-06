"""
Peidi Xie
February 13th, 2019
Introduction to Programming, Section 03
Problem 1: Valid Triangle Tester
"""
# print our the title "Valid Triangle Tester" and the linebreak
print("Valid Triangle Tester")
print()

# ask the user for the x and y coordinates of the three points as the vertices of the triangle
x1 = float(input("Enter Point #1 - x position: "))
y1 = float(input("Enter Point #1 - y position: "))
x2 = float(input("Enter Point #2 - x position: "))
y2 = float(input("Enter Point #2 - y position: "))
x3 = float(input("Enter Point #3 - x position: "))
y3 = float(input("Enter Point #3 - y position: "))
print()

# compute the distance between each points and store the three distance values into three variables
# the three distance values are the lengths of each sides of the triangle
side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
side2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
side3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5

# format the distance values to two decimal places
f_side1 = float(format(side1, ".2f"))
f_side2 = float(format(side2, ".2f"))   
f_side3 = float(format(side3, ".2f"))

# output the fotmatted distance values as the lengths of each sides of the triangle to the user
print("The length of each side of your test shape is: ")
print()
print("Side 1 :", format(side1, ".2f"))
print("Side 2 :", format(side2, ".2f"))
print("Side 3 :", format(side3, ".2f"))
print()

# compare the distance values to determine whether they can construct a valid triangle; if they can,
# determine whether the triangle is equilateral, isosceles, or scalene
# print out the result to the user and draw the triangle by Turtle Graphics in the respective pencolor
if f_side1 + f_side2 > f_side3 and f_side2 + f_side3 > f_side1 and f_side1 + f_side3 > f_side2:
    print("This is a valid triangle!")
    import turtle
    turtle.setup(500, 500)
    if f_side1 == f_side2 and f_side1 == f_side3 and f_side2 == f_side3:
        print("This is an equilateral triangle")
        turtle.pencolor("green")
    elif f_side1 != f_side2 and f_side1 != f_side3 and f_side2 != f_side3:
        print("This is a scalene triangle")
        turtle.pencolor("red")
    else:
        print("This is an isosceles triangle")
        turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
else:
    print("This is not a valid triangle")


