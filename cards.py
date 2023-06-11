import os
from enum import Enum

class CardColor(Enum):
    heart = 1
    spade = 2
    club = 3
    diamond = 4

class Card:
    def __init__(self, number, color: CardColor):
        self.number = number
        self.color = color


class HandCard:
    def __init__(self, card1: Card, card2: Card):
        self.card1 = card1
        self.card2 = card2

all_cards = []

for number in range(2, 15):
    for color in [CardColor.heart, CardColor.spade, CardColor.club, CardColor.diamond]:
        print("number is: {}; color is: {}".format(number, color))
        all_cards.append(Card(number, color))


