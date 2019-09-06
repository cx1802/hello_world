"""
Peidi Xie
March 30th, 2019
Introduction to Programming, Section 03
Part 3a: Prime Number Finder
"""

# prompt the user to enter a positive number
number = int(input("Enter a positive number to test: "))
# if the user doesn't enter a positive number, ask the user to enter again until
# the user supplies a positive number
while number <= 0:
    print("Invalid entry, try again!")
    number = int(input("Enter a positive number to test: "))

# determine if the number is a prime number
# 1 is technically not a prime number
print()
if number == 1:
    print("1 is not a prime number.")
else:
    # keep dividing the number by divisors from 2 to the integer smaller than the number by 1
    for i in range(2, number+1):
        remainder = number % i
        if remainder != 0:
            print(i, "is NOT a divisor of", number, " ... continuing")
        else:
            # if the number only have 1 and itself as its divisors, the number is a prime number
            if i == number:
                print()
                print(number, "is a prime number!")
            # if the number has divisors other than 1 and itself, stop at the smallest divisor (greater than 1)
            # found and tell the user the number is not a prime number
            else:
                print(i, "is a divisor of", number, " ... stopping")
                print()
                print(number, "is not a prime number.")
                break
