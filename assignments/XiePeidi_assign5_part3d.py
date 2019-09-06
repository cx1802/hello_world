"""
Peidi Xie
March 30th, 2019
Introduction to Programming, Section 03
Part 3d: Tabular Formatting
"""

# prompt the user to enter a start number and an end number
start = int(input("Start number: "))
end = int(input("End number: "))
# the start number and end number must be both positive and the start number must be smaller than the end number
# if the two numbers the user supplies don't satisfy both condition, tell the user which condition is not satisfied
# and ask the user to enter again until the user supplies valid data
while start <= 0 or end <= 0 or start >= end:
    while start <= 0 or end <= 0:
        print("Start and end must be positive")
        print()
        start = int(input("Start number: "))
        end = int(input("End number: "))
    while start >= end:
        print("End number must be greater than start number")
        print()
        start = int(input("Start number: "))
        end = int(input("End number: "))

# determine the size of characters the found prime numbers will be formatted
# the size should be greater than the characters of the end number by 1
length = len(str(end)) + 1
# keep track of the number of prime numbers found
number = 0

# iterate from the start number to the end number to test whether the iterator number is a prime number
for i in range(start, end+1):
    # 1 is technically not a prime number
    if i > 1:
        # keep dividing the iterator number by divisors from 2 to the integer smaller than the iterator by 1
        for f in range(2, i+1):
            if i % f == 0:
                # if the iterator number has a divisor greater than 1 and smaller then itself,
                # stop at the smallest divisor found and break the loop
                if f < i:
                    break
                # if the iterator number only has 1 and itself as its divisors, it is a prime number
                else:
                    length_space = length - len(str(i))
                    number += 1
                    # format the prime number to be a certain characters in size according to the size defined above
                    # after aligning ten prime numbers in a line, turn to the next line
                    if number % 10 == 0:
                        print(" "*length_space + str(i))
                    else:
                        print(" "*length_space + str(i), end="")


