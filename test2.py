import random
from time import sleep

card_deck_dct = {
    "H2": 2, "H3": 3, "H4": 4, "H5": 5, "H6": 6, "H7": 7, "H8": 8, "H9": 9, "H10": 10, "HJ": 10, "HQ": 10, "HK": 10,
    "HA": 11,
    "D2": 2, "D3": 3, "D4": 4, "D5": 5, "D6": 6, "D7": 7, "D8": 8, "D9": 9, "D10": 10, "DJ": 10, "DQ": 10, "DK": 10,
    "DA": 11,
    "C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7, "C8": 8, "C9": 9, "C10": 10, "CJ": 10, "CQ": 10, "CK": 10,
    "CA": 11,
    "S2": 2, "S3": 3, "S4": 4, "S5": 5, "S6": 6, "S7": 7, "S8": 8, "S9": 9, "S10": 10, "SJ": 10, "SQ": 10, "SK": 10,
    "SA": 11,
}


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = '♥♦♣♠'[suit-1]  # 1,2,3,4 = ♥♦♣♠

    def __str__(self):
        return f'┌───────┐\n| {self.value:<2}    |\n|       |\n|  {self.suit}   |\n|       |\n|    {self.value:>2} |\n└───────┘'

card = Card("A", 2)
print(card)


def deal_card(card_deck, cards):
    card = random.choice(card_deck)
    value = card_deck_dct[card]
    card_deck.remove(card)
    cards.append(value)
    return card, value


def lose_check(hand):
    return hand > 21


def win_check(hand):
    return hand == 21


def update_wallet(wallet_value, bet, outcome):
    if outcome == "Player wins!":
        wallet_value += bet
    elif outcome in ("Dealer wins", "Player lose"):
        wallet_value -= bet
    else:
        print("It's a draw. Wallet value unchanged.")

    print(f"You have {wallet_value} dollars in your wallet.")
    return wallet_value

def ask_bet(chips):
    while True:
        try:
            bet = int(input("Place your bet (chips): "))
            if bet > chips:
                print("You don't have enough chips. Enter a valid amount.")
            elif bet <= 0:
                print("Bet must be greater than 0. Enter a valid amount.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Enter an integer.")

def win_lose_check(bet, player_cards, player_hand, wallet_value):
    status = ""
    if win_check(player_hand):
        status = "Player wins!"
        print(status)
        wallet_value = update_wallet(wallet_value, bet, status)
    elif lose_check(player_hand) and player_cards.count(11) > 0:
        player_cards.pop(player_cards.index(11))
        player_cards.append(1)
        player_hand = player_hand - 10
        print(f"After recalculation you have {player_hand} points")
        if lose_check(player_hand):
            status = "Player lose"
            print(status)
            wallet_value = update_wallet(wallet_value, bet, status)
        else:
            status = "Player wins!"
            print(status)
            wallet_value = update_wallet(wallet_value, bet, status)
    elif lose_check(player_hand):
        status = "Player lose"
        print(status)
        wallet_value = update_wallet(wallet_value, bet, status)
    elif player_hand < 21:
        status = "Continue playing."
        print(status)
    return player_hand, wallet_value, status

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
            print(a[0])
            player_hand += a[1]
            b = deal_card(card_deck, player_cards)
            player_hand += b[1]
            print(b[0])
            print(f"You have {player_hand} points")
            sleep(0.5)

            print(f"Dealer has")
            sleep(0.5)
            c = deal_card(card_deck, dealer_cards)
            print(c[0])
            dealer_hand += c[1]
            d = deal_card(card_deck, dealer_cards)
            dealer_hand += d[1]

            if win_check(player_hand):
                status = "Player wins!"
                print(status)
                wallet_value = update_wallet(wallet_value, bet, status)
                continue

            while True:
                new_card = input("Do you want another card? Y/N ")
                if new_card.lower() == "y":
                    e = deal_card(card_deck, player_cards)
                    player_hand += e[1]
                    print(f"You received")
                    sleep(0.5)
                    print(e[0])
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
                    print(c[0])
                    sleep(0.5)
                    print(d[0])
                    sleep(0.5)
                    print(f"Dealer has {dealer_hand} points")
                    sleep(0.5)

                    if dealer_hand > player_hand or win_check(dealer_hand):
                        status = "Dealer wins"
                        print(status)
                        wallet_value = update_wallet(wallet_value, bet, status)
                        sleep(0.5)
                        break

                    status = ""
                    while dealer_hand <= 16:
                        f = deal_card(card_deck, dealer_cards)
                        dealer_hand += f[1]
                        print(f"Dealer received a {f[0]} and has {dealer_hand} points")
                        sleep(0.5)
                        if lose_check(dealer_hand):
                            status = "Player wins!"
                            print(status)
                            wallet_value = update_wallet(wallet_value, bet, status)
                            sleep(0.5)
                            break
                        elif win_check(dealer_hand) or dealer_hand > player_hand:
                            status = "Dealer wins"
                            print(status)
                            wallet_value = update_wallet(wallet_value, bet, status)
                            sleep(0.5)
                            break

                    if status != "":
                        break

                    if dealer_hand < player_hand:
                        status = "Player wins!"
                        print(status)
                        wallet_value = update_wallet(wallet_value, bet, status)
                        sleep(0.5)
                        break
                    elif dealer_hand == player_hand:
                        status = "Draw"
                        print(status)
                        sleep(0.5)
                        break
blackjack()
