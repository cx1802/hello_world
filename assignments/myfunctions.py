'''
Part 2a
'''

# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)

def horizontal_line(width, character):
    return width*character

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)

def vertical_line(shift, height, character):
    final_pattern = ""
    pattern = " "*shift + character + "\n"
    for i in range(height):
        final_pattern += pattern 
    return final_pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)

def two_vertical_lines(width, height, character):
    final_pattern = ""
    pattern = character + " "*(width-2) + character + "\n"
    for i in range(height):
        final_pattern += pattern
    return final_pattern


'''
Part 2b
'''

# function:   number_0
# input:      a width value (integer) and a single character (string)
# processing: generates the number 0 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_0(width, character):
    pattern = horizontal_line(width, character) + "\n" + two_vertical_lines(width, 3, character) + horizontal_line(width, character) + "\n"
    return pattern

# function:   number_1
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_1(width, character):
    pattern = vertical_line(width-1, 5, character)
    return pattern

# function:   number_2
# input:      a width value (integer) and a single character (string)
# processing: generates the number 2 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_2(width, character):
    pattern = horizontal_line(width, character) + "\n" + vertical_line(width-1, 1, character) + horizontal_line(width, character) + "\n" + vertical_line(0, 1, character) + horizontal_line(width, character) + "\n"
    return pattern

# function:   number_3
# input:      a width value (integer) and a single character (string)
# processing: generates the number 3 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_3(width, character):
    pattern = horizontal_line(width, character) + "\n" + vertical_line(width-1, 1, character) + horizontal_line(width, character) + "\n" + vertical_line(width-1, 1, character) + horizontal_line(width, character) + "\n"
    return pattern

# function:   number_4
# input:      a width value (integer) and a single character (string)
# processing: generates the number 4 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_4(width, character):
    pattern = two_vertical_lines(width, 2, character) + horizontal_line(width, character) + "\n" + vertical_line(width-1, 2, character)
    return pattern

# function:   number_5
# input:      a width value (integer) and a single character (string)
# processing: generates the number 5 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_5(width, character):
    pattern = horizontal_line(width, character) + "\n" + vertical_line(0, 1, character) + horizontal_line(width, character) + "\n" + vertical_line(width-1, 1, character) + horizontal_line(width, character) + "\n"
    return pattern

# function:   number_6
# input:      a width value (integer) and a single character (string)
# processing: generates the number 6 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_6(width, character):
    pattern = horizontal_line(width, character) + "\n" + vertical_line(0, 1, character) + horizontal_line(width, character) + "\n" + two_vertical_lines(width, 1, character) + horizontal_line(width, character) + "\n"
    return pattern

# function:   number_7
# input:      a width value (integer) and a single character (string)
# processing: generates the number 7 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_7(width, character):
    pattern = horizontal_line(width, character) + "\n" + vertical_line(width-1, 4, character)
    return pattern

# function:   number_8
# input:      a width value (integer) and a single character (string)
# processing: generates the number 8 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_8(width, character):
    pattern = horizontal_line(width, character) + "\n" + two_vertical_lines(width, 1, character) + horizontal_line(width, character) + "\n" + two_vertical_lines(width, 1, character) + horizontal_line(width, character) + "\n"
    return pattern

# function:   number_9
# input:      a width value (integer) and a single character (string)
# processing: generates the number 9 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def number_9(width, character):
    pattern = horizontal_line(width, character) + "\n" + two_vertical_lines(width, 1, character) + horizontal_line(width, character) + "\n" + vertical_line(width-1, 2, character)
    return pattern

'''
Part 2c
'''

# function:   print_number
# input:      a number to print (integer), a width value (integer) and a single character (string)
# processing: prints the desired number to the screen using the supplied width value
# output:     does not return anything

def print_number(number, width, character):
    if number == 0:
        print(number_0(width, character))
    elif number == 1:
        print(number_1(width, character))
    elif number == 2:
        print(number_2(width, character))
    elif number == 3:
        print(number_3(width, character))
    elif number == 4:
        print(number_4(width, character))
    elif number == 5:
        print(number_5(width, character))
    elif number == 6:
        print(number_6(width, character))
    elif number == 7:
        print(number_7(width, character))
    elif number == 8:
        print(number_8(width, character))
    elif number == 9:
        print(number_9(width, character))


'''
Part 2d
'''

# function:   plus
# input:      a width value (integer) and a single character (string)
# processing: generates the addition operator as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def plus(width, character):
    if width % 2 == 1:
        pattern = vertical_line(width//2, 2, character) + horizontal_line(width, character) + "\n" + vertical_line(width//2, 2, character)
    else:
        pattern = vertical_line(width//2-1, 2, horizontal_line(2, character)) + horizontal_line(width, character) + "\n" + vertical_line(width//2-1, 2, horizontal_line(2, character))
    return pattern

# function:   minus
# input:      a width value (integer) and a single character (string)
# processing: generates the subtraction operator as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def minus(width, character):
    pattern = 2 * "\n" + horizontal_line(width, character) + 2 * "\n"
    return pattern

# function:   multiply
# input:      a width value (integer) and a single character (string)
# processing: generates the multiplication operator as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def multiply(width, character):
    if width % 2 == 1:
        pattern = two_vertical_lines(width, 1, character) + two_vertical_lines(width-3, 1, " "+character) + vertical_line(width//2, 1, character) + two_vertical_lines(width-3, 1, " "+character) + two_vertical_lines(width, 1, character)
    else:
        pattern = two_vertical_lines(width, 1, character) + two_vertical_lines(width-3, 1, " "+character) + vertical_line(width//2-1, 1, horizontal_line(2, character)) + two_vertical_lines(width-3, 1, " "+character) + two_vertical_lines(width, 1, character)
    return pattern

# function:   divide
# input:      a width value (integer) and a single character (string)
# processing: generates the division operator as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)

def divide(width, character):
    if width % 2 == 1:
        pattern = vertical_line(width//2, 1, character) + "\n" + horizontal_line(width, character) + 2*"\n" + vertical_line(width//2, 1, character)
    else:
        pattern = vertical_line(width//2-1, 1, horizontal_line(2, character)) + "\n" + horizontal_line(width, character) + 2*"\n" + vertical_line(width//2-1, 1, horizontal_line(2, character))
    return pattern


'''
Part 2e
'''

# function:   check_answer
# input:      two numbers (number1 & number2, both integers); an answer (an integer)
#             and an operator (+ or - or * or /, expressed as a String)
# processing: determines if the supplied expression is correct.  for example, if the operator
#             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
#             (1 + 2 = 3).
# output:     returns True if the expression is correct, False if it is not correct

def check_answer(number1, number2, answer, operator):
    if operator == "+":
        if answer == number1 + number2:
            result = True
        else:
            result = False
    elif operator == "-":
        if answer == number1 - number2:
            result = True
        else:
            result = False
    elif operator == "*":
        if answer == number1 * number2:
            result = True
        else:
            result = False
    elif operator == "/":
        if answer == number1 / number2:
            result = True
        else:
            result = False
    return result
