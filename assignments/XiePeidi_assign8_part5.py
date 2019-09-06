"""
Peidi Xie
April 28th, 2019
Introduction to Programming, Section 03
Part 5: extra credit
"""

# the lists of deck of cards and the corresponding values of the cards for game of Blackjack
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

# the "bank" of money the user maintains to bet during the playing of game
player_money = 25

import random

# the user can keep playing as long as there is money in his bank
while player_money > 0:
    # deal two cards at random to the player when game starts.
    # store the user's cards and values in separate lists and report to the user
    player_cards = random.sample(cards, 2)
    player_values = [values[cards.index(player_cards[0])], values[cards.index(player_cards[1])]]
    print("Player hand:", player_cards, "is worth", sum(player_values))
    # remove the two cards and the two values from the lists
    for i in range(len(player_cards)):
        del values[cards.index(player_cards[i])]
        cards.remove(player_cards[i])
    while True:
        # keep asking the user if he wants to "hit" or "stand" when the game is not over
        player_choice = input("(h)it or (s)tand? ")
        # if the user chooses "hit", deal him another card and store the card and the value
        # report to the user every time he gets a new card
        if player_choice == "h":
            p_card = random.choice(cards)
            player_cards.append(p_card)
            player_values.append(values[cards.index(p_card)])
            print("You drew", p_card)
            print("Player hand:", player_cards, "is worth", sum(player_values))
            # remove the card and the value from the lists
            del values[cards.index(p_card)]
            cards.remove(p_card)
        # if the user chooses "stand", deal two cards to the computer
        # store the computer's cards and values in separate lists and report 
        elif player_choice == "s":
            print()
            computer_cards = random.sample(cards, 2)
            computer_values = [values[cards.index(computer_cards[0])], values[cards.index(computer_cards[1])]]
            print("Computer hand:", computer_cards, "is worth", sum(computer_values))
            # remove the two cards and the two values from the lists
            for i in range(len(computer_cards)):
                del values[cards.index(computer_cards[i])]
                cards.remove(computer_cards[i])
            # keep dealing the computer one card at a time until meeting certain conditions
            # store the card and the value, report, and remove the card and the value from the lists
            while sum(computer_values) <= sum(player_values):
                c_card = random.choice(cards)
                computer_cards.append(c_card)
                computer_values.append(values[cards.index(c_card)])
                print("Computer drew", c_card)
                print("Computer hand:", computer_cards, "is worth", sum(computer_values))
                del values[cards.index(c_card)]
                cards.remove(c_card)
                # when the computer gets exactly 21 points the computer wins
                # stop dealing card, report, and cost 5 dollars bet from the user's "bank"
                if sum(computer_values) == 21:
                    print("Computer got 21! Blackjack!")
                    print("Computer wins!")
                    print()
                    player_money -= 5
                    break
                # when the computer gets over 21 points the computer loses
                # stop dealing card, report "bust", and add 5 dollars bet to the user's bank
                elif sum(computer_values) > 21:
                    print("Bust!")
                    print("Player wins!")
                    print()
                    player_money += 5
                    break
            # if the computer earns greater point than the user and doesn't go "bust", the computer wins
            # end this round of the game, report, and cost 5 dollars bet from the user's "bank"
            if sum(computer_values) > sum(player_values) and sum(computer_values) < 21:
                print("Computer wins!")
                print()
                player_money -= 5
            break
        # if the user continuously "hits" and gets over 21 points, the user loses
        # end this round of the game, report, and cost 5 dollars bet from the user's "bank"
        if sum(player_values) > 21:
            print("Bust!")
            print("Computer wins!")
            print()
            player_money -= 5
            break
        # if the user continuously "hits" and gets exactly 21 points, the user wins
        # end this round of the game, report, and add 5 dollars bet to the user's "bank"
        elif sum(player_values) == 21:
            print("Player got 21! Blackjack!")
            print("Player wins!")
            print()
            player_money += 5
            break
        

        
