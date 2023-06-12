import utils
import itertools
import copy

def compare_full_house(hand_cards, public_cards):
    """
    full house

    return
        * None if both hands are not full_house
        * 0 if both hands are full_house and equal
        * 1 if hand1 is full_house and larger
        * 2 if hand2 is full_house and larger
    """
    assert len(hand_cards) == 2
    hand_card1 = hand_cards[0]
    hand_card2 = hand_cards[1]
    is_hand1_full_house = is_full_house(hand_card1, public_cards)
    is_hand2_full_house = is_full_house(hand_card2, public_cards)
    if is_hand1_full_house is not None and is_hand2_full_house is None:
        return 1
    elif is_hand1_full_house is None and is_hand2_full_house is not None:
        return 2
    elif is_hand1_full_house is not None and is_hand2_full_house is not None:
        if is_hand1_full_house[0].number > is_hand2_full_house[0].number:
            return 1
        elif is_hand1_full_house[0].number < is_hand2_full_house[0].number:
            return 2
        else:
            assert is_hand1_full_house[0].number == is_hand2_full_house[0].number
            if is_hand1_full_house[3].number > is_hand2_full_house[3].number:
                return 1
            elif is_hand1_full_house[3].number < is_hand2_full_house[3].number:
                return 2
            else:
                assert is_hand1_full_house[3].number == is_hand2_full_house[3].number
                return 0
    return None

def is_full_house(hand_card, public_cards):
    """
    检查葫芦
    return None if not full house
    else return the largest full house with format [same number of 3 kind, same number of 2 kind]
    """
    assert public_cards.__len__() == 5
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    assert len(full_cards_to_check) == 7

    all_combinations = itertools.combinations(full_cards_to_check, 5)
    full_house_card = None
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
                if utils._is_two_of_a_kind(test_cards):
                    if full_house_card is None:
                        full_house_card = copy.deepcopy(list(sub_combination))
                        full_house_card.extend(test_cards)
                    elif sub_combination[0].number > full_house_card[0].number:
                        full_house_card = copy.deepcopy(list(sub_combination))
                        full_house_card.extend(test_cards)
                    elif sub_combination[0].number == full_house_card[0].number:
                        if test_cards[0].number > full_house_card[3].number:
                            full_house_card = copy.deepcopy(list(sub_combination))
                            full_house_card.extend(test_cards)
    return full_house_card
