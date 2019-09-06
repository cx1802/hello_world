"""
Peidi Xie
April 14th, 2019
Introduction to Programming, Section 03
Part 2b
"""

def add_letters(word, num):
    import random
    new_word = ""
    for i in word:
        letter = ""
        for j in range(num):
            letter += chr(random.choice([random.randint(65, 90), random.randint(97, 122)]))
        new_word += i + letter
    return new_word

def remove_letters(word, num):
    new_word = word[::num+1]
    return new_word

def shift_characters(word, num):
    new_word = ""
    for i in word:
        letter = chr(ord(i)+num)
        new_word += letter
    return new_word

# ask the user for an option of encoding, decoding, or quit
# continually prompt the user to enter an option until the user enters quit
while True:
    option = input("(e)ncode, (d)ecode or (q)uit: ")
    if option == "e":
        # ask the user to enter a positive number between 1 and 5 and a phrase to encode
        num = int(input("Enter a number between 1 and 5: "))
        # if the number is not within the range, prompt the user to enter again until valid data is supplied
        while num < 1 or num > 5:
            print("Invalid entry, please try again")
            num = int(input("Enter a number between 1 and 5: "))
        word = input("Enter a phrase to encode: ")
        # encode the phrase by applying add_letters function first and then shift_characters function
        encoded_word = shift_characters(add_letters(word, num), num)
        # display the encoded phrase to the user
        print("Your encoded word is:", encoded_word)
    if option == "d":
        # ask the user to enter a positive number between 1 and 5 and a phrase to decode
        num = int(input("Enter a number between 1 and 5: "))
        # if the number is not within the range, prompt the user to enter again until valid data is supplied
        while num < 1 or num > 5:
            print("Invalid entry, please try again")
            num = int(input("Enter a number between 1 and 5: "))
        word = input("Enter a phrase to decode: ")
        # decode the phrase by applying remove_letters function first and then shift_characters function
        decoded_word = shift_characters(remove_letters(word, num), -num)
        # display the decoded phrase to the user
        print("Your decoded word is:", decoded_word)
    if option == "q":
        break
    print()
