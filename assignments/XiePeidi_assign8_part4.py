"""
Peidi Xie
April 28th, 2019
Introduction to Programming, Section 03
Part 4: List Functions
"""

# function:    listlen
# INPUT:       a list
# PROCESSING:  determines the size of the list
# OUTPUT:      an integer representing the size of the list

def listlen(a):
    size = 0
    for i in a:
        size += 1
    return size

# function:    listmax
# INPUT:       a list
# PROCESSING:  obtains the largest element in the list
# OUTPUT:      returns the largest element in the list

def listmax(a):
    if a == []:
        element = "None"
    else:
        element = a[0]
        for i in a:
            if i > element:
                element = i
    return element

# function:    listcopy
# INPUT:       a list
# PROCESSING:  creates a new list which serves as a copy of the supplied list
# OUTPUT:      returns a new copy of the list

def listcopy(a):
    new_list = []
    for i in a:
        new_list += [i]
    return new_list

# function:    listappend
# INPUT:       a list and an element to add to the list (any data type)
# PROCESSING:  creates a new list which includes the new element appended
#              to the end of the list
# OUTPUT:      returns a new copy of the list

def listappend(a, b):
    new_list = a + [b]
    return new_list

# function:    listinsert
# INPUT:       a list, a location (integer) and a data 
#              element (can be a string, float, Boolean or 
#              int)
# PROCESSING:  inserts the supplied data element into the 
#              list at the desired location
# OUTPUT:      return a new copy of the list that contains
#              the inserted element

def listinsert(a, b, c):
    new_list = a[:b] + [c] + a[b:]
    return new_list

# function:    listremove
# INPUT:       a list and a data element (can be a string, 
#              float, Boolean or int)
# PROCESSING:  removes all occurrences of the supplied 
#              data element from the list.  You can assume 
#              that the data element is present in the list 
#              somewhere.
# OUTPUT:      return a new copy of the list with the
#              desired element removed

def listremove(a, b):
    new_list = []
    for i in a:
        if i != b:
            new_list += [i]
    return new_list

# function:    listreverse
# INPUT:       a list
# PROCESSING:  creates a copy of the supplied list that
#              contains the same elements as the original
#              list, but in reverse order
# OUTPUT:      return a new copy of the list in reverse order

def listreverse(a):
    new_list = []
    for i in range(-1, -listlen(a)-1, -1):
        new_list += [a[i]]
    return new_list

