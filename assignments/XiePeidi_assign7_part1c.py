"""
Peidi Xie
April 14th, 2019
Introduction to Programming, Section 03
Part 1c
"""

'''
Part1a
'''
# ask the user to enter a username.
# if the username doesn't comply to the rules, prompt the user to enter again until valid data is supplied
while True:
    username = input("Enter a username: ")
    # display the length of the username
    print("* Length of username:", len(username))
    # a valid username should be between 8 and 15 characters long
    if len(username) < 8 or len(username) > 15:
        checker1 = False
    else:
        checker1 = True
    # display whether the username is comprised of only alphabetic and numeric characters
    print("* All characters are alpha-numeric:", username.isalnum())
    # a valid username should be comprised of only alphabetic and numeric characters
    checker2 = username.isalnum()
    # display whether the first and last characters of the username are not digits
    print("* First & Last characters are not digits:", not (username[0].isnumeric() or username[-1].isnumeric()))
    # the first and last characters of a valid username should not be digits
    checker3 = username[0].isalpha() and username[-1].isalpha()
    # count the numbers of uppercase, lowercase, and numeric characters in the username
    upper = 0
    lower = 0
    digit = 0
    for i in username:
        if ord(i) >= 65 and ord(i) <= 90:
            upper += 1
        if ord(i) >= 97 and ord(i) <= 122:
            lower += 1
        if ord(i) >= 48 and ord(i) <= 57:
            digit += 1
    # display the numbers of uppercase, lowercase, and numeric characters in the username
    print("* # of uppercase characters in the username:", upper)
    print("* # of lowercase characters in the username:", lower)
    print("* # of digits in the username:", digit)
    # a valid username should have at least one uppercase character, one lowercase character, and one numeric character
    checker4 = upper >= 1 and lower >= 1 and digit >= 1
    # check if the username complies to all rules and tell the user the username is valid or not
    checker = checker1 and checker2 and checker3 and checker4
    if checker:
        print("Username is valid")
        break
    else:
        print("Username is invalid, please try again")
        print()

'''
Part 1c
'''

# ask the user to enter a password
print()
password = input("Enter a password: ")
# display the length of the password
print("* Length of password:", len(password))
# a valid password should be at least 8 characters long
if len(password) >= 8:
    checker1 = True
else:
    checker1 = False
# display whether the password contains the username
print("* Username is part of password:", username in password)
# a valid password should not contains the username
checker2 = not (username in password)
# keep track of the numbers of uppercase, lowercase, numeric, a selection of special characters, and invalid characters in the password
upper = 0
lower = 0
digit = 0
special_chr = 0
invalid_chr = 0
invalid_part = ""
for i in password:
    if ord(i) >= 65 and ord(i) <= 90:
        upper += 1
    elif ord(i) >= 97 and ord(i) <= 122:
        lower += 1
    elif ord(i) >= 48 and ord(i) <= 57:
        digit += 1
    elif ord(i) >= 35 and ord(i) <= 38:
        special_chr += 1
    else:
        invalid_part += i
        invalid_chr += 1
# display the numbers of uppercase, lowercase, numeric, special, and invalid characters in the password
print("* # of uppercase characters in the password:", upper)
print("* # of lowercase characters in the password:", lower)
print("* # of digits in the password:", digit)
print("* # of special characters in the password:", special_chr)
print("* # of invalid characters in the password:", invalid_chr)
# a valid password should have at least one uppercase character, one lowercase character,
# one numeric character, one special character, and no invalid character
checker4 = upper >= 1 and lower >= 1 and digit >= 1 and special_chr >= 1 and invalid_chr == 0
# check if the password complies to all rules and tell the user the password is valid or not
checker = checker1 and checker2 and checker3 and checker4
if checker:
    print("Password is valid")
else:
    print("Password is invalid")
    print()
    # ask the user if the user wants the program to fix the password
    import random
    fix = input("Would you like us to fix your password for you? ")
    if fix == "yes":
        # if there is/are invalid character(s) in the password, remove invalid character(s) first
        if invalid_chr > 0:
            for i in invalid_part:
                password = password.replace(i, "")
            print("* New password with invalid characters removed:", password)
        # if the password contains the username, insert a random valid character into the username part
        if username in password:
            username_index = password.find(username)
            place = random.randint(username_index+1, username_index+len(username)-1)
            character = random.choice([random.randint(65, 90), random.randint(97, 122), random.randint(48, 57), random.randint(35, 38)])
            password = password[:place] + chr(character) + password[place:]
            print("* Username is in password - interrupting string to remove it:", password)
            if character >= 65 and character <= 90:
                upper += 1
            elif character >= 97 and character <= 122:
                lower += 1
            elif character >= 48 and character <= 57:
                digit += 1
            elif character >= 35 and character <= 38:
                special_chr += 1
        # if the password doesn't contain uppercase character, add a random uppercase character at a random position
        if upper == 0:
            place = random.randint(0, len(password))
            character = random.randint(65, 90)
            password = password[:place] + chr(character) + password[place:]
            print("* Adding a random uppercase character at a random position:", password)
        # if the password doesn't contain lowercase character, add a random lowercase character at a random position
        if lower == 0:
            place = random.randint(0, len(password))
            character = random.randint(97, 122)
            password = password[:place] + chr(character) + password[place:]
            print("* Adding a random lowercase character at a random position:", password)
        # if the password doesn't contain digit character, add a random digit character at a random position
        if digit == 0:
            place = random.randint(0, len(password))
            character = random.randint(48, 57)
            password = password[:place] + chr(character) + password[place:]
            print("* Adding a random digit character at a random position:", password)
        # if the password doesn't contain special character, add a random special character at a random position
        if special_chr == 0:
            place = random.randint(0, len(password))
            character = random.randint(35, 38)
            password = password[:place] + chr(character) + password[place:]
            print("* Adding a random special character at a random position:", password)
        # if the password is less than 8 characters long, add random valid characters to the password to 8 characters long
        if len(password) < 8:
            for i in range(8-len(password)):
                place = random.randint(0, len(password))
                character = random.choice([random.randint(65, 90), random.randint(97, 122), random.randint(48, 57), random.randint(35, 38)])
                password = password[:place] + chr(character) + password[place:]
            print("* Adding random valid character(s) to be 8 characters long:", password)
        # display the new valid password to the user
        print("Your new password is", password)
