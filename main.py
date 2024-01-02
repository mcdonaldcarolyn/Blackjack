import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main(): 
    print(''' Rules: try to get as close to 21 as you can''')
    money = 5000
    while True:
        if money <= 0:
            print("You are broke")
            print("Thanks for playing")
        print('Money:', money)
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), ]