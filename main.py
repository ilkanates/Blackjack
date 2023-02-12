from random import sample
from time import sleep      # import sleep to show output for some time period

# Putting the card names and values in a dictionary allows you to pull their value in a function

card_deck_dct = {"H2": 2, "H3": 3, "H4": 4, "H5": 5, "H6": 6, "H7": 7, "H8": 8, "H9": 9, "H10": 10, "HJ": 10, "HQ": 10, "HK": 10, "HA": 11,
                 "D2": 2, "D3": 3, "D4": 4, "D5": 5, "D6": 6, "D7": 7, "D8": 8, "D9": 9, "D10": 10, "DJ": 10, "DQ": 10, "DK": 10, "DA": 11,
                 "C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7, "C8": 8, "C9": 9, "C10": 10, "CJ": 10, "CQ": 10, "CK": 10, "CA": 11,
                 "S2": 2, "S3": 3, "S4": 4, "S5": 5, "S6": 6, "S7": 7, "S8": 8, "S9": 9, "S10": 10, "SJ": 10, "SQ": 10, "SK": 10, "SA": 11}


# This function takes key and value from the dictionary and creates a card visual

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = '♥♦♣♠'[suit-1]  # 1,2,3,4 = ♥♦♣♠

    def print(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')


# Prints the card visual on the screen

def print_card(card):
    card.print()
    sleep(0.5)
    return


def print_text(text):
    print(f'{text}')
    sleep(0.5)


# Picks a random card from the deck and matching value from the dictionary
# Pops the chosen card from the deck

def deal_card(card_deck, cards, should_print=True):
    card = sample(card_deck, 1)
    card = card[0]
    value = card_deck_dct[card]
    card_index = card_deck.index(card)
    card_deck.pop(card_index)
    shape = int((str(card)[0]).replace("H", "1").replace("D", "2").replace("C", "3").replace("S", "4"))
    number = card[1:]
    card = Card(number, shape)
    cards.append(card)
    if should_print:
        print_card(card)
    return value


# Checks if hand is over 21

def lose_check(hand):
    return hand > 21


# Checks if hand is equal to 21

def win_check(hand):
    return hand == 21


# Changes the value of the player's wallet according to their bet and game outcome

def recalculate_wallet(wallet_value, bet, x):
    if x == "Player wins!":
        wallet_value += bet
    elif x == "Dealer wins" or "Player lose":
        wallet_value -= bet
    else:
        print_text("it's a draw. Wallet value unchanged.")

    print_text(f"You have {wallet_value} dollars in your wallet.")
    return wallet_value


# Error check function - takes input from player and validates it

def ask_bet(wallet_value):
    while True:
        player_bet = input(f"Please enter bet. Your max allowed bet is {wallet_value} dollars ")
        if player_bet.isdigit() and int(player_bet) in range(1, wallet_value + 1):
            player_bet = int(player_bet)
            break
    return player_bet


def win_lose_check(bet, player_cards, player_hand, wallet_value):
    status = ""
    if lose_check(player_hand):
        for card in player_cards:
            if card.value == 'A':
                player_hand = player_hand - 10
                print_text(f"After recalculation you have {player_hand} points")
                break

    if win_check(player_hand):
        status = "Player wins!"
        print_text(status)
        wallet_value = recalculate_wallet(wallet_value, bet, status)
    elif lose_check(player_hand):
        status = "Player lose"
        print_text(status)
        wallet_value = recalculate_wallet(wallet_value, bet, status)
    return player_hand, wallet_value, status


def dealers_turn(card_deck, dealer_cards, dealer_hand, player_hand, status):
    while dealer_hand <= 16:
        print_text("Dealer received")
        card_value = deal_card(card_deck, dealer_cards)
        dealer_hand += card_value
        print_text(f"Dealer has {dealer_hand} points")
        if lose_check(dealer_hand):
            status = "Player wins!"
            break
        elif win_check(dealer_hand) or dealer_hand > player_hand:
            status = "Dealer wins"
            break
    return dealer_hand, status


# The Game

def blackjack():
    wallet_value = 100

    while True:
        card_deck = list(card_deck_dct.keys())
        if wallet_value == 0:
            print_text("You lose")
            exit()
        play_game = input("Are you ready to play? Y/N? ").lower()

        if play_game == "y":
            print_text(f"You have {wallet_value} dollars in your wallet.")

            bet = int(ask_bet(wallet_value))
            player_hand = 0
            dealer_hand = 0
            player_cards = []
            dealer_cards = []
            status = ""

            print_text("You received")
            card_value = deal_card(card_deck, player_cards)
            player_hand += card_value
            card_value = deal_card(card_deck, player_cards)
            player_hand += card_value
            print_text(f"You have {player_hand} points")

            print_text("Dealer has")
            card_value = deal_card(card_deck, dealer_cards)
            dealer_hand += card_value
            card_value = deal_card(card_deck, dealer_cards, False)
            dealer_hand += card_value

            if win_check(player_hand):
                status = "Player wins!"
                print_text(status)
                wallet_value = recalculate_wallet(wallet_value, 1.5 * bet, status)
                continue

            while True:
                new_card = input("Do you want another card? Y/N ")
                if new_card.lower() == "y":
                    print_text("You received")
                    card_value = deal_card(card_deck, player_cards)
                    player_hand += card_value
                    print_text(f"You have {player_hand} points")

                    player_hand, wallet_value, status = win_lose_check(bet, player_cards, player_hand, wallet_value)
                    if status != "":
                        break
                elif new_card.lower() == "n":
                    print_text("Dealers turn")
                    print_text("Dealer received")
                    print_card(dealer_cards[0])
                    print_card(dealer_cards[1])
                    print_text(f"Dealer has {dealer_hand} points")

                    status = ""
                    if dealer_hand > player_hand or win_check(dealer_hand):
                        status = "Dealer wins"

                    if status == "":
                        dealer_hand, status = dealers_turn(card_deck, dealer_cards, dealer_hand, player_hand, status)

                    if status == "Dealer wins":
                        print_text(status)
                        wallet_value = recalculate_wallet(wallet_value, bet, status)
                        sleep(0.5)
                        break
                    elif status == "Player wins!" or dealer_hand < player_hand:
                        status = "Player wins!"
                        print_text(status)
                        wallet_value = recalculate_wallet(wallet_value, bet, status)
                        sleep(0.5)
                        break
                    elif dealer_hand == player_hand:
                        status = "Draw"
                        print_text(status)
                        break

        elif play_game == "n":
            print_text("Bye")
            break


blackjack()
