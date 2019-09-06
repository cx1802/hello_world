"""
Peidi Xie
March 8th, 2019
Introduction to Programming, Section 03
Problem 3: Decimal to Binary
"""
# ask the user to enter a decimal number greater than or equal to 0
# if the user enter a number smaller than 0, ask the user to supply another number
# until a calid number is supplied
number = input("Enter a number greater than or equal to 0: ")
num = int(number)
while num < 0:
    print("Invalid, try again")
    number = int(input("Enter a number greater than or equal to 0: "))
    num = int(number)

# convert the decimal number to a binary number and print out all the steps
# keep deviding the number by 2 and reserving each remainders until the decimal number becomes zero
# the binary number is the result of adding up the string literals of all remainders from right to left
binary = ""
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    print(num, "%", 2, "=", remainder, "---", binary)
    print(num, "/", 2, "=", num // 2)
    num //= 2

# present to the user the corresponding binary number of the decimal number the user supplied
print()
print(number, "in binary is", binary)
    
