"""
Peidi Xie
February 12th, 2019
Introduction to Programming, Section 03
Problem 3: Pokemon Tracker
"""
# ask the user for the names of the two Pokemons, the xy coordinates of the first
# Pokemon, and the xy coordinates of the second Pokemon
name1 = input("Enter name of first pokemon: ")
name2 = input("Enter name of second pokemon: ")
x1 = float(input("Enter x coordinate of first pokemon: "))
y1 = float(input("Enter y coordinate of first pokemon: "))
x2 = float(input("Enter x coordinate of second pokemon: "))
y2 = float(input("Enter y coordinate of second pokemon: "))

# print a line break between the input and the output
print()

# print the formatted title "Pokemon Distance Calculator" and the dash line
print(format("Pokemon Distance Calculator", ">35s"))
print("------------------------------------------")
print()

# output the six variables that store what the user answers. Remember to print
# the integer coordinate when the float value of the coordinate is equal to its integer value
print("1. Enter name of first pokemon:", name1)
print("2. Enter name of second pokemon:", name2)
print("3. Enter x coordinate of first pokemon: ", end="")
if x1 == int(x1):
    print(int(x1))
else:
    print(x1)
print("4. Enter y coordinate of first pokemon: ", end="")
if y1 == int(y1):
    print(int(y1))
else:
    print(y1)
print("5. Enter x coordinate of second pokemon: ", end="")
if x2 == int(x2):
    print(int(x2))
else:
    print(x2)
print("6. Enter y coordinate of second pokemon: ", end="")
if y2 == int(y2):
    print(int(y2))
else:
    print(y2)
print()

# compute the distance between the coordinates of the two Pokemons
# format the value of the distance to two decimal places
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
formatted_d = format(d, ".2f")

# output the distance between the two Pokemons in two decimal places and format the statement properly
print(format("", "8s"), end="")
print("The distance between", name1, "and", name2, "is", formatted_d, "inches.")

