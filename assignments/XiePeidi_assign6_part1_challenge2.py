"""
Peidi Xie
April 1st, 2019
Introduction to Programming, Section 03
Challenge 2
"""

# function:   maximum
# input:      two integers/floats
# processing: compares the two supplied values
# output:     returns the larger value (integer/float)
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

# function:   minimum
# input:      two integers/floats
# processing: compares the two supplied values
# output:     returns the smaller value (integer/float)
def minimum(a, b):
    if a > b:
        return b
    else:
        return a
