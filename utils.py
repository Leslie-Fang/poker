import os
import itertools
import copy

def print_all_cards(cards):
    print("start to print cards", flush=True)
    for card in cards:
        print("number is: {}; color is: {}".format(card.number, card.color), flush=True)
    return

def remove_hand_card(remain_cards, hand_card):
    """
    Revome hand_card from remain_cards
    """
    for card in [hand_card.card1, hand_card.card2]:
        for remain_card in remain_cards:
            if card.number == remain_card.number and card.color == remain_card.color:
                remain_cards.remove(remain_card)
    return remain_cards

def remove_public_card(remain_cards, public_card):
    """
    Revome public_card from remain_cards
    """
    for remain_card in remain_cards:
        if public_card.number == remain_card.number and public_card.color == remain_card.color:
            remain_cards.remove(remain_card)
    return remain_cards

def _is_four_of_a_kind(cards):
    assert cards.__len__() == 4
    number = cards[0].number
    for card in cards:
        if card.number != number:
            return False
    return True

def _is_three_of_a_kind(cards):
    assert cards.__len__() == 3
    number = cards[0].number
    for card in cards:
        if card.number != number:
            return False
    return True

def _is_two_of_a_kind(cards):
    assert cards.__len__() == 2
    number = cards[0].number
    for card in cards:
        if card.number != number:
            return False
    return True

def _is_flush(cards):
    assert cards.__len__() == 5
    color = cards[0].color
    for card in cards:
        if card.color != color:
            return False
    return True

def _is_straight(cards):
    assert cards.__len__() == 5
    cards = copy.deepcopy(list(cards))
    cards.sort(key=lambda card: card.number, reverse=True)
    if cards[0].number == 14 and cards[1].number == 5:
        if cards[2].number != 4:
            return False
        if cards[3].number != 3:
            return False
        if cards[4].number != 2:
            return False
        return True

    if (cards[0].number - cards[1].number != 1):
        return False
    if (cards[1].number - cards[2].number != 1):
        return False
    if (cards[2].number - cards[3].number != 1):
        return False
    if (cards[3].number - cards[4].number != 1):
        return False
    return True

def is_three_of_a_kind():
    pass

def is_two_pair():
    pass

def is_one_pair():
    pass

