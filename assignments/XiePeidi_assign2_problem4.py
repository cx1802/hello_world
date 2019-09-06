"""
Peidi Xie
February 12th, 2019
Introduction to Programming, Section 03
Problem 4: Data Size Converter
"""
# ask the user for the file size in Kilobytes (KB)
_kilobytes = float(input("Enter a file size, in kilobytes (KB): "))
print()

# print out the file size in Kilobytes
# print in integer if the integer value is equal to the float value
if _kilobytes == int(_kilobytes):
    print(int(_kilobytes), end=" ")
else:
    print(_kilobytes, end=" ")
print("KB ...")
print()

# convert the file size the user entered to units of bits, bytes, megabytes, and gigabytes
_bits = _kilobytes * 1024 * 8
_bytes = _kilobytes * 1024
_megabytes = _kilobytes / 1024
_gigabytes = _megabytes / 1024

# format the converted value to two decimal places and add comma separators
f_bits = format(_bits, ",.2f")
f_bytes = format(_bytes, ",.2f")
f_megabytes = format(_megabytes, ",.2f")
f_gigabytes = format(_gigabytes, ",.2f")

# output the converted value. Remember to format the four converted values to
# line up in a right-justified column
print("... in bits", end="")
print(format(f_bits, ">29s"), "bits")
print("... in bytes", end="")
print(format(f_bytes, ">28s"), "bytes")
print("... in megabytes", end="")
print(format(f_megabytes, ">24s"), "MB")
print("... in gigabytes", end="")
print(format(f_gigabytes, ">24s"), "GB")

# the following line would cause a run-time error because I forgot that
# the output of format function would be automatically turned into a string value
# which is incalculable in a math operation
# _bits = format(_kilobytes * 1024 * 8, ",.2f")
# _bytes = format(_bits / 8, ",.2f")

# the following line would cause a logical error because I forgot to
# include the formatting pattern within the parentheses of the format function
# so that the string literal wasn't formatted
# print(format(f_bits), ">29s", "bits")

# the following line would cause a syntax error because I forgot to
# put a colon after the "if" statement
# if _kilobytes == int(_kilobytes)

# the following line would cause a run-time error because I forgot to
# delimit the string literal which I didn't define as a variable when I was attempting to print out
# print(format(f_bits, ">29s"), bits)

# the following line would cause a logical error because I typed the wrong argument
# "sep" when I was trying to override the default behavior of the print() function to print a linebreak
# print("... in bits", sep="")
