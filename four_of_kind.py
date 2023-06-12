import utils
import itertools
import copy

def compare_four_of_a_kind(hand_cards, public_cards):
    """
    four kind

    return
        * None if both hands are not four_of_a_kind
        * 0 if both hands are four_of_a_kind and equal
        * 1 if hand1 is four_of_a_kind and larger
        * 2 if hand2 is four_of_a_kind and larger
    """
    assert len(hand_cards) == 2
    hand_card1 = hand_cards[0]
    hand_card2 = hand_cards[1]
    is_hand1_four_kind = is_four_of_a_kind(hand_card1, public_cards)
    is_hand2_four_kind = is_four_of_a_kind(hand_card2, public_cards)
    if is_hand1_four_kind is not None and is_hand2_four_kind is None:
        return 1
    elif is_hand1_four_kind is None and is_hand2_four_kind is not None:
        return 2
    elif is_hand1_four_kind is not None and is_hand2_four_kind is not None:
        if is_hand1_four_kind[0].number > is_hand2_four_kind[0].number:
            return 1
        elif is_hand1_four_kind[0].number < is_hand2_four_kind[0].number:
            return 2
        else:
            assert is_hand1_four_kind[0].number == is_hand2_four_kind[0].number
            if is_hand1_four_kind[4].number > is_hand2_four_kind[4].number:
                return 1
            elif is_hand1_four_kind[4].number < is_hand2_four_kind[4].number:
                return 2
            else:
                assert is_hand1_four_kind[4].number == is_hand2_four_kind[4].number
                return 0
    return None

def is_four_of_a_kind(hand_card, public_cards):
    """
    检查4条
    return None if not 4 of kind
    else return the largest 4 kind with format [same number of 4 kind, T corner]
    """
    assert public_cards.__len__() == 5
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    assert len(full_cards_to_check) == 7

    all_combinations = itertools.combinations(full_cards_to_check, 5)
    corner_card = None
    four_kinds_card = None
    for cards in all_combinations:
        all_sub_combinations = itertools.combinations(cards, 4)
        for sub_combination in all_sub_combinations:
            if utils._is_four_of_a_kind(sub_combination):

                # Get remaining (T corner) cards from 4 kinds out of cards
                same_number = sub_combination[0].number
                for card in cards:
                    if card.number != same_number:
                        corner_card = card

                assert corner_card is not None

                if four_kinds_card is None:
                    # four_kinds_number = sub_combination[0].number
                    # T_corner_number = corner_card.number
                    four_kinds_card = copy.deepcopy(list(sub_combination))
                    four_kinds_card.append(corner_card)
                elif sub_combination[0].number > four_kinds_card[0].number:
                    four_kinds_card = copy.deepcopy(list(sub_combination))
                    four_kinds_card.append(corner_card)
                elif sub_combination[0].number == four_kinds_card[0].number:
                    if corner_card.number == four_kinds_card[4].number:
                        four_kinds_card = copy.deepcopy(list(sub_combination))
                        four_kinds_card.append(corner_card)
    return four_kinds_card
