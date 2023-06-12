import os
import cards
import copy
import utils
import itertools
import compare_functions as cf
from multiprocessing import Pool, Manager, Lock
import multiprocessing

use_parallel = True
count_list = [0, 0, 0]  # number of equal, number of hand1 win, number of hand2 win
count_manager = multiprocessing.Lock()


rough_count = 0

def _compare_f(_hand_cards1, _hand_cards2, _public_cards_combination):
    # global count_list, count_manager
    # print("---calculation", flush=True)
    global rough_count
    rough_count += 1
    if rough_count % 10000 == 0:
        print("rough_count is: {}".format(rough_count), flush=True)
    return cf.compare_two_hand(_hand_cards1, _hand_cards2, _public_cards_combination)
    # print("finnish execution round in inner_function", flush=True)
    # try:
    #     _count_manager.acquire(block=True)
    #     count_list[res] += 1
    #     _current_total_count = count_list[0] + count_list[1] + count_list[2]
    #     print("current_total_count is: {}".format(_current_total_count), flush=True)
    #     if _current_total_count % 10000 == 0:
    #         print("current_total_count is: {}".format(_current_total_count), flush=True)
    #         print("current hand1 win count: {} percentage is: {:.2f}%".format(count_list[1], count_list[
    #             1] * 100 / _current_total_count),
    #               flush=True)
    #         print("current hand2 win count: {} percentage is: {:.2f}%".format(count_list[2], count_list[
    #             2] * 100 / _current_total_count),
    #               flush=True)
    #         print("current hand1 and hand2 equal count: {} is: {:.2f}%".format(count_list[0], count_list[
    #             0] * 100 / _current_total_count),
    #               flush=True)
    # finally:
    #     _count_manager.release()
    #
    # return

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
    all_cards = cards.get_all_cards()
    remain_cards = copy.deepcopy(all_cards)
    for hand_card in hand_cards:
        remain_cards = utils.remove_hand_card(remain_cards, hand_card)

    for public_card in public_cards:
        remain_cards = utils.remove_public_card(remain_cards, public_card)

    # utils.print_all_cards(remain_cards)
    remain_cards_needed = 5 - len(public_cards)

    total_candidate = 0
    all_public_cards_combinations = itertools.combinations(remain_cards, remain_cards_needed)
    for _ in all_public_cards_combinations:
        total_candidate += 1
    print("Total candidates is: {}".format(total_candidate), flush=True)

    global use_parallel, count_list, count_manager
    # use_parallel = True
    # count_list = [0, 0, 0]  # number of equal, number of hand1 win, number of hand2 win
    # count_manager = Lock()

    all_public_cards_combinations = itertools.combinations(remain_cards, remain_cards_needed)
    if use_parallel:
        # parallel calculation
        number_of_process = 4
        pool = Pool(processes=number_of_process)
        print("use multi processes", flush=True)

        # l = multiprocessing.Manager().Lock()

        future_results = []

        for public_cards_combination in all_public_cards_combinations:
            future_results.append(pool.apply_async(_compare_f, (hand_cards[0], hand_cards[1], public_cards_combination)))
        pool.close()
        print("finish submission of all tasks", flush=True)
        pool.join()
        print("finish calculation of all tasks", flush=True)
        for future_result in future_results:
            count_list[future_result.get()] += 1

    else:
        current_progress = 0
        for public_cards_combination in all_public_cards_combinations:
            count_list[cf.compare_two_hand(hand_cards[0], hand_cards[1], public_cards_combination)] += 1

            current_progress += 1
            if current_progress % 10000 == 0:
                print("progress count is: {}; percentage is: {:.2}%".format(current_progress, current_progress/total_candidate*100), flush=True)
                current_total_count = count_list[0] + count_list[1] + count_list[2]
                print("current_total_count is: {}".format(current_total_count), flush=True)
                print("current hand1 win count: {} percentage is: {:.2f}%".format(count_list[1], count_list[1] * 100 / current_total_count),
                      flush=True)
                print("current hand2 win count: {} percentage is: {:.2f}%".format(count_list[2], count_list[2] * 100 / current_total_count),
                      flush=True)
                print("current hand1 and hand2 equal count: {} is: {:.2f}%".format(count_list[0], count_list[0] * 100 / current_total_count),
                      flush=True)

    total_count = count_list[0] + count_list[1] + count_list[2]
    print("total_count is: {}".format(total_count), flush=True)
    print("hand1 win count: {} percentage is: {:.2f}%".format(count_list[1], count_list[1] * 100 / total_count), flush=True)
    print("hand2 win count: {} percentage is: {:.2f}%".format(count_list[2], count_list[2] * 100 / total_count), flush=True)
    print("hand1 and hand2 equal count: {} is: {:.2f}%".format(count_list[0], count_list[0] * 100 / total_count), flush=True)


if __name__ == "__main__":
    hand_card1 = cards.HandCard(cards.Card(10, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
    hand_card2 = cards.HandCard(cards.Card(14, cards.CardColor.heart), cards.Card(2, cards.CardColor.heart))
    hand_cards = [hand_card1, hand_card2]
    public_cards = []
    compare_hands(hand_cards, public_cards)