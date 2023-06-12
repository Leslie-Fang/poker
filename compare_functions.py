from straight_flush import is_straight_flush, compare_straight_flush
from four_of_kind import is_four_of_a_kind, compare_four_of_a_kind
from full_house import is_full_house, compare_full_house
from flush import compare_flush
from straight import compare_straight
from three_kind import compare_three_kind
from two_pairs import compare_two_pairs
from one_pair import compare_one_pair
from high_cards import compare_high_cards


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

    # Step1: Compare straight_flush firstly
    res_straight_flush = compare_straight_flush([hand_card1, hand_card2], public_cards)
    if res_straight_flush is not None:
        return res_straight_flush
    # all of 2 hands are not straight_flush

    # Step2: compare 4 kind
    res_four_kind = compare_four_of_a_kind([hand_card1, hand_card2], public_cards)
    if res_four_kind is not None:
        return res_four_kind
    # all of 2 hands are not four_kind

    # Step3: compare full house
    res_full_house = compare_full_house([hand_card1, hand_card2], public_cards)
    if res_full_house is not None:
        return res_full_house
    # all of 2 hands are not full house

    # Step4: compare flush
    res_flush = compare_flush([hand_card1, hand_card2], public_cards)
    if res_flush is not None:
        return res_flush
    # all of 2 hands are not flush

    # Step5: compare straight
    res_straight = compare_straight([hand_card1, hand_card2], public_cards)
    if res_straight is not None:
        return res_straight
    # all of 2 hands are not straight

    # Step6: compare three kinds
    res_three_kind = compare_three_kind([hand_card1, hand_card2], public_cards)
    if res_three_kind is not None:
        return res_three_kind
    # all of 2 hands are not three kinds

    # Step7: compare two pairs
    res_two_pair = compare_two_pairs([hand_card1, hand_card2], public_cards)
    if res_two_pair is not None:
        return res_two_pair
    # all of 2 hands are not two pairs

    # Step8: compare one pair
    res_one_pair = compare_one_pair([hand_card1, hand_card2], public_cards)
    if res_one_pair is not None:
        return res_one_pair
    # all of 2 hands are not one pair

    # Step9: compare high card
    return compare_high_cards([hand_card1, hand_card2], public_cards)
