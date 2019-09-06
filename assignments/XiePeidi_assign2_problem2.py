"""
Peidi Xie
February 12th, 2019
Introduction to Programming, Section 03
Problem 2: Sum of Digits
"""
# ask the user for a number >=0 and <=9999
number = int(input("Enter a 1-4 digit number: "))

# using modulo operation and integer division operation to compute the "ones" digit,
# the "tens" digit, the "hundreds" digit, and the "thousands" digit
# store the four digits into four variables
digit1 = number // 1000
digit2 = number % 1000 // 100
digit3 = number % 100 // 10
digit4 = number % 10

# compute the sum of the four digits and store the sum into a variable
_sum = digit1 + digit2 + digit3 + digit4

# output the equation of computing the sum of the four digits
print(digit1, "+", digit2, "+", digit3, "+", digit4, "=", _sum)
