import utils
import itertools
import copy


def compare_one_pair(hand_cards, public_cards):
    """
    one pair

    return
        * None if both hands are not one pair
        * 0 if both hands are one pair and equal
        * 1 if hand1 is one pair and larger
        * 2 if hand2 is one pair and larger
    """
    assert len(hand_cards) == 2
    hand_card1 = hand_cards[0]
    hand_card2 = hand_cards[1]
    is_hand1_one_pair = is_one_pair(hand_card1, public_cards)
    is_hand2_one_pair = is_one_pair(hand_card2, public_cards)
    if is_hand1_one_pair is not None and is_hand2_one_pair is None:
        return 1
    elif is_hand1_one_pair is None and is_hand2_one_pair is not None:
        return 2
    elif is_hand1_one_pair is not None and is_hand2_one_pair is not None:
        if is_hand1_one_pair[0].number > is_hand2_one_pair[0].number:
            return 1
        elif is_hand1_one_pair[0].number < is_hand2_one_pair[0].number:
            return 2
        else:
            assert is_hand1_one_pair[0].number == is_hand2_one_pair[0].number
            if is_hand1_one_pair[2].number > is_hand2_one_pair[2].number:
                return 1
            elif is_hand1_one_pair[2].number < is_hand2_one_pair[2].number:
                return 2
            else:
                assert is_hand1_one_pair[2].number == is_hand2_one_pair[2].number
                if is_hand1_one_pair[3].number > is_hand2_one_pair[3].number:
                    return 1
                elif is_hand1_one_pair[3].number < is_hand2_one_pair[3].number:
                    return 2
                else:
                    assert is_hand1_one_pair[3].number == is_hand2_one_pair[3].number
                    if is_hand1_one_pair[4].number > is_hand2_one_pair[4].number:
                        return 1
                    elif is_hand1_one_pair[4].number < is_hand2_one_pair[4].number:
                        return 2
                    else:
                        assert is_hand1_one_pair[4].number == is_hand2_one_pair[4].number
                        return 0
    return None

def is_one_pair(hand_card, public_cards):
    """
    检查 one pair
    return None if not one pair
    else return the largest one pair with format [pair, corner number with decrease order]
    """
    assert public_cards.__len__() == 5
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    assert len(full_cards_to_check) == 7

    all_combinations = itertools.combinations(full_cards_to_check, 5)
    largest_one_pair_cards = None
    for cards in all_combinations:
        all_sub_combinations = itertools.combinations(cards, 2)
        for sub_combination in all_sub_combinations:
            if utils._is_two_of_a_kind(sub_combination):

                test_cards = copy.deepcopy(list(cards))
                # for card in test_cards:
                cards_to_remove = []
                for card_to_check in test_cards:
                    for two_kinds_card in sub_combination:
                        if two_kinds_card.number == card_to_check.number and two_kinds_card.color == card_to_check.color:
                            cards_to_remove.append(card_to_check)
                for card in cards_to_remove:
                    test_cards.remove(card)
                assert len(test_cards) == 3

                corner_cards = copy.deepcopy(list(test_cards))

                corner_cards.sort(key=lambda card: card.number, reverse=True)

                if largest_one_pair_cards is None:
                    largest_one_pair_cards = copy.deepcopy(list(sub_combination))
                    largest_one_pair_cards.extend(corner_cards)
                else:
                    if sub_combination[0].number > largest_one_pair_cards[0].number:
                        largest_one_pair_cards = copy.deepcopy(list(sub_combination))
                        largest_one_pair_cards.extend(corner_cards)
                    elif sub_combination[0].number == largest_one_pair_cards[0].number:
                        if corner_cards[0].number > largest_one_pair_cards[2].number:
                            largest_one_pair_cards = copy.deepcopy(list(sub_combination))
                            largest_one_pair_cards.extend(corner_cards)
                        elif corner_cards[0].number == largest_one_pair_cards[2].number:
                            if corner_cards[1].number > largest_one_pair_cards[3].number:
                                largest_one_pair_cards = copy.deepcopy(list(sub_combination))
                                largest_one_pair_cards.extend(corner_cards)
                            elif corner_cards[1].number == largest_one_pair_cards[3].number:
                                if corner_cards[2].number > largest_one_pair_cards[4].number:
                                    largest_one_pair_cards = copy.deepcopy(list(sub_combination))
                                    largest_one_pair_cards.extend(corner_cards)

    return largest_one_pair_cards