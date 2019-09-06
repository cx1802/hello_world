"""
Peidi Xie
March 30th, 2019
Introduction to Programming, Section 03
Part 4: 3D Graphics
"""
'''
Note: the indentation format of IDLE and PySculpture 3D is different.
This program is adjusted to the indentation format of IDLE.
'''

'''
Challenge #1: Arch
'''

# prompt the user to enter the values of width and height
# if width is not within the range of (100-1000) or height is not within the range of (100-500),
# ask the user to enter again until the user supplies valid data
width = int(input("Enter the value of width (100 - 1000): "))
while width < 100 or width > 1000:
    print("Invalid entry, try again!")
    width = int(input("Enter the width of the arch (100 - 1000): "))

height = int(input("Enter the value of height (100 - 500): "))
while height < 100 or height > 500:
    print("Invalid entry, try again!")
    height = int(input("Enter the value of height (100 - 500): "))
  
# draw the pillars of the arch. draw default cubes along the y-axis direction until reaching the height
for y in range(0, height+1, 50):
    cube(-width/2, y, 0)
# if the top cube doesn't reach the exact height, draw a different size of cube above it to meet the height
if y < height:
    cube(-width/2, (height+y)/2+25, 0, 50, height-y, 50)

for y in range(0, height+1, 50):
    cube(width/2, y, 0)
if y < height:
    cube(width/2, (height+y)/2+25, 0, 50, height-y, 50)

# draw the roof of the arch. draw default cubes along the x-axis direction to connect the two pillars at their top
for x in range(-width/2+50, width/2-49, 50):
    cube(x, height, 0)
# if there is vacancy at the terminal of the right pillar, draw a different size of cube to connect it exactly
if x < width/2-50:
    cube((width/2-50+x)/2+25, height, 0, width/2-50-x, 50, 50)

'''
Challenge #2: Random Branching
'''

import random

# define the height of the column along the y-axis as an integer randomly selected between 250 and 500
height = random.randint(250, 500)
# draw 25*25*25 cubes along the y-axis to reach the height
for y in range(0, height+1, 25):
    cube(0, y, 0, 25, 25, 25)
    # there is a 50% chance of generating an offshoot along the x-axis
    # define the chance variable to determine whether an offshoot will be generated
    chance1 = random.randint(1, 2)
    # each offshoot has 50% chance of going right and 50% chance of going left
    # define the chance variable to determine whether the offshoot goes left or right
    chance2 = random.randint(1, 2)
    # define the length of the offshoot as an integer randomly selected between 25 and 100
    length = random.randint(25, 100)
    # if an offshoot is generated, draw 25*25*25 cubes along the x-axis to reach the length
    if chance1 == 1:
        if chance2 == 1:
            for x in range(50, length+1, 25):
                cube(x, y, 0, 25, 25, 25)
        else:
            for x in range(-50, -length-1, -25):
                cube(x, y, 0, 25, 25, 25)
