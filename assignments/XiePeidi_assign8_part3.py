"""
Peidi Xie
April 28th, 2019
Introduction to Programming, Section 03
Part 3: Fast Food Restaurant
"""
'''
Part 3a
'''

# the lists of the restaurant's products and their corresponding unit prices
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]

# keep prompting the user to choose the service of inquiry into the products
while True:
    operation = input("(s)earch for product or (q)uit: ")
    # if the user chooses "search", asks for the product name and report the unit price of the product
    if operation == "s":
        product = input("Enter a product name: ")
        # data validation: the product name the user provides need to be in the list
        if product in product_names:
            print("We sell " + '"' + product + '"' + " at", product_costs[product_names.index(product)], "per unit")
        else:
            print("Sorry, we don't sell " + '"' + product + '"')
    # if the user chooses "quit", quit the program
    elif operation == "q":
        print("See you soon!")
        break
    # data validation: the user has to choose the designated service
    else:
        print("Invalid option, try again")
    print()

'''
Part 3b
'''

# the lists of the restaurant's products, corresponding unit prices and quantities
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
storage = [10, 5, 20]

# keep prompting the user to choose one of the services of inquiry into the products
while True:
    operation = input("(s)earch, (l)ist or (q)uit: ")
    # if the user chooses "search", asks for the product name and report the unit price and the current quantity of the product
    if operation == "s":
        product = input("Enter a product name: ")
        # data validation: the product name the user provides need to be in the list
        if product in product_names:
            print("We sell " + '"' + product + '"' + " at", product_costs[product_names.index(product)], "per unit")
            print("We currently have", storage[product_names.index(product)], "in stock")
        else:
            print("Sorry, we don't sell " + '"' + product + '"')
    # if the user chooses "list", lists all product names, their corresponding unit prices and quantities in formatted columns
    elif operation == "l":
        print(format("Product", "<13s") + format("Price", ">8s") + format("Quantity", ">10s"))
        for i in range(len(product_names)):
            print(format(product_names[i], "<13s") + format(str(product_costs[i]), ">8s") + 3*" " + str(storage[i]))
    # if the user chooses "quit", quit the program
    elif operation == "q":
        print("See you soon!")
        break
    # data validation: the user has to choose among designated services
    else:
        print("Invalid option, try again")
    print()

'''
Part 3c
'''

# the lists of the restaurant's products, corresponding unit prices and quantities
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
storage = [10, 5, 20]

# keep prompting the user to choose one of the services of inquiry into the products
while True:
    operation = input("(s)earch, (l)ist, (a)dd or (q)uit: ")
    # if the user chooses "search", asks for the product name and report the unit price and the current quantity of the product
    if operation == "s":
        product = input("Enter a product name: ")
        # data validation: the product name the user provides need to be in the list
        if product in product_names:
            print("We sell " + '"' + product + '"' + " at", product_costs[product_names.index(product)], "per unit")
            print("We currently have", storage[product_names.index(product)], "in stock")
        else:
            print("Sorry, we don't sell " + '"' + product + '"')
    # if the user chooses "list", lists all product names, their corresponding unit prices and quantities in formatted columns
    elif operation == "l":
        print(format("Product", "<18s") + format("Price", ">13s") + format("Quantity", ">10s"))
        for i in range(len(product_names)):
            print(format(product_names[i], "<18s") + format(str(product_costs[i]), ">13s") + format(str(storage[i]), ">10s"))
    # if the user chooses "add", asks for the new product name, its unit price and quantity
    # append the three values the user supplies to their corresponding lists
    elif operation == "a":
        new_product = input("Enter a new product name: ")
        # data validation: the new product name cannot already exist in the list
        while new_product in product_names:
            print("Sorry, we already sell that product. Try again.")
            new_product = input("Enter a new product name: ")
        product_names += [new_product]
        new_cost = float(input("Enter a product cost: "))
        # data validation: the new unit price has to be positive
        while new_cost <= 0:
            print("Invalid cost. Try again.")
            new_cost = float(input("Enter a product cost: "))
        product_costs += [new_cost]
        new_storage = int(input("How many of these products do we have? "))
        # data validation: the new quantity has to be positive
        while new_storage <= 0:
            print("Invalid quantity. Try again.")
            new_storage = int(input("How many of these products do we have? "))
        storage += [new_storage]
        print("Product added!")
    # if the user chooses "quit", quit the program
    elif operation == "q":
        print("See you soon!")
        break
    # data validation: the user has to choose among designated services
    else:
        print("Invalid option, try again")
    print()


'''
Part 3d
'''

# the lists of the restaurant's products, corresponding unit prices and quantities
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
storage = [10, 5, 20]

# keep prompting the user to choose one of the services of inquiry into the products
while True:
    operation = input("(s)earch, (l)ist, (a)dd, (r)emove or (q)uit: ")
    # if the user chooses "search", asks for the product name and report the unit price and the current quantity of the product
    if operation == "s":
        product = input("Enter a product name: ")
        # data validation: the product name the user provides need to be in the list
        if product in product_names:
            print("We sell " + '"' + product + '"' + " at", product_costs[product_names.index(product)], "per unit")
            print("We currently have", storage[product_names.index(product)], "in stock")
        else:
            print("Sorry, we don't sell " + '"' + product + '"')
    # if the user chooses "list", lists all product names, their corresponding unit prices and quantities in formatted columns
    elif operation == "l":
        print(format("Product", "<18s") + format("Price", ">13s") + format("Quantity", ">10s"))
        for i in range(len(product_names)):
            print(format(product_names[i], "<18s") + format(str(product_costs[i]), ">13s") + format(str(storage[i]), ">10s"))
    # if the user chooses "add", asks for the new product name, its unit price and quantity
    # append the three values the user supplies to their corresponding lists
    elif operation == "a":
        new_product = input("Enter a new product name: ")
        # data validation: the new product name cannot already exist in the list
        while new_product in product_names:
            print("Sorry, we already sell that product. Try again.")
            new_product = input("Enter a new product name: ")
        product_names += [new_product]
        new_cost = float(input("Enter a product cost: "))
        # data validation: the new unit price has to be positive
        while new_cost <= 0:
            print("Invalid cost. Try again.")
            new_cost = float(input("Enter a product cost: "))
        product_costs += [new_cost]
        new_storage = int(input("How many of these products do we have? "))
        # data validation: the new quantity has to be positive
        while new_storage <= 0:
            print("Invalid quantity. Try again.")
            new_storage = int(input("How many of these products do we have? "))
        storage += [new_storage]
        print("Product added!")
    # if the user chooses "remove", ask for the name of product the user wants to remove
    # remove the product name, its unit price and the quantity from corresponding lists
    elif operation == "r":
        remove_product = input("Enter a product name: ")
        # data validatiom: the name of the product to be removed has to be in the list
        if remove_product in product_names:
            product_costs.remove(product_costs[product_names.index(remove_product)])
            storage.remove(storage[product_names.index(remove_product)])
            product_names.remove(remove_product)
            print("Product removed!")
        else:
            print("Product doesn't exist. Can't remove.")
    # if the user chooses "quit", quit the program
    elif operation == "q":
        print("See you soon!")
        break
    # data validation: the user has to choose among designated services
    else:
        print("Invalid option, try again")
    print()


'''
Part 3e
'''
# the lists of the restaurant's products, corresponding unit prices and quantities
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
storage = [10, 5, 20]

# keep prompting the user to choose one of the services of inquiry into the products
while True:
    operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate or (q)uit: ")
    # if the user chooses "search", asks for the product name and report the unit price and the current quantity of the product
    if operation == "s":
        product = input("Enter a product name: ")
        # data validation: the product name the user provides need to be in the list
        if product in product_names:
            print("We sell " + '"' + product + '"' + " at", product_costs[product_names.index(product)], "per unit")
            print("We currently have", storage[product_names.index(product)], "in stock")
        else:
            print("Sorry, we don't sell " + '"' + product + '"')
    # if the user chooses "list", lists all product names, their corresponding unit prices and quantities in formatted columns
    elif operation == "l":
        print(format("Product", "<18s") + format("Price", ">13s") + format("Quantity", ">10s"))
        for i in range(len(product_names)):
            print(format(product_names[i], "<18s") + format(format(product_costs[i], ".2f"), ">13s") + format(str(storage[i]), ">10s"))
    # if the user chooses "add", asks for the new product name, its unit price and quantity
    # append the three values the user supplies to their corresponding lists
    elif operation == "a":
        new_product = input("Enter a new product name: ")
        # data validation: the new product name cannot already exist in the list
        while new_product in product_names:
            print("Sorry, we already sell that product. Try again.")
            new_product = input("Enter a new product name: ")
        product_names += [new_product]
        new_cost = float(input("Enter a product cost: "))
        # data validation: the new unit price has to be positive
        while new_cost <= 0:
            print("Invalid cost. Try again.")
            new_cost = float(input("Enter a product cost: "))
        product_costs += [new_cost]
        new_storage = int(input("How many of these products do we have? "))
        # data validation: the new quantity has to be positive
        while new_storage <= 0:
            print("Invalid quantity. Try again.")
            new_storage = int(input("How many of these products do we have? "))
        storage += [new_storage]
        print("Product added!")
    # if the user chooses "remove", ask for the name of product the user wants to remove
    # remove the product name, its unit price and the quantity from corresponding lists
    elif operation == "r":
        remove_product = input("Enter a product name: ")
        # data validatiom: the name of the product to be removed has to be in the list
        if remove_product in product_names:
            product_costs.remove(product_costs[product_names.index(remove_product)])
            storage.remove(storage[product_names.index(remove_product)])
            product_names.remove(remove_product)
            print("Product removed!")
        else:
            print("Product doesn't exist. Can't remove.")
    # if the user chooses "update", asks for the name of the product the user wants to update
    # asks for the feature of the product the user wants to update (name, price, or quantity)
    # asks for the new information to supplant the old information and change the values in the lists accordingly
    elif operation == "u":
        update_product = input("Enter a product name: ")
        # data validation: the product to be updated need to be in the list
        if update_product in product_names:
            print("What would you like to update?")
            update = input("(n)ame, (c)ost or (q)uantity: ")
            if update == "n":
                update_name = input("Enter a new name: ")
                # data validation: the new name cannot already exist in the list
                while update_name in product_names:
                    print("Duplicate name!")
                    update_name = input("Enter a new name: ")
                product_names[product_names.index(update_product)] = update_name
                print("Product name has been updated")
            elif update == "c":
                update_cost = float(input("Enter a new cost: "))
                # data validation: the value of the new price has to be positive
                while update_cost <= 0:
                    print("Invalid cost!")
                    update_cost = float(input("Enter a new cost: "))
                product_costs[product_names.index(update_product)] = update_cost
                print("Product cost has been updated")
            elif update == "q":
                update_q = int(input("Enter a new quantity: "))
                # data validation: the value of the new quantity has to be positive
                while update_q <= 0:
                    print("Invalid quantity!")
                    update_q = int(input("Enter a new quantity: "))
                storage[product_names.index(update_product)] = update_q
                print("Product quantity has been updated")
            else:
                print("Invalid option")
        else:
            print("Product doesn't exist. Can't update.")
    # if the user chooses "quit", quit the program
    elif operation == "q":
        print("See you soon!")
        break
    # data validation: the user has to choose among designated services
    else:
        print("Invalid option, try again")
    print()

'''
Part 3f
'''

# the lists of the restaurant's products, corresponding unit prices and quantities
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
storage = [10, 5, 20]

# keep prompting the user to choose one of the services of inquiry into the products
while True:
    operation = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    # if the user chooses "search", asks for the product name and report the unit price and the current quantity of the product
    if operation == "s":
        product = input("Enter a product name: ")
        if product in product_names:
            print("We sell " + '"' + product + '"' + " at", product_costs[product_names.index(product)], "per unit")
            print("We currently have", storage[product_names.index(product)], "in stock")
        # data validation: the product name the user provides need to be in the list
        else:
            print("Sorry, we don't sell " + '"' + product + '"')
    # if the user chooses "list", lists all product names, their corresponding unit prices and quantities in formatted columns 
    elif operation == "l":
        print(format("Product", "<18s") + format("Price", ">13s") + format("Quantity", ">10s"))
        for i in range(len(product_names)):
            print(format(product_names[i], "<18s") + format(format(product_costs[i], ".2f"), ">13s") + format(str(storage[i]), ">10s"))
    # if the user chooses "add", asks for the new product name, its unit price and quantity
    # append the three values the user supplies to their corresponding lists
    elif operation == "a":
        new_product = input("Enter a new product name: ")
        # data validation: the new product name cannot already exist in the list
        while new_product in product_names:
            print("Sorry, we already sell that product. Try again.")
            new_product = input("Enter a new product name: ")
        product_names += [new_product]
        new_cost = float(input("Enter a product cost: "))
        # data validation: the new unit price has to be positive
        while new_cost <= 0:
            print("Invalid cost. Try again.")
            new_cost = float(input("Enter a product cost: "))
        product_costs += [new_cost]
        new_storage = int(input("How many of these products do we have? "))
        # data validation: the new quantity has to be positive
        while new_storage <= 0:
            print("Invalid quantity. Try again.")
            new_storage = int(input("How many of these products do we have? "))
        storage += [new_storage]
        print("Product added!")
    # if the user chooses "remove", ask for the name of product the user wants to remove
    # remove the product name, its unit price and the quantity from corresponding lists
    elif operation == "r":
        remove_product = input("Enter a product name: ")
        # data validatiom: the name of the product to be removed has to be in the list
        if remove_product in product_names:
            product_costs.remove(product_costs[product_names.index(remove_product)])
            storage.remove(storage[product_names.index(remove_product)])
            product_names.remove(remove_product)
            print("Product removed!")
        else:
            print("Product doesn't exist. Can't remove.")
    # if the user chooses "update", asks for the name of the product the user wants to update
    # asks for the feature of the product the user wants to update (name, price, or quantity)
    # asks for the new information to supplant the old information and change the values in the lists accordingly
    elif operation == "u":
        update_product = input("Enter a product name: ")
        # data validation: the product to be updated need to be in the list
        if update_product in product_names:
            print("What would you like to update?")
            update = input("(n)ame, (c)ost or (q)uantity: ")
            if update == "n":
                update_name = input("Enter a new name: ")
                # data validation: the new name cannot already exist in the list
                while update_name in product_names:
                    print("Duplicate name!")
                    update_name = input("Enter a new name: ")
                product_names[product_names.index(update_product)] = update_name
                print("Product name has been updated")
            elif update == "c":
                update_cost = float(input("Enter a new cost: "))
                # data validation: the value of the new price has to be positive
                while update_cost <= 0:
                    print("Invalid cost!")
                    update_cost = float(input("Enter a new cost: "))
                product_costs[product_names.index(update_product)] = update_cost
                print("Product cost has been updated")
            elif update == "q":
                update_q = int(input("Enter a new quantity: "))
                # data validation: the value of the new quantity has to be positive
                while update_q <= 0:
                    print("Invalid quantity!")
                    update_q = int(input("Enter a new quantity: "))
                storage[product_names.index(update_product)] = update_q
                print("Product quantity has been updated")
            # data validation: the user has to choose among the features of name, price, and quantity
            else:
                print("Invalid option")
        else:
            print("Product doesn't exist. Can't update.")
    # if the user chooses "report", report the most expensive product and its price, the least expensive product and its price
    # and the total value of all products in the inventory in formatted columns
    elif operation == "e":
        print(format("Most expensive product:", "<29s") + format(max(product_costs), ".2f") + " (" + product_names[product_costs.index(max(product_costs))] + ")")
        print(format("Least expensive product:", "<29s") + format(min(product_costs), ".2f") + " (" + product_names[product_costs.index(min(product_costs))] + ")")
        total_value = 0
        for j in range(len(product_costs)):
            total_value += product_costs[j] * storage[j]
        print("Total value of all products:", format(total_value, ".2f"))
    # if the user chooses "quit", quit the program
    elif operation == "q":
        print("See you soon!")
        break
    # data validation: the user has to choose among designated services
    else:
        print("Invalid option, try again")
    print()

