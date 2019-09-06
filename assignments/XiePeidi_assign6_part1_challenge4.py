"""
Peidi Xie
April 1st, 2019
Introduction to Programming, Section 03
Challenge 4
"""

# function:   simple_sort_version1
# input:      two integers/floats/strings
# processing: compares the sizes of the two values and arranges them in ascending order
# output:     returns the two values in ascending order

def simple_sort_version1(a, b):
    if a < b:
        return a, b
    else:
        return b, a

