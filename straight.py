import utils
import itertools
import copy

def compare_straight(hand_cards, public_cards):
    """
    顺子

    return
        * None if both hands are not straight
        * 0 if both hands are straight and equal
        * 1 if hand1 is straight and larger
        * 2 if hand2 is straight and larger
    """
    assert len(hand_cards) == 2
    hand_card1 = hand_cards[0]
    hand_card2 = hand_cards[1]
    is_hand1_straight = is_straight(hand_card1, public_cards)
    is_hand2_straight = is_straight(hand_card2, public_cards)
    if is_hand1_straight is not None and is_hand2_straight is None:
        return 1
    elif is_hand1_straight is None and is_hand2_straight is not None:
        return 2
    elif is_hand1_straight is not None and is_hand2_straight is not None:
        if is_hand1_straight[0].number == is_hand2_straight[0].number:
            return 0


        if is_hand1_straight[0].number != 14 and is_hand2_straight[0].number == 14:
            return 1
        elif is_hand1_straight[0].number == 14 and is_hand2_straight[0].number != 14:
            return 2
        else:
            assert is_hand1_straight[0].number != 14
            assert is_hand1_straight[1].number != 14


        if is_hand1_straight[0].number > is_hand2_straight[0].number:
            return 1
        if is_hand1_straight[0].number < is_hand2_straight[0].number:
            return 2
    return None

def is_straight(hand_card, public_cards):
    """
    检查顺子
    return None if not flush
    else return the largest straight card with sorted of decrease order
    """
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    if len(full_cards_to_check) < 5:
        return False
    all_combinations = itertools.combinations(full_cards_to_check, 5)

    straight_card = None
    for cards in all_combinations:
        if utils._is_straight(cards):
            if straight_card is None:
                straight_card = copy.deepcopy(list(cards))
                straight_card.sort(key=lambda card: card.number, reverse=True)
            else:
                compare_cards = copy.deepcopy(list(cards))
                compare_cards.sort(key = lambda card:card.number, reverse=True)
                if compare_cards[0].number > straight_card[0].number:
                    straight_card = compare_cards

    return straight_card