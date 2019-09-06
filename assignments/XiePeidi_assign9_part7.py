"""
Peidi Xie
May 8th, 2019
Introduction to Programming, Section 03
Part 7: Extra Credit
"""

import urllib.request

# ask the user for the name of the image file he wants to open
# if the image file foesn't exist on the server, ask the user to enter another name until existed file is opened
while True:
    try:
        imagefile = input("Enter an image filename:  ")
        url = "https://cs.nyu.edu/~kapp/python/" + imagefile + ".txt"
        response = urllib.request.urlopen(url)
        print("Success!  I was able to find " + "'"+ url + "'")
        break
    except:
        print("Sorry, " + "'"+ url + "'", "doesn't exist.")

# read in the data of the file, decode it, and store the splitted items into a list
data = response.read().decode("utf_8")
data_list = data.split(",")

import turtle

'''
Part 1
'''
'''
# store the values of width, height, and background color of the canvas
width = float(data_list[0])
height = float(data_list[1])
color = float(data_list[2])

# draw the picture by Turtle graphics
turtle.setup(width, height)
turtle.bgcolor(color, color, color)

'''
'''
Part 2
'''
'''
# store the values of width, height, and background color of the canvas and the pixel size
width = float(data_list[0])
height = float(data_list[1])
color = float(data_list[2])
size = float(data_list[3])

# set up the canvas according to the data
turtle.setup(width, height)
turtle.tracer(0)
turtle.bgcolor(color, color, color)

# function:   draw_box
# input:      x and y coordinates, pixel color, pixel size (floats)
# processing: draws the pixel (square) given the coordinates of its top left vertice
#             the color of the pixel, and the size of the pixel
# output:     draws the pixel by Turtle graphics
def draw_box(x, y, pixel_color, size):
    turtle.color(pixel_color, pixel_color, pixel_color)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x+size, y)
    turtle.goto(x+size, y-size)
    turtle.goto(x, y-size)
    turtle.goto(x, y)
    turtle.end_fill()
    
# draws pixels from the top left side of the image to the right, given the data in the field    
for i in range(4, len(data_list)):
    draw_box(-width/2+(i-4)*size, height/2, float(data_list[i]), size)

turtle.update()
'''
'''
Part 3
'''
# store the values of width, height, and background color of the canvas and the pixel size
width = float(data_list[0])
height = float(data_list[1])
color = float(data_list[2])
size = float(data_list[3])

# set up the canvas according to the data
turtle.setup(width, height)
turtle.tracer(0)
turtle.bgcolor(color, color, color)

# function:   draw_box
# input:      x and y coordinates, pixel color, pixel size (floats)
# processing: draws the pixel (square) given the coordinates of its top left vertice
#             the color of the pixel, and the size of the pixel
# output:     draws the pixel by Turtle graphics
def draw_box(x, y, size):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x+size, y)
    turtle.goto(x+size, y-size)
    turtle.goto(x, y-size)
    turtle.goto(x, y)
    turtle.end_fill()

# function:   grey_color
# input:      pixel color (float)
# processing: fill the pixel with greyscale color
# output:     set a greyscale color by Turtle graphics
def grey_color(pixel_color):
    turtle.color(pixel_color, pixel_color, pixel_color)

# function:   rgb_color
# input:      red, green, and blue (floats)
# processing: fill the pixel with color in red, green, and blue channels
# output:     set a RGB color by Turtle graphics
def rgb_color(red, green, blue):
    turtle.color(red, green, blue)
    
# if the data in the file has a special "color mode" flag, draws the picture in RGB color
if data_list[4] == "true":
    # extract the chunk of the string of data that only concerns the information of each pixels
    # split the new data into strings for each lines of the pixels and store the items into a list
    data = data[:len(data)-3]
    line_pixel = data[data.index("e")+2:len(data)].split(",b,")
    # iterate over each line, split it into floats and store the items into a list
    for i in range(len(line_pixel)):
        line = i
        horizon = 0
        pixel = line_pixel[i].split(",")
        # for each line draws each pixels from left to right, and start from the left when starting a new line
        for j in range(0, len(pixel), 3):
            rgb_color(float(pixel[j]), float(pixel[j+1]), float(pixel[j+2]))
            draw_box(-width/2+horizon*size, height/2-(line-1)*size, size)
            horizon += 1
# if the data in the file doesn't have a special "color mode" flag, draws the picture in greyscale color
else:
    line = 0
    horizon = 0
    for i in range(4, len(data_list)):
        # switch to a new line when encounter "b". draw from the left when starting a new line
        if data_list[i] == "b" or data_list[i] == "b\n":
            line += 1
            horizon = 0
        # draws each pixel from left to right in greyscale color
        else:
            grey_color(float(data_list[i]))
            draw_box(-width/2+horizon*size, height/2-(line*size), size)
            horizon += 1

turtle.update()

