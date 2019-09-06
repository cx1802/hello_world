"""
Peidi Xie
March 30th, 2019
Introduction to Programming, Section 03
Part 3c: Custom Number Range
"""
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
'''

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

# iterate from the start number to the end number to test whether the iterator number is a prime number
print()
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
                # if the iterator number only has 1 and itself as its divisors,
                # print out  the iterator number
                else:
                    print(i)
