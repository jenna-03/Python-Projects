

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
BLACKJACK = 21
DEALER_THRESHOLD = 16


####### DO NOT EDIT ABOVE ########
def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple
    :return: a single- or double-character string representing a playing card
    >>> random.seed(13)
    >>> deal_card()
    '5'
    >>> deal_card()
    '5'
    >>> deal_card()
    'J'
    """

    return random.choice(CARD_LABELS)


def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)
    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value
    >>> card_label = 'A'
    >>> get_card_value(card_label)
    1
    >>> card_label = 'K'
    >>> get_card_value(card_label)
    10
    >>> card_label = '5'
    >>> get_card_value(card_label)
    5
    """

    if card_label == "A":
        return ACE_VALUE
    elif card_label in "JQK":
        return FACE_CARD_VALUE
    else:
        return int(card_label)


def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total
    :return: the total value of the cards dealt
    """

    player_card1 = deal_card()
    player_card2 = deal_card()

    total = get_card_value(player_card1) + get_card_value(player_card2)
    print("Player drew", player_card1, "and", player_card2 + ".")
    print("Player's total is", str(total) + '.')
    print()

    game = True

    while game == True:
        prompt = input("Hit (h) or Stay (s)?")
        print()
        if prompt == 'h':
            player_card3 = deal_card()
            total += get_card_value(player_card3)
            print("Player drew", player_card3 + '.')
            print("Player's total is", str(total) + '.')
            print()
        if prompt == 's':
            game = False
        if total >= BLACKJACK:
            game = False


    return int(total)

def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total
    :return: the total value of the cards dealt
    """
    deal_card1 = deal_card()
    deal_card2 = deal_card()
    total = get_card_value(deal_card1) + get_card_value(deal_card2)

    print("The dealer has", deal_card1, "and", deal_card2 + ".")
    print("Dealer's total is", str(total) + '.')
    print()

    while total <= DEALER_THRESHOLD:
        card3 = deal_card()
        total += get_card_value(card3)
        print("Dealer drew", str(card3) + '.')
        print("Dealer's total is", str(total) + '.')
        print()

    return int(total)


def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.
    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """
    if player_total == dealer_total:
        print("YOU LOSE!")
        print()
    elif player_total == BLACKJACK and dealer_total == BLACKJACK:
        print("YOU LOSE!")
        print()
    elif dealer_total > BLACKJACK:
        print("YOU WIN!")
        print()
    elif player_total > BLACKJACK >= dealer_total:
        print("YOU LOSE!")
        print()
    elif player_total > dealer_total:
        print("YOU WIN!")
        print()
    elif player_total < dealer_total:
        print("YOU LOSE!")
        print()








def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome
    :return: None
    """
    print("Let's Play Blackjack!")
    print()
    player_card = deal_cards_to_player()

    if player_card > BLACKJACK:
        dealer_card = BLACKJACK
    else:
        dealer_card = deal_cards_to_dealer()

    determine_outcome(player_card, dealer_card)

    prompt = input("Play again (Y/N)? ")
    print()

    game = True
    while game == True:
        if prompt == "Y":
            player_card = deal_cards_to_player()

            if player_card > BLACKJACK:
                dealer_card = BLACKJACK
            else:
                dealer_card = deal_cards_to_dealer()

            determine_outcome(player_card, dealer_card)
            prompt = input("Play again (Y/N)? ")
        elif prompt == "N":
            game = False
        else:
            prompt = input("Play again (Y/N)? ")
            print()

    print("Goodbye.")


def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    # call play_blackjack() here and remove pass below
    play_blackjack()

####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    #Remove comments for next 4 lines to run doctests
    #print("Running doctests...")
    #import doctest
    #doctest.testmod(verbose=True)

    #print("\nRunning program...\n")

    main()
