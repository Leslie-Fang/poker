import utils
import itertools
import copy

def compare_flush(hand_cards, public_cards):
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
    is_hand1_flush = is_flush(hand_card1, public_cards)
    is_hand2_flush = is_flush(hand_card2, public_cards)
    if is_hand1_flush is not None and is_hand2_flush is None:
        return 1
    elif is_hand1_flush is None and is_hand2_flush is not None:
        return 2
    elif is_hand1_flush is not None and is_hand2_flush is not None:
        if is_hand1_flush[0].number > is_hand2_flush[0].number:
            return 1
        elif is_hand1_flush[0].number < is_hand2_flush[0].number:
            return 2
        else:
            assert is_hand1_flush[0].number == is_hand2_flush[0].number
            if is_hand1_flush[1].number > is_hand2_flush[1].number:
                return 1
            elif is_hand1_flush[1].number < is_hand2_flush[1].number:
                return 2
            else:
                assert is_hand1_flush[1].number == is_hand2_flush[1].number
                if is_hand1_flush[2].number > is_hand2_flush[2].number:
                    return 1
                elif is_hand1_flush[2].number < is_hand2_flush[2].number:
                    return 2
                else:
                    assert is_hand1_flush[2].number == is_hand2_flush[2].number
                    if is_hand1_flush[3].number > is_hand2_flush[3].number:
                        return 1
                    elif is_hand1_flush[3].number < is_hand2_flush[3].number:
                        return 2
                    else:
                        assert is_hand1_flush[3].number == is_hand2_flush[3].number
                    if is_hand1_flush[4].number > is_hand2_flush[4].number:
                        return 1
                    elif is_hand1_flush[4].number < is_hand2_flush[4].number:
                        return 2
                    else:
                        assert is_hand1_flush[4].number == is_hand2_flush[4].number
                        return 0
    return None

def is_flush(hand_card, public_cards):
    """
    检查同花
    return None if not flush
    else return the largest flush card with sorted of decrease order
    """
    full_cards_to_check = copy.deepcopy(list(public_cards))
    full_cards_to_check.append(hand_card.card1)
    full_cards_to_check.append(hand_card.card2)
    # Sort of decrease number
    full_cards_to_check.sort(key = lambda card:card.number, reverse=True)

    if len(full_cards_to_check) < 5:
        return False
    all_combinations = itertools.combinations(full_cards_to_check, 5)
    # return any(_is_flush(cards) for cards in all_combinations)

    flush_card = None
    for cards in all_combinations:
        if utils._is_flush(cards):
            if flush_card is None:
                flush_card = copy.deepcopy(list(cards))
                flush_card.sort(key=lambda card: card.number, reverse=True)
            else:
                compare_card = copy.deepcopy(list(cards))
                compare_card.sort(key=lambda card: card.number, reverse=True)
                if compare_card[0].number > flush_card[0].number:
                    flush_card = copy.deepcopy(list(compare_card))
                    flush_card.sort(key=lambda card: card.number, reverse=True)
                elif compare_card[0].number == flush_card[0].number:
                    if compare_card[1].number > flush_card[1].number:
                        flush_card = copy.deepcopy(list(compare_card))
                        flush_card.sort(key=lambda card: card.number, reverse=True)
                    elif compare_card[1].number == flush_card[1].number:
                        if compare_card[2].number > flush_card[2].number:
                            flush_card = copy.deepcopy(list(compare_card))
                            flush_card.sort(key=lambda card: card.number, reverse=True)
                        elif compare_card[2].number == flush_card[2].number:
                            if compare_card[3].number > flush_card[3].number:
                                flush_card = copy.deepcopy(list(compare_card))
                                flush_card.sort(key=lambda card: card.number, reverse=True)
                            elif compare_card[3].number == flush_card[3].number:
                                if compare_card[4].number > flush_card[4].number:
                                    flush_card = copy.deepcopy(list(compare_card))
                                    flush_card.sort(key=lambda card: card.number, reverse=True)
    return flush_card