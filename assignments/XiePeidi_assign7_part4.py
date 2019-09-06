"""
Peidi Xie
April 14th, 2019
Introduction to Programming, Section 03
Part 4
"""
# function:   string_length
# input:      a word (String)
# processing: computes the length of the supplied String (without using the len() function)
# output:     returns the length of the string (integer)

def string_length(word):
    length = 0
    for i in word:
        length += 1
    return length

# function:   string_isalpha
# input:      a word (String)
# processing: determines if the supplied String contains all alphabetic characters (A-Z,a-z)
#             DO NOT USE THE "isalpha()" METHOD or any other String methods!
# output:     returns True of False (boolean)

def string_isalpha(word):
    non_alpha = 0
    alpha = 0
    for i in word:
        if not (i >= "A" and i <= "Z") and not (i >= "a" and i <= "z"):
            non_alpha += 1
        else:
            alpha += 1
    if non_alpha == 0 and alpha > 0:
        isalpha = True
    else:
        isalpha = False
    return isalpha

# function:   string_isupper
# input:      a word (String)
# processing: determines if the supplied String contains all uppercase characters (A-Z)
#             DO NOT USE THE "isupper()" METHOD or any other String methods!
# output:     returns True of False (boolean)

def string_isupper(word):
    non_upper = 0
    upper = 0
    for i in word:
        if i < "A" or i > "Z":
            non_upper += 1
        else:
            upper += 1
    if non_upper == 0 and upper > 0:
        isupper = True
    else:
        isupper = False
    return isupper

# function:   string_isdigit
# input:      a word (String)
# processing: determines if the supplied String contains all numeric characters (0-9)
#             DO NOT USE THE "isdigit()" METHOD or any other String methods!
# output:     returns True of False (boolean)

def string_isdigit(word):
    non_numeric = 0
    numeric = 0
    for i in word:
        if i < "0" or i > "9":
            non_numeric += 1
        else:
            numeric += 1
    if non_numeric == 0 and numeric > 0:
        isnumeric = True
    else:
        isnumeric = False
    return isnumeric

# function:   string_swapcase
# input:      a word (String)
# processing: swaps uppercase characters with lowercase characters & vice-versa
#             DO NOT USE THE "swapcase()" METHOD or any other String methods!
# output:     returns a new copy of the String

def string_swapcase(word):
    new_word = ""
    for i in word:
        if i >= "a" and i <= "z":
            i = chr(ord(i) - 32)
        elif i >= "A" and i <= "Z":
            i = chr(ord(i) + 32)
        new_word += i
    return new_word

# function:   string_lower
# input:      a word (String)
# processing: converts all characters in a String to their lowecase equivalents
#             DO NOT USE THE "lower()" METHOD OR "str.lower()"! or any other String methods!
# output:     returns a new copy of the String

def string_lower(word):
    new_word = ""
    for i in word:
        if i >= "A" and i <= "Z":
            i = chr(ord(i) + 32)
        new_word += i
    return new_word




