''' WElcome to Our blackjack game
The deck is unlimited in size
There are no jokers
The Ace can count as 11 or 1
Jack/Queen/King all count as 10
The cards in the list have equal opportunity of being drawn
Cards are not removed from the deck as they are drawn
'''
import random
from art import logo
import os
import platform

def clear_terminal():
    # Check the operating system
    os_name = platform.system()
    if os_name == "Windows":
        # Windows
        os.system('cls')
    else:
        # Linux and Mac
        os.system('clear')
# This function will return a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# This function will check the score of the user and the computer
# If both of the scores are valid (not over 21 and not below 17) then compare
# Else if one of the players has a score > 21 then that one loses
def check_score(user, comp):
    # check if user or computer has won with a blackjack
    if (user == comp) and (user < 21):
        print("It's a tie 🪢")

    elif user == 0:
        print("You won with a blackjack :D The computer lost")

    elif comp == 0:
        print("The computer won with a blackjack!! You lost :(")

    # check for user's score in invalid range
    elif user < 17 or user > 21:
        print("You lost due to invalid score :(")
    # check for computer's score in invalid range
    elif comp > 21:
        print("The computer lost due to invalid score, you're the winner :D")

    # if the user's score and computer's score are in valid range, no blackjack, no tie
    else:
        if user > comp:
            print("You win 😃")
        else:
            print("You lost 😔")

    return


# This function will calculate the score of the user and the computer
def calculate_score(cards):
    # A hand with only 2 cards: an ace and 10 is a blackjack
    # Then return 0
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    
    # If the hand contains an 11 and the sum is greater than 21, replace the 11 with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# check if the game should be over
def is_game_over(user_score, comp_score):
    if user_score == 0 or comp_score == 0 or user_score > 21:
        return True
    return False


#finalize the game
def final(user_cards, user_score, comp_cards, comp_score):
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    check_score(user_score, comp_score)
    return


def play_game():
    # if the user wants to play, start the game
    print(logo)
    # deal 2 cards for the user and the computer
    user_cards = []
    comp_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)

    # if the user or the computer has a blackjack, the game is over, or if the user's score is over 21
    if is_game_over(user_score, comp_score):
        final(user_cards, user_score, comp_cards, comp_score)
        return


    # if the game is not over, print the user's cards and the computer's first card
    print(f"Your cards: {user_cards}, current score:{user_score}")
    print(f"Computer's first card: {comp_cards[0]}")

    # if the computer's score is less than 17, the computer will get another card
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    # ask if the user wants to get another card
    game_over = False
    while not game_over:
        print("Want to get another card? y/n: ")
        get_card = input()

        #if the user doesn't want to get another card, the game is over
        if get_card == "n":
            final(user_cards, user_score, comp_cards, comp_score)
            game_over = True

        # if the user wants to get another card, get another card
        else:
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            # after each time the user gets a card, check if the game is over
            if is_game_over(user_score, comp_score):
                final(user_cards, user_score, comp_cards, comp_score)
                game_over = True
            # if the game is not over, print the user's cards and keep asking if the user wants to get another card
            else:
                print(f"Your cards: {user_cards}, current score:{user_score}")

# the game will continue until the user decides to stop
while input("Do you want to play BlackJack? y or n: ") == "y":  
    clear_terminal()
    play_game()
    


    