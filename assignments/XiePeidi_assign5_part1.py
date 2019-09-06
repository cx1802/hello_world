"""
Peidi Xie
March 30th, 2019
Introduction to Programming, Section 03
Part 1: Pizza Party
"""

# prompt the user to enter the budget for party, the price per slice of pizza,
# the price per pie of pizza, and the number of people attending party
budget = int(input("Enter budget for your party: "))
price_slice = float(input("Cost per slice of pizza: "))
price_pie = float(input("Cost per whole pizza pie (8 slices): "))
num_ppl = int(input("How many people will be attending your party? "))

# ask the user for how many slices of pizza each individual wants, and keep recording
# the total number of slices of pizza having been ordered
total_slices = 0
for i in range(1, num_ppl+1):
    slices = int(input("Enter number of slices for person #" + str(i) + ": "))
    # if the user enter a non-positive number, prompt the user to enter another number
    # until the user supplies a valid number
    while slices <= 0:
        print("Not a valid entry, try again!")
        print()
        slices = int(input("Enter number of slices for person #" + str(i) + ": "))
    total_slices += slices

# calculate how many slices and pies the user have ordered and the total cost of those slices and pies
num_pies = total_slices // 8
num_slices = total_slices % 8
total_cost = num_pies * price_pie + num_slices * price_slice

# report to the user the number of slices and pies he ordered, the cost of them, and how much budget remained
# if the total cost of pizza ordered exceeds the budget, warn the user that the order cannot be completed
if total_cost < budget:
    print("You should purchase", num_pies, "pies and", num_slices, "slices")
    print("Your total cost will be:", format(total_cost, ".2f"))
    print("You will still have", format(budget-total_cost, ".2f"), "left after your order")   
elif total_cost == budget:
    print("You should purchase", num_pies, "pies and", num_slices, "slices")
    print("Your total cost will be:", format(total_cost, ".2f"))
    print("You will have no money left after your order.")
else:
    print("Your order cannot be completed.")
    print("You would need to purchase", num_pies, "pies and", num_slices, "slices")
    print("This would put you over budget by", format(total_cost-budget, ".2f"))
    
