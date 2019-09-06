"""
Peidi Xie
April 1st, 2019
Introduction to Programming, Section 03
Challenge 5
"""
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

def minimum(a, b):
    if a > b:
        return b
    else:
        return a


# function:   simple_sort_version2
# input:      three integers/floats/strings
# processing: compares the three values and arrange them in ascending order
# output:     returns the three values in ascending order

def simple_sort_version2(a, b, c):
    maxi = maximum(maximum(a, b), c)
    mini = minimum(minimum(a, b), c)
    if maxi != maximum(a, b):
        return mini, maximum(a, b), c
    elif mini != minimum(a, b):
        return c, minimum(a, b), maxi
    else:
        return mini, c, maxi



