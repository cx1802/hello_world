"""
Peidi Xie
April 14th, 2019
Introduction to Programming, Section 03
Part 1b
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
        print("Username is valid!")
        break
    else:
        print("Username is invalid, please try again")
        print()

'''
Part1b
'''

# ask the user to enter a password.
# if the password doesn't comply to the rules, prompt the user to enter again until valid data is supplied
print()
while True:
    password = input("Enter a password: ")
    # display the length of the password
    print("* Length of password:", len(password))
    # a valid password should be at least 8 characters long
    if len(password) >= 8:
        checker1 = True
    else:
        checker1 = False
    # display whether the password contains the username
    print("* Username is part of password", username in password)
    # a valid password should not contains the username
    checker2 = not (username in password)
    # keep track of the numbers of uppercase, lowercase, numeric, and a selection of special characters in the password
    upper = 0
    lower = 0
    digit = 0
    special_chr = 0
    for i in password:
        if ord(i) >= 65 and ord(i) <= 90:
            upper += 1
        if ord(i) >= 97 and ord(i) <= 122:
            lower += 1
        if ord(i) >= 48 and ord(i) <= 57:
            digit += 1
        if ord(i) >= 35 and ord(i) <= 38:
            special_chr += 1
    # display the numbers of uppercase, lowercase, numeric, and special characters in the password
    print("* # of uppercase characters in the password:", upper)
    print("* # of lowercase characters in the password:", lower)
    print("* # of digits in the password:", digit)
    print("* # of special characters in the password:", special_chr)
    # a valid password should have at least one uppercase character, one lowercase character, one numeric character, and one special character
    checker4 = upper >= 1 and lower >= 1 and digit >= 1 and special_chr >= 1
    # check if the password complies to all rules and tell the user the password is valid or not
    checker = checker1 and checker2 and checker3 and checker4
    if checker:
        print("Password is valid!")
        break
    else:
        print("Password is invalid, please try again")
        print()
