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
        print(f'|  {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')


# Prints the card visual on the screen

def print_card(g):
    shape = int((str(g)[2]).replace("H", "1").replace("D", "2").replace("C", "3").replace("S", "4"))
    number = str(g)[3]+str(g)[4].replace("'", "")
    card = Card(number, shape)
    card.print()
    sleep(0.5)
    return


# Picks a random card from the deck and matching value from the dictionary
# Pops the chosen card from the deck

def deal_card(card_deck, cards):
    card = sample(card_deck, 1)
    value = card_deck_dct[card[0]]
    card_index = card_deck.index(card[0])
    card_deck.pop(card_index)
    cards.append(value)
    return card, value


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
        print("it's a draw. Wallet value unchanged.")

    print(f"You have {wallet_value} dollars in your wallet.")
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
    status = "";
    if win_check(player_hand):
        status = "Player wins!"
        print(status)
        wallet_value = recalculate_wallet(wallet_value, bet, status)
        sleep(0.5)
    elif lose_check(player_hand) and player_cards.count(11) > 0:
        player_cards.pop(player_cards.index(11))
        player_cards.append(1)
        player_hand = player_hand - 10
        print(f"After recalculation you have {player_hand} points")
        sleep(0.5)
        if lose_check(player_hand):
            status = "Player lose"
            print(status)
            wallet_value = recalculate_wallet(wallet_value, bet, status)
            sleep(0.5)
        elif win_check(player_hand):
            status = "Player wins!"
            print(status)
            wallet_value = recalculate_wallet(wallet_value, bet, status)
            sleep(0.5)
    elif lose_check(player_hand):
        status = "Player lose"
        print(status)
        wallet_value = recalculate_wallet(wallet_value, bet, status)
        sleep(0.5)
    return player_hand, wallet_value, status


# The Game

def blackjack():
    wallet_value = 100

    while True:
        card_deck = list(card_deck_dct.keys())
        play_game = input("Are you ready to play? Y/N? ").lower()

        if play_game == "y":
            print(f"You have {wallet_value} dollars in your wallet.")
            bet = int(ask_bet(wallet_value))
            player_hand = 0
            dealer_hand = 0
            player_cards = []
            dealer_cards = []
            status = ""
            print(f"You received")
            sleep(0.5)
            a = deal_card(card_deck, player_cards)
            print_card(a[0])
            player_hand += a[1]
            b = deal_card(card_deck, player_cards)
            player_hand += b[1]
            print_card(b[0])
            print(f"You have {player_hand} points")
            sleep(0.5)

            print(f"Dealer has")
            sleep(0.5)
            c = deal_card(card_deck, dealer_cards)
            print_card(c[0])
            dealer_hand += c[1]
            d = deal_card(card_deck, dealer_cards)
            dealer_hand += d[1]

            if win_check(player_hand):
                status = "Player wins!"
                print(status)
                wallet_value = recalculate_wallet(wallet_value, bet, status)
                continue

            while True:
                new_card = input("Do you want another card? Y/N ")
                if new_card.lower() == "y":
                    e = deal_card(card_deck, player_cards)
                    player_hand += e[1]
                    print(f"You received")
                    sleep(0.5)
                    print_card(e[0])
                    print(f"You have {player_hand} points")
                    sleep(0.5)

                    player_hand, wallet_value, status = win_lose_check(bet, player_cards, player_hand, wallet_value)
                    if status != "":
                        break
                elif new_card.lower() == "n":
                    print("Dealers turn")
                    sleep(0.5)
                    print(f"Dealer received")
                    sleep(0.5)
                    print_card(c[0])
                    sleep(0.5)
                    print_card(d[0])
                    sleep(0.5)
                    print(f"Dealer has {dealer_hand} points")
                    sleep(0.5)

                    if dealer_hand > player_hand or win_check(dealer_hand):
                        status = "Dealer wins"
                        print(status)
                        wallet_value = recalculate_wallet(wallet_value, bet, status)
                        sleep(0.5)
                        break

                    status = ""
                    while dealer_hand <= 16:
                        f = deal_card(card_deck, dealer_cards)
                        dealer_hand += f[1]
                        print(f"Dealer received")
                        sleep(0.5)
                        print_card(f[0])
                        print(f"Dealer has {dealer_hand} points")
                        sleep(0.5)
                        if lose_check(dealer_hand):
                            status = "Player wins!"
                            print(status)
                            wallet_value = recalculate_wallet(wallet_value, bet, status)
                            sleep(0.5)
                            break
                        elif win_check(dealer_hand) or dealer_hand > player_hand:
                            status = "Dealer wins"
                            print(status)
                            wallet_value = recalculate_wallet(wallet_value, bet, status)
                            sleep(0.5)
                            break

                    if status != "":
                        break

                    if dealer_hand < player_hand:
                        status = "Player wins!"
                        print(status)
                        wallet_value = recalculate_wallet(wallet_value, bet, status)
                        sleep(0.5)
                        break
                    elif dealer_hand == player_hand:
                        status = "Draw"
                        print(status)
                        sleep(0.5)
                        break

        elif play_game == "n":
            print("Bye")
            sleep(0.5)
            break

blackjack()
