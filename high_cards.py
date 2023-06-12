import utils
import itertools
import copy

def compare_high_cards(hand_cards, public_cards):
    """
    high cards

    return
        * 0 if both hands are straight and equal
        * 1 if hand1 is straight and larger
        * 2 if hand2 is straight and larger
    """
    assert len(hand_cards) == 2
    hand_card1 = hand_cards[0]
    hand_card2 = hand_cards[1]
    is_hand1_straight = largest_high_card(hand_card1, public_cards)
    is_hand2_straight = largest_high_card(hand_card2, public_cards)
    if is_hand1_straight[0].number > is_hand2_straight[0].number:
        return 1
    elif is_hand1_straight[0].number < is_hand2_straight[0].number:
        return 2
    else:
        assert is_hand1_straight[0].number == is_hand2_straight[0].number
        if is_hand1_straight[1].number > is_hand2_straight[1].number:
            return 1
        elif is_hand1_straight[1].number < is_hand2_straight[1].number:
            return 2
        else:
            assert is_hand1_straight[1].number == is_hand2_straight[1].number
            if is_hand1_straight[2].number > is_hand2_straight[2].number:
                return 1
            elif is_hand1_straight[2].number < is_hand2_straight[2].number:
                return 2
            else:
                assert is_hand1_straight[2].number == is_hand2_straight[2].number
                if is_hand1_straight[3].number > is_hand2_straight[3].number:
                    return 1
                elif is_hand1_straight[3].number < is_hand2_straight[3].number:
                    return 2
                else:
                    assert is_hand1_straight[3].number == is_hand2_straight[3].number
                    if is_hand1_straight[4].number > is_hand2_straight[4].number:
                        return 1
                    elif is_hand1_straight[4].number < is_hand2_straight[4].number:
                        return 2
                    else:
                        assert is_hand1_straight[4].number == is_hand2_straight[4].number
                        return 0


def largest_high_card(hand_card, public_cards):
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

    largest_high_cards = None
    for cards in all_combinations:
        compare_card = copy.deepcopy(list(cards))
        compare_card.sort(key=lambda card: card.number, reverse=True)
        if largest_high_cards is None:
            largest_high_cards = compare_card
        else:
            if compare_card[0].number > largest_high_cards[0].number:
                largest_high_cards = compare_card
            elif compare_card[0].number == largest_high_cards[0].number:
                if compare_card[1].number > largest_high_cards[1].number:
                    largest_high_cards = compare_card
                elif compare_card[1].number == largest_high_cards[1].number:
                    if compare_card[2].number > largest_high_cards[2].number:
                        largest_high_cards = compare_card
                    elif compare_card[2].number == largest_high_cards[2].number:
                        if compare_card[3].number > largest_high_cards[3].number:
                            largest_high_cards = compare_card
                        elif compare_card[3].number == largest_high_cards[3].number:
                            if compare_card[4].number > largest_high_cards[4].number:
                                largest_high_cards = compare_card

    return largest_high_cards
