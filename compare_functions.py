from straight_flush import is_straight_flush, compare_straight_flush
from four_of_kind import is_four_of_a_kind, compare_four_of_a_kind
from full_house import is_full_house, compare_full_house
from flush import compare_flush
from straight import compare_straight
from three_kind import compare_three_kind
from two_pairs import compare_two_pairs
from one_pair import compare_one_pair
from high_cards import compare_high_cards
import copy
from multiprocessing import Pool
import cards
import utils
import itertools

def _compare_f(_hand_cards1, _hand_cards2, _public_cards_combination):
    return compare_two_hand(_hand_cards1, _hand_cards2, _public_cards_combination)

def compare_hands(hand_cards, public_cards, all_cards=cards.get_all_cards(), use_parallel=True, number_of_process=4):
    """
    inputs:
    * hand_cards: a list: 1. size is number of player; 2. Each item is the hand of the player
    * public_cards: Known of public cards in the playgroup
    """
    # Only support compare of 2 hands at now
    assert isinstance(hand_cards, list)
    assert len(hand_cards) == 2
    assert isinstance(public_cards, list)
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

    count_list = [0, 0, 0]  # number of equal, number of hand1 win, number of hand2 win
    all_public_cards_combinations = itertools.combinations(remain_cards, remain_cards_needed)
    if use_parallel:
        # parallel calculation
        pool = Pool(processes=number_of_process)
        print("use multi processes", flush=True)

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
            count_list[compare_two_hand(hand_cards[0], hand_cards[1], public_cards_combination)] += 1

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
    return count_list

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
    hand_card1 = copy.deepcopy(hand_card1)
    hand_card2 = copy.deepcopy(hand_card2)

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
