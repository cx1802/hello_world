"""
Peidi Xie
February 6th, 2019
Introduction to Programming, Section 03
Problem 3: Math Expressions
"""

# Print the dash line and the title of the program.
# The title should be properly formatted.
print("--------------------------------------------------------------")
formatted_title = format("mL to US Fluid Volume Units", ">43s")
print(formatted_title)
print("--------------------------------------------------------------")

# Calculate the number of units of mL that is equal to 250 milliliters.
# Print the measurement mL and the corresponding number of units.
# Properly formatted into two left-aligned columns.
f_num_mL = format("250.0", ">17s")
formatted_mL = format("mL:", ">11s")
print(formatted_mL, f_num_mL)

# Calculate the number of units of tsp that is equal to 250 milliliters.
# Print the measurement tsp and the corresponding number of units.
# Properly formatted into two left-aligned columns.
num_tsp = 250.0 *0.202884
f_num_tsp = format(str(num_tsp), ">29s")
formatted_tsp = format("tsp:", ">12s")
print(formatted_tsp, f_num_tsp)

# Calculate the number of units of tbsq that is equal to 250 milliliters.
# Print the measurement tbsq and the corresponding number of units.
# Properly formatted into two left-aligned columns.
num_tbsq = num_tsp / 3
f_num_tbsq = format(str(num_tbsq), ">16s")
formatted_tbsq = format("tbsq:", ">13s")
print(formatted_tbsq, f_num_tbsq)

# Calculate the number of units of cup that is equal to 250 milliliters.
# Print the measurement cup(s) and the corresponding number of units.
# Properly formatted into two left-aligned columns.
num_cup = num_tbsq / 16
f_num_cup = format(str(num_cup), ">17s")
formatted_cup = format("cup(s):", ">15s")
print(formatted_cup, f_num_cup)

# Calculate the number of units of pint that is equal to 250 milliliters.
# Print the measurement pint(s) and the corresponding number of units.
# Properly formatted into two left-aligned columns.
num_pint = num_cup / 2
f_num_pint = format(str(num_pint), ">17s")
formatted_pint = format("pint(s):", ">16s")
print(formatted_pint, f_num_pint)

# Calculate the number of units of quart that is equal to 250 milliliters.
# Print the measurement quart(s) and the corresponding number of units.
# Properly formatted into two left-aligned columns.
num_quart = num_pint / 2
f_num_quart = format(str(num_quart), ">17s")
formatted_quart = format("quart(s):", ">17s")
print(formatted_quart, f_num_quart)

# Calculate the number of units of gallon that is equal to 250 milliliters.
# Print the measurement gallon(s) and the corresponding number of units.
# Properly formatted into two left-aligned columns.
num_gallon = num_quart / 4
f_num_gallon = format(str(num_gallon), ">18s")
formatted_gallon = format("gallon(s):", ">18s")
print(formatted_gallon, f_num_gallon)

# Calculate the number of units of floz that is equal to 250 milliliters.
# Print the measurement floz and the corresponding number of units.
# Properly formatted into two left-aligned columns.
num_floz = 250.0 / 29.5735
f_num_floz = format(str(num_floz), ">26s")
formatted_floz = format("fl oz:", ">14s")
print(formatted_floz, f_num_floz)

# Print the dash line
print("--------------------------------------------------------------")
