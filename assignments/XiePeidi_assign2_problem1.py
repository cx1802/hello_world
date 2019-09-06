"""
Peidi Xie
February 12th, 2019
Introduction to Programming, Section 03
Problem 1: Lottery Winnings Calculator
"""
# ask the user for the total amount they won, the number of people splitting
# the winnings, and the tax rate being applied to each person's share
total = int(input("How much money did you win? "))
num_ppl = int(input("How many people are splitting the winnings? "))
tax_rate = int(input("What is the tax rate on lottery winnings (i.e. 25 = 25%): "))

# compute the total amount they won, the amount of each person's share,
# the tax due on each share, and the final amount each person will take home
total1 = float(total)
per_won = total1 / num_ppl
per_tax = per_won * tax_rate * 0.01
per_takehome = per_won - per_tax

# format the computed four variables into two decimal places and add the "comma" separator
total2 = format(total1, ",.2f")
per_won2 = format(per_won, ",.2f")
per_tax2 = format(per_tax, ",.2f")
per_takehome2 = format(per_takehome, ",.2f")

# output the formatted four variables
print()
print("In total you won $", end="")
print(total2)
print("Split", num_ppl, "ways that amounts to $", end="")
print(per_won2, "per person")
print("Tax per person: $", end="")
print(per_tax2)
print("Take home amount per person: $", end="")
print(per_takehome2)


