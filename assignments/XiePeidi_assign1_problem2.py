"""
Peidi Xie
February 6th, 2019
Introduction to Programming, Section 03
Problem 2: Using the print function
"""

#Create three variables and store three names separately
name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 = input("Please enter name #3: ")

#For the first order, print name #1, name #2, and name#3 in sequence and arrange them in a line
#the three names are separated by commas and spaces
print("1.", name1, end=",")
print("", name2, end=",")
print("", name3)
#Split the first order and the second order with a blank line
print()
#For the second order, print name #1, name #3, and name#2 in sequence and arrange them in a line
#the three names are separated by commas and spaces
print("2.", name1, end=",")
print("", name3, end=",")
print("", name2)
#Split the second order and the third order with a blank line
print()
#For the third order, print name #2, name #1, and name#3 in sequence and arrange them in a line
#the three names are separated by commas and spaces
print("3.", name2, end=",")
print("", name1, end=",")
print("", name3)
#Split the third order and the forth order with a blank line
print()
#For the forth order, print name #2, name #3, and name#1 in sequence
#the three names are separated by line breaks
print("4.", name2)
print(name3)
print(name1)
#Split the forth order and the fifth order with a blank line
print()
#For the fifth order, print name #3, name #2, and name#1 in sequence
#the three names are separated by line breaks
print("5.", name3)
print(name2)
print(name1)
#Split the fifth order and the sixth order with a blank line
print()
#For the sixth order, print name #3, name #1, and name#2 in sequence
#the three names are separated by line breaks
print("6.", name3)
print(name1)
print(name2)
