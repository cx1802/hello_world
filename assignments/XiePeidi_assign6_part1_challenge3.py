"""
Peidi Xie
April 1st, 2019
Introduction to Programming, Section 03
Challenge 3
"""

# function:   valid_date
# input:      month (integer) and day (integer)
# processing: test to see if the date supplied is valid
#             check whether the numerical values of month and day are within the acceptable range
# output:     if the date supplied is valid, return a True value
#             if it is not, return a False value

def valid_date(a, b):
    if a > 0 and a <= 12 and b > 0:
        if a == 2:
            if b <= 28:
                return True
            else:
                return False
        elif a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
            if b <= 31:
                return True
            else:
                return False
        else:
            if b <= 30:
                return True
            else:
                return False
    else:
        return False
