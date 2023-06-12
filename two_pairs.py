import utils
import itertools
import copy


def compare_two_pairs(hand_cards, public_cards):
    """
    two pairs house

    return
        * None if both hands are not two pairs
        * 0 if both hands are two pairs and equal
        * 1 if hand1 is two pairs and larger
        * 2 if hand2 is two pairs and larger
    """
    assert len(hand_cards) == 2
    hand_card1 = hand_cards[0]
    hand_card2 = hand_cards[1]
    is_hand1_two_pairs = is_two_pairs(hand_card1, public_cards)
    is_hand2_two_pairs = is_two_pairs(hand_card2, public_cards)
    if is_hand1_two_pairs is not None and is_hand2_two_pairs is None:
        return 1
    elif is_hand1_two_pairs is None and is_hand2_two_pairs is not None:
        return 2
    elif is_hand1_two_pairs is not None and is_hand2_two_pairs is not None:
        if is_hand1_two_pairs[0].number > is_hand2_two_pairs[0].number:
            return 1
        elif is_hand1_two_pairs[0].number < is_hand2_two_pairs[0].number:
            return 2
        else:
            assert is_hand1_two_pairs[0].number == is_hand2_two_pairs[0].number
            if is_hand1_two_pairs[2].number > is_hand2_two_pairs[2].number:
                return 1
            elif is_hand1_two_pairs[2].number < is_hand2_two_pairs[2].number:
                return 2
            else:
                assert is_hand1_two_pairs[2].number == is_hand2_two_pairs[2].number
                if is_hand1_two_pairs[4].number > is_hand2_two_pairs[4].number:
                    return 1
                elif is_hand1_two_pairs[4].number < is_hand2_two_pairs[4].number:
                    return 2
                else:
                    assert is_hand1_two_pairs[4].number == is_hand2_two_pairs[4].number
                    return 0
    return None

def is_two_pairs(hand_card, public_cards):
    """
    检查 two pairs
    return None if not full house
    else return the largest two pairs with format [large pair, small pair, corner number]
    """
    assert public_cards.__len__() == 5
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    assert len(full_cards_to_check) == 7

    all_combinations = itertools.combinations(full_cards_to_check, 5)
    largest_two_pair_cards = None
    for cards in all_combinations:
        all_sub_combinations = itertools.combinations(cards, 2)
        for sub_combination in all_sub_combinations:
            pair1 = None
            if utils._is_two_of_a_kind(sub_combination):
                pair1 = copy.deepcopy(sub_combination)

                test_cards = copy.deepcopy(list(cards))
                # for card in test_cards:
                cards_to_remove = []
                for card_to_check in test_cards:
                    for two_kinds_card in pair1:
                        if two_kinds_card.number == card_to_check.number and two_kinds_card.color == card_to_check.color:
                            cards_to_remove.append(card_to_check)
                for card in cards_to_remove:
                    test_cards.remove(card)
                assert len(test_cards) == 3
                all_sub_combinations2 = itertools.combinations(test_cards, 2)
                for sub_combination2 in all_sub_combinations2:
                    pair2 = None
                    if utils._is_two_of_a_kind(sub_combination2):
                        pair2 = copy.deepcopy(sub_combination2)

                        larger_pair = None
                        small_pair = None

                        if pair1[0].number > pair2[0].number:
                            larger_pair = pair1
                            small_pair = pair2
                        elif pair1[0].number < pair2[0].number:
                            larger_pair = pair2
                            small_pair = pair1
                        else:
                            assert pair1[0].number == pair2[0].number
                            larger_pair = pair1
                            small_pair = pair2

                        T_corner_card = None
                        cards_to_remove2 = []
                        for card_to_check in test_cards:
                            for two_kinds_card in pair2:
                                if two_kinds_card.number == card_to_check.number and two_kinds_card.color == card_to_check.color:
                                    cards_to_remove2.append(card_to_check)
                        for card in cards_to_remove2:
                            test_cards.remove(card)
                        assert len(test_cards) == 1
                        T_corner_card = test_cards[0]

                        if largest_two_pair_cards is None:
                            largest_two_pair_cards = copy.deepcopy(list(larger_pair))
                            largest_two_pair_cards.extend(small_pair)
                            largest_two_pair_cards.append(T_corner_card)
                        else:
                            if larger_pair[0].number > largest_two_pair_cards[0].number:
                                largest_two_pair_cards = copy.deepcopy(list(larger_pair))
                                largest_two_pair_cards.extend(small_pair)
                                largest_two_pair_cards.append(T_corner_card)
                            elif larger_pair[0].number == largest_two_pair_cards[0].number:
                                if small_pair[0].number > largest_two_pair_cards[2].number:
                                    largest_two_pair_cards = copy.deepcopy(list(larger_pair))
                                    largest_two_pair_cards.extend(small_pair)
                                    largest_two_pair_cards.append(T_corner_card)
                                elif small_pair[0].number == largest_two_pair_cards[2].number:
                                    if T_corner_card.number > largest_two_pair_cards[4].number:
                                        largest_two_pair_cards = copy.deepcopy(list(larger_pair))
                                        largest_two_pair_cards.extend(small_pair)
                                        largest_two_pair_cards.append(T_corner_card)
    return largest_two_pair_cards