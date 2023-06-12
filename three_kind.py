import utils
import itertools
import copy

def compare_three_kind(hand_cards, public_cards):
    """
    three kind

    return
        * None if both hands are not three kinds
        * 0 if both hands are three kinds and equal
        * 1 if hand1 is three kinds and larger
        * 2 if hand2 is three kinds and larger
    """
    assert len(hand_cards) == 2
    hand_card1 = hand_cards[0]
    hand_card2 = hand_cards[1]
    is_hand1_three_kind = is_three_kind(hand_card1, public_cards)
    is_hand2_three_kind = is_three_kind(hand_card2, public_cards)
    if is_hand1_three_kind is not None and is_hand2_three_kind is None:
        return 1
    elif is_hand1_three_kind is None and is_hand2_three_kind is not None:
        return 2
    elif is_hand1_three_kind is not None and is_hand2_three_kind is not None:
        if is_hand1_three_kind[0].number > is_hand2_three_kind[0].number:
            return 1
        elif is_hand1_three_kind[0].number < is_hand2_three_kind[0].number:
            return 2
        else:
            assert is_hand1_three_kind[0].number == is_hand2_three_kind[0].number
            if is_hand1_three_kind[3].number > is_hand2_three_kind[3].number:
                return 1
            elif is_hand1_three_kind[3].number < is_hand2_three_kind[3].number:
                return 2
            else:
                assert is_hand1_three_kind[3].number == is_hand2_three_kind[3].number
                if is_hand1_three_kind[4].number > is_hand2_three_kind[4].number:
                    return 1
                elif is_hand1_three_kind[4].number < is_hand2_three_kind[4].number:
                    return 2
                else:
                    assert is_hand1_three_kind[4].number == is_hand2_three_kind[4].number
                    return 0
    return None

def is_three_kind(hand_card, public_cards):
    """
    检查 3kinds
    return None if not full house
    else return the largest 3 kinds with format [same number of 3 kind, larger number, small number]
    """
    assert public_cards.__len__() == 5
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    assert len(full_cards_to_check) == 7

    all_combinations = itertools.combinations(full_cards_to_check, 5)
    largest_three_kinds_card = None
    for cards in all_combinations:
        all_sub_combinations = itertools.combinations(cards, 3)
        for sub_combination in all_sub_combinations:
            if utils._is_three_of_a_kind(sub_combination):
                test_cards = copy.deepcopy(list(cards))
                # for card in test_cards:
                cards_to_remove = []
                for card_to_check in test_cards:
                    for three_kinds_card in sub_combination:
                        if three_kinds_card.number == card_to_check.number and three_kinds_card.color == card_to_check.color:
                            cards_to_remove.append(card_to_check)
                for card in cards_to_remove:
                    test_cards.remove(card)
                assert len(test_cards) == 2
                test_cards.sort(key=lambda card: card.number, reverse=True)
                assert utils._is_two_of_a_kind(test_cards) is False

                if largest_three_kinds_card is None:
                    largest_three_kinds_card = copy.deepcopy(list(sub_combination))
                    largest_three_kinds_card.extend(test_cards)
                elif sub_combination[0].number > largest_three_kinds_card[0].number:
                    largest_three_kinds_card = copy.deepcopy(list(sub_combination))
                    largest_three_kinds_card.extend(test_cards)
                elif sub_combination[0].number == largest_three_kinds_card[0].number:
                    if test_cards[0].number > largest_three_kinds_card[3].number:
                        largest_three_kinds_card = copy.deepcopy(list(sub_combination))
                        largest_three_kinds_card.extend(test_cards)
                    elif test_cards[0].number == largest_three_kinds_card[3].number:
                        if test_cards[1].number > largest_three_kinds_card[4].number:
                            largest_three_kinds_card = copy.deepcopy(list(sub_combination))
                            largest_three_kinds_card.extend(test_cards)
    return largest_three_kinds_card