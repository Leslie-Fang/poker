import utils
import itertools
import copy


def compare_straight_flush(hand_cards, public_cards):
    """
    同花顺

    return
        * None if both hands are not straight flush
        * 0 if both hands are straight flush and equal
        * 1 if hand1 is straight flush and larger
        * 2 if hand2 is straight flush and larger
    """
    assert len(hand_cards) == 2
    hand_card1 = hand_cards[0]
    hand_card2 = hand_cards[1]
    is_hand1_straight_flush = is_straight_flush(hand_card1, public_cards)
    is_hand2_straight_flush = is_straight_flush(hand_card2, public_cards)
    if is_hand1_straight_flush is not None and is_hand2_straight_flush is None:
        return 1
    elif is_hand1_straight_flush is None and is_hand2_straight_flush is not None:
        return 2
    elif is_hand1_straight_flush is not None and is_hand2_straight_flush is not None:
        if is_hand1_straight_flush[0].number == is_hand2_straight_flush[0].number:
            return 0
        if is_hand1_straight_flush[0].number > is_hand2_straight_flush[0].number:
            return 1
        if is_hand1_straight_flush[0].number < is_hand2_straight_flush[0].number:
            return 2
    return None


def is_straight_flush(hand_card, public_cards):
    """
    同花顺

    return
    * None if is not straight_flush
    * else return the largest straight_flush
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
        if utils._is_flush(cards) and utils._is_straight(cards):
            if largest_cards is None:
                largest_cards = copy.deepcopy(list(cards))
                largest_cards.sort(key = lambda card:card.number, reverse=True)
            else:
                compare_cards = copy.deepcopy(list(cards))
                compare_cards.sort(key = lambda card:card.number, reverse=True)
                if compare_cards[0].number > largest_cards[0].number:
                    largest_cards = compare_cards
    return largest_cards