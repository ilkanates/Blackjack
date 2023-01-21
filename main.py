from random import sample
from time import sleep      # import sleep to show output for some time period

# Putting the card names and values in a dictionary allows you to pull their value in a function

card_deck_dct = {"H2": 2, "H3": 3, "H4": 4, "H5": 5, "H6": 6, "H7": 7, "H8": 8, "H9": 9, "H10": 10, "HJ": 10, "HQ": 10,
                 "HK": 10, "HA": 11
    , "D2": 2, "D3": 3, "D4": 4, "D5": 5, "D6": 6, "D7": 7, "D8": 8, "D9": 9, "D10": 10, "DJ": 10, "DQ": 10, "DK": 10,
                 "DA": 11
    , "C2": 2, "C3": 3, "C4": 4, "C5": 5, "C6": 6, "C7": 7, "C8": 8, "C9": 9, "C10": 10, "CJ": 10, "CQ": 10, "CK": 10,
                 "CA": 11
    , "S2": 2, "S3": 3, "S4": 4, "S5": 5, "S6": 6, "S7": 7, "S8": 8, "S9": 9, "S10": 10, "SJ": 10, "SQ": 10, "SK": 10,
                 "SA": 11}

# This function takes key and value from the dictionary and creates a card visual

class Card:
    def __init__(self,valuec,suit):
        self.valuec = valuec
        self.suit = '♥♦♣♠'[suit-1] # 1,2,3,4 = ♥♦♣♠

    def print(self):
        print('┌───────┐')
        print(f'| {self.valuec:<2}    |')
        print('|       |')
        print(f'|  {self.suit}   |')
        print('|       |')
        print(f'|    {self.valuec:>2} |')
        print('└───────┘')

# Prints the card visual on the screen

def print_card(g):
    shape = int((str(g[0])[2]).replace("H","1").replace("D","2").replace("C","3").replace("S","4"))
    number = str(g[0])[3]+str(g[0])[4].replace("'","")
    print_card = Card(number,shape)
    print_card.print()
    return

# Picks a random card from the deck and matching value from the dictionary
# Pops the chosen card from the deck

def dealing(card_deck):
    card = sample(card_deck,1)
    value = card_deck_dct[card[0]]
    card_index = card_deck.index(card[0])
    card_deck.pop(card_index)
    return card,value

# Checks if hand is over 21

def lose_check(hand):
    if hand > 21:
        return True
    else:
        return False

# Checks if hand is equal to 21

def win_check(hand):
    if hand == 21:
        return True
    else:
        return False


# Changes the value of the player's wallet according to their bet and game outcome

def wallet(wallet_value, bet, x):
    if x == "Player wins!":
        wallet_value += bet
    elif x == "Dealer wins" or "Player lose":
        wallet_value -= bet
    else:
        print("it's a draw. Wallet value unchanged.")

    print(f"You have {wallet_value} dollars in your wallet.")
    return wallet_value

# Error check function - takes input from player and validates it

def bet_f(wallet_value):
    while True:
        try:
            player_bet = input(f"Please enter bet. Your max bet allowed is  {wallet_value} dollars ")
            player_bet = int(player_bet)
        except ValueError:
            continue
        else:
            while not int(player_bet) in range(1,((wallet_value)+1)):
                player_bet = input(f"Please enter bet. Your max bet allowed is  {wallet_value} dollars ")
            break
    return player_bet


def blackjack():
    wallet_value = 100

    while True:
        card_deck = list(card_deck_dct.keys())
        play_game = input("Are you ready to play? Y/N? ")

        if play_game.lower() == "y":
            print(f"You have {wallet_value} dollars in your wallet.")
            bet = int(bet_f(wallet_value))
            player_hand = 0
            dealer_hand = 0
            player_cards = []
            x = ""
            a = dealing(card_deck)
            sleep(0.5)
            b = dealing(card_deck)
            sleep(0.5)
            c = dealing(card_deck)
            sleep(0.5)
            d = dealing(card_deck)
            player_cards.append(a[1])
            player_cards.append(b[1])
            player_hand = a[1] + b[1]
            dealer_hand = c[1] + d[1]
            print(f"You received")
            sleep(0.5)
            print_card(a)
            sleep(0.5)
            print_card(b)
            sleep(0.5)
            print(f"You have {player_hand} points")
            sleep(0.5)
            print(f"Dealer has")
            sleep(0.5)
            print_card(c)
            sleep(0.5)

            if win_check(player_hand) == True:
                x = "Player wins!"
                print(x)
                wallet_value = wallet(wallet_value, bet, x)
                continue
            else:
                while win_check(player_hand) == False:
                    if x != "":
                        break
                    elif x == "":
                        new_card = input("Do you want another card? Y/N ")
                        if new_card.lower() == "y":
                            e = dealing(card_deck)
                            player_cards.append(e[1])
                            player_hand += e[1]
                            print(f"You received")
                            sleep(0.5)
                            print_card(e)
                            print(f"You have {player_hand} points")
                            sleep(0.5)
                            if win_check(player_hand) == True:
                                x = "Player wins!"
                                print(x)
                                wallet_value = wallet(wallet_value, bet, x)
                                sleep(0.5)
                                break
                            elif lose_check(player_hand) == True and player_cards.count(11) > 0:
                                player_cards.pop(player_cards.index(11))
                                player_cards.append(1)
                                player_hand = player_hand - 10
                                print(f"After recallulation you have {player_hand} points")
                                sleep(0.5)
                                if lose_check(player_hand) == True:
                                    x = "Player lose"
                                    print(x)
                                    wallet_value = wallet(wallet_value, bet, x)
                                    sleep(0.5)
                                else:
                                    continue
                            elif lose_check(player_hand) == True and player_cards.count(11) > 0:
                                player_cards.pop(player_cards.index(11))
                                player_cards.append(1)
                                player_hand = player_hand - 10
                                print(f"After recallulation you have {player_hand} points")
                                sleep(0.5)
                                if lose_check(player_hand) == True:
                                    x = "Player lose"
                                    print(x)
                                    wallet_value = wallet(wallet_value, bet, x)
                                    sleep(0.5)
                                elif win_check(player_hand) == True:
                                    x = "Player wins!"
                                    print(x)
                                    wallet_value = wallet(wallet_value, bet, x)
                                    sleep(0.5)
                                    break
                                else:
                                    continue
                            elif lose_check(player_hand) == True:
                                x = "Player lose"
                                print(x)
                                wallet_value = wallet(wallet_value, bet, x)
                                sleep(0.5)
                                break
                            else:
                                continue

                        elif new_card.lower() == "n":
                            print("Dealers turn")
                            sleep(0.5)
                            print(f"Dealer received")
                            sleep(0.5)
                            print_card(c)
                            sleep(0.5)
                            print_card(d)
                            sleep(0.5)
                            print(f"Dealer has {dealer_hand} points")
                            sleep(0.5)
                            if (dealer_hand > player_hand) or (win_check(dealer_hand) == True):
                                x = "Dealer wins"
                                print(x)
                                wallet_value = wallet(wallet_value, bet, x)
                                sleep(0.5)
                                break

                            elif dealer_hand > 16 and dealer_hand < player_hand:
                                x = "Player wins!"
                                print(x)
                                wallet_value = wallet(wallet_value, bet, x)
                                sleep(0.5)
                                break

                            elif dealer_hand == player_hand and dealer_hand > 16:
                                x = "Draw"
                                print(x)
                                sleep(0.5)
                                break

                            else:
                                while dealer_hand <= 16:
                                    f = dealing(card_deck)
                                    dealer_hand += f[1]
                                    print(f"Dealer received")
                                    sleep(0.5)
                                    print_card(f)
                                    sleep(0.5)
                                    print(f"Dealer has {dealer_hand} points")
                                    sleep(0.5)
                                    if win_check(dealer_hand) == True:
                                        x = "Dealer wins"
                                        print(x)
                                        wallet_value = wallet(wallet_value, bet, x)
                                        sleep(0.5)
                                        break
                                    elif lose_check(dealer_hand) == True:
                                        x = "Player wins!"
                                        print(x)
                                        wallet_value = wallet(wallet_value, bet, x)
                                        sleep(0.5)
                                        game_on = False
                                        break
                                    elif dealer_hand > player_hand:
                                        x = "Dealer wins"
                                        print(x)
                                        wallet_value = wallet(wallet_value, bet, x)
                                        sleep(0.5)
                                        break
                                    elif dealer_hand == player_hand and dealer_hand > 16:
                                        x = "Draw"
                                        print(x)
                                        sleep(0.5)
                                        break
                                    elif player_hand > dealer_hand and dealer_hand > 16:
                                        x = "Player wins!"
                                        print(x)
                                        wallet_value = wallet(wallet_value, bet, x)
                                        sleep(0.5)

                                        break
                                    else:
                                        continue
                    else:
                        break
        elif play_game.lower() == "n":
            print("Bye")
            sleep(0.5)
            break
        else:
            continue

blackjack()

