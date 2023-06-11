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

def compare_two_hand(hand_card1, hand_card2, public_cards):
    """
    inputs:
    * hand1
    * hand2
    * public cards

    return:
    * 0 if equal
    * 1 is hand1 is larger
    * 2 is hand2 is larger
    """
    is_hand1_straight_flush = is_straight_flush(hand_card1, public_cards)
    is_hand2_straight_flush = is_straight_flush(hand_card2, public_cards)

    if is_hand1_straight_flush is not None and is_hand2_straight_flush is None:
        return 1
    if is_hand1_straight_flush is None and is_hand2_straight_flush is not None:
        return 2
    if is_hand1_straight_flush is not None and is_hand2_straight_flush is not None:
        if is_hand1_straight_flush[0].number == is_hand2_straight_flush[0].number:
            return 0
        if is_hand1_straight_flush[0].number > is_hand2_straight_flush[0].number:
            return 1
        if is_hand1_straight_flush[0].number < is_hand2_straight_flush[0].number:
            return 2
    # all is not straight_flush
    return 0



def is_straight_flush(hand_card, public_cards):
    """
    同花顺

    return None if is not straight_flush
    else return the largest straight_flush
    """
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    if len(full_cards_to_check) < 5:
        return None
    all_combinations = itertools.combinations(full_cards_to_check, 5)

    # if not any((_is_flush(cards) and _is_straight(cards)) for cards in all_combinations):
    largest_cards = None
    for cards in all_combinations:
        if _is_flush(cards) and _is_straight(cards):
            if largest_cards is None:
                largest_cards = copy.deepcopy(list(cards))
                largest_cards.sort(key = lambda card:card.number, reverse=True)
            else:
                compare_cards = copy.deepcopy(list(cards))
                compare_cards.sort(key = lambda card:card.number, reverse=True)
                if compare_cards[0].number > largest_cards[0].number:
                    largest_cards = compare_cards
    return largest_cards


def _is_four_of_a_kind(cards):
    assert cards.__len__() == 4
    number = cards[0].number
    for card in cards:
        if card.number != number:
            return False
    return True

def is_four_of_a_kind(hand_card, public_cards):
    """
    **TODO** support case when not enough cards input
    return None if not 4 of kind
    elif only 4 cards
        return high card of -1
    else
        return the high card
    """
    assert public_cards.__len__() == 5
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    if len(full_cards_to_check) < 4:
        return None

    high_card = None
    all_combinations = itertools.combinations(full_cards_to_check, 4)



def is_full_house():
    pass


def _is_flush(cards):
    assert cards.__len__() == 5
    color = cards[0].color
    for card in cards:
        if card.color != color:
            return False
    return True

def is_flush(hand_card, public_cards):
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    if len(full_cards_to_check) < 5:
        return False
    all_combinations = itertools.combinations(full_cards_to_check, 5)
    return any(_is_flush(cards) for cards in all_combinations)

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

def is_straight(hand_card, public_cards):
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    if len(full_cards_to_check) < 5:
        return False
    all_combinations = itertools.combinations(full_cards_to_check, 5)
    return any(_is_straight(cards) for cards in all_combinations)


def is_three_of_a_kind():
    pass

def is_two_pair():
    pass

def is_one_pair():
    pass

