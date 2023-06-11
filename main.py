import os
import cards
import copy
import utils
import itertools

def compare_hands(hand_cards, public_cards):
    """
    inputs:
    * hand_cards: a list: 1. size is number of player; 2. Each item is the hand of the player
    * public_cards: Known of public cards in the playgroup
    """
    # Only support compare of 2 hands at now
    all_cards = cards.all_cards
    remain_cards = copy.deepcopy(all_cards)
    for hand_card in hand_cards:
        remain_cards = utils.remove_hand_card(remain_cards, hand_card)

    for public_card in public_cards:
        remain_cards = utils.remove_public_card(remain_cards, public_card)

    # utils.print_all_cards(remain_cards)

    all_public_cards_combinations = itertools.combinations(remain_cards, 5)
    count_list = [0, 0, 0] # number of equal, number of hand1 win, number of hand2 win

    # utils.is_straight_flush(hand_cards[0], public_cards_combination)

    for public_cards_combination in all_public_cards_combinations:
        # res = utils.is_straight_flush(hand_cards[0], public_cards_combination)

        count_list[utils.compare_two_hand(hand_cards[0], hand_cards[1], public_cards_combination)] += 1

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


    # public_card1 = cards.Card(3, cards.CardColor.heart)
    # public_card2 = cards.Card(4, cards.CardColor.heart)
    # public_card3 = cards.Card(5, cards.CardColor.heart)
    # public_card4 = cards.Card(6, cards.CardColor.heart)
    # public_card5 = cards.Card(7, cards.CardColor.heart)
    # public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]

    # print(utils.is_straight_flush(hand_cards[1], public_cards))
    # public_cards.sort(key=lambda card: card.number, reverse=True)
    # print(utils._is_flush(public_cards))
    # print(utils._is_straight(public_cards))