import os
import cards
import copy
import utils
import itertools
import compare_functions as cf


def compare_hands(hand_cards, public_cards):
    """
    inputs:
    * hand_cards: a list: 1. size is number of player; 2. Each item is the hand of the player
    * public_cards: Known of public cards in the playgroup
    """
    # Only support compare of 2 hands at now
    assert isinstance(hand_cards, list)
    assert len(hand_cards) == 2
    assert isinstance(public_cards, list)
    all_cards = cards.all_cards
    remain_cards = copy.deepcopy(all_cards)
    for hand_card in hand_cards:
        remain_cards = utils.remove_hand_card(remain_cards, hand_card)

    for public_card in public_cards:
        remain_cards = utils.remove_public_card(remain_cards, public_card)

    # utils.print_all_cards(remain_cards)
    remain_cards_needed = 5 - len(public_cards)
    count_list = [0, 0, 0] # number of equal, number of hand1 win, number of hand2 win

    total_candidate = 0
    all_public_cards_combinations = itertools.combinations(remain_cards, remain_cards_needed)
    for _ in all_public_cards_combinations:
        total_candidate += 1

    print("Total candidates is: {}".format(total_candidate), flush=True)
    current_progress = 0
    all_public_cards_combinations = itertools.combinations(remain_cards, remain_cards_needed)
    for public_cards_combination in all_public_cards_combinations:
        count_list[cf.compare_two_hand(hand_cards[0], hand_cards[1], public_cards_combination)] += 1

        current_progress += 1
        if current_progress % 10000 == 0:
            print("progress count is: {}; percentage is: {}%".format(current_progress, current_progress/total_candidate*100), flush=True)

    total_count = count_list[0] + count_list[1] + count_list[2]
    print("total_count is: {}".format(total_count), flush=True)
    print("hand1 win count: {} percentage is: {}".format(count_list[1], count_list[1] / total_count), flush=True)
    print("hand2 win count: {} percentage is: {}".format(count_list[2], count_list[2] / total_count), flush=True)
    print("hand1 and hand2 equal count: {} is: {}".format(count_list[0], count_list[0] / total_count), flush=True)


if __name__ == "__main__":
    hand_card1 = cards.HandCard(cards.Card(10, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
    hand_card2 = cards.HandCard(cards.Card(14, cards.CardColor.heart), cards.Card(2, cards.CardColor.heart))
    hand_cards = [hand_card1, hand_card2]
    public_cards = []
    compare_hands(hand_cards, public_cards)