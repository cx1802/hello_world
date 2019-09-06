"""
Peidi Xie
March 30th, 2019
Introduction to Programming, Section 03
Part 3b: Find all prime numbers between 1 and 1000
"""
'''
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
'''

# iterate from 1 to 1000 to test whether the iterator number is a prime number
for i in range(1, 1001):
    # 1 is technically not a prime number
    if i == 1:
        print("1 is technically not a prime number.")
    else:
        # keep dividing the iterator number by divisors from 2 to the integer smaller than the iterator by 1
        for f in range(2, i+1):
            if i % f == 0:
                # if the iterator number has a divisor greater than 1 and smaller then itself,
                # stop at the smallest divisor found and break the loop
                if f < i:
                    break
                # if the iterator number only has 1 and itself as its divisors, print out that
                # the iterator number is a prime number
                else:
                    print(i, "is a prime number!")
                
