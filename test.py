import cards
import copy
import utils
import itertools
import pytest
from straight_flush import is_straight_flush, compare_straight_flush
from four_of_kind import is_four_of_a_kind, compare_four_of_a_kind
from full_house import is_full_house, compare_full_house
from flush import is_flush, compare_flush
from straight import is_straight, compare_straight
from three_kind import is_three_kind, compare_three_kind
from two_pairs import is_two_pairs, compare_two_pairs
from one_pair import is_one_pair, compare_one_pair
from high_cards import compare_high_cards

class TestStraightFlush:
    def test_straight_flush_internal(self):
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(5, cards.CardColor.heart)
        public_card4 = cards.Card(6, cards.CardColor.heart)
        public_card5 = cards.Card(7, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]

        assert utils._is_flush(public_cards)
        assert utils._is_straight(public_cards)

    def test_straight_flush(self):
        hand_card = cards.HandCard(cards.Card(10, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(6, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_straight_flush(hand_card, public_cards) is not None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_straight_flush(hand_card, public_cards) is None

    def test_compare_straight_flush(self):
        hand_card1 = cards.HandCard(cards.Card(7, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(2, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.heart)
        public_card3 = cards.Card(4, cards.CardColor.heart)
        public_card4 = cards.Card(5, cards.CardColor.heart)
        public_card5 = cards.Card(6, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_straight_flush(hand_card, public_cards) == 1

        hand_card1 = cards.HandCard(cards.Card(8, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(10, cards.CardColor.heart), cards.Card(14, cards.CardColor.heart))
        hand_card = [hand_card1, hand_card2]
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_straight_flush(hand_card, public_cards) == 2

class TestFourKind:
    def test_four_of_a_kind_internal(self):
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(3, cards.CardColor.diamond)
        public_cards = [public_card1, public_card2, public_card3, public_card4]

        assert utils._is_four_of_a_kind(public_cards)

    def test_four_of_a_kind(self):
        hand_card = cards.HandCard(cards.Card(3, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_four_of_a_kind(hand_card, public_cards) is not None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_four_of_a_kind(hand_card, public_cards) is None

    def test_compare_four_of_a_kind(self):
        hand_card1 = cards.HandCard(cards.Card(3, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_four_of_a_kind(hand_card, public_cards) == 1

        hand_card1 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(3, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_four_of_a_kind(hand_card, public_cards) == 2

        hand_card1 = cards.HandCard(cards.Card(3, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_four_of_a_kind(hand_card, public_cards) is None

class TestFullHouse:
    def test_full_house(self):
        hand_card = cards.HandCard(cards.Card(10, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_full_house(hand_card, public_cards) is not None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_full_house(hand_card, public_cards) is None

    def test_compare_full_house(self):
        hand_card1 = cards.HandCard(cards.Card(10, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_full_house(hand_card, public_cards) is 1

        hand_card1 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(10, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_full_house(hand_card, public_cards) is 2

        hand_card1 = cards.HandCard(cards.Card(9, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_full_house(hand_card, public_cards) is None

        hand_card1 = cards.HandCard(cards.Card(3, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(3, cards.CardColor.heart), cards.Card(9, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_full_house(hand_card1, public_cards) is not None
        assert is_full_house(hand_card2, public_cards) is not None
        assert compare_full_house(hand_card, public_cards) is 1

class TestFlush:
    def test_flush(self):
        hand_card = cards.HandCard(cards.Card(14, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_flush(hand_card, public_cards) is None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.club)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_flush(hand_card, public_cards) is not None

    def test_compare_flush(self):
        hand_card1 = cards.HandCard(cards.Card(14, cards.CardColor.heart), cards.Card(2, cards.CardColor.heart))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.heart)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_flush(hand_card, public_cards) is 1

class TestStraight:
    def test_straight_internal(self):
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(5, cards.CardColor.club)
        public_card4 = cards.Card(6, cards.CardColor.heart)
        public_card5 = cards.Card(7, cards.CardColor.club)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]

        assert utils._is_straight(public_cards)

    def test_straight(self):
        hand_card = cards.HandCard(cards.Card(12, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(6, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.club)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_straight(hand_card, public_cards) is not None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_straight(hand_card, public_cards) is None

    def test_compare_straight(self):
        hand_card1 = cards.HandCard(cards.Card(7, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(14, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(2, cards.CardColor.spade)
        public_card2 = cards.Card(3, cards.CardColor.heart)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(5, cards.CardColor.diamond)
        public_card5 = cards.Card(6, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_straight(hand_card, public_cards) == 1

        hand_card1 = cards.HandCard(cards.Card(8, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(10, cards.CardColor.heart), cards.Card(14, cards.CardColor.heart))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(2, cards.CardColor.spade)
        public_card2 = cards.Card(3, cards.CardColor.heart)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(7, cards.CardColor.diamond)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_straight(hand_card, public_cards) is None

class TestThreeKind:
    def test_three_kind(self):
        hand_card = cards.HandCard(cards.Card(10, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_three_kind(hand_card, public_cards) is not None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_three_kind(hand_card, public_cards) is None

    def test_compare_three_kind(self):
        hand_card1 = cards.HandCard(cards.Card(10, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(3, cards.CardColor.heart), cards.Card(3, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_three_kind(hand_card, public_cards) is 1

        hand_card1 = cards.HandCard(cards.Card(3, cards.CardColor.diamond), cards.Card(7, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(3, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_three_kind(hand_card1, public_cards) is not None
        assert is_three_kind(hand_card2, public_cards) is not None
        assert compare_three_kind(hand_card, public_cards) is 2

        hand_card1 = cards.HandCard(cards.Card(9, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(11, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_three_kind(hand_card, public_cards) is None

class TestTwoPairs:
    def test_two_pairs(self):
        hand_card = cards.HandCard(cards.Card(10, cards.CardColor.diamond), cards.Card(3, cards.CardColor.club))
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_two_pairs(hand_card, public_cards) is not None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_two_pairs(hand_card, public_cards) is None

    def test_compare_two_pairs(self):
        hand_card1 = cards.HandCard(cards.Card(6, cards.CardColor.diamond), cards.Card(8, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(2, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_two_pairs(hand_card1, public_cards) is not None
        assert is_two_pairs(hand_card2, public_cards) is not None
        assert compare_two_pairs(hand_card, public_cards) is 2

        hand_card1 = cards.HandCard(cards.Card(9, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(2, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(3, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_two_pairs(hand_card, public_cards) is 1

class TestOnePair:
    def test_one_pair(self):
        hand_card = cards.HandCard(cards.Card(10, cards.CardColor.diamond), cards.Card(5, cards.CardColor.club))
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_one_pair(hand_card, public_cards) is not None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_one_pair(hand_card, public_cards) is None

    def test_compare_one_pairs(self):
        hand_card1 = cards.HandCard(cards.Card(6, cards.CardColor.diamond), cards.Card(8, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(8, cards.CardColor.spade))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert is_one_pair(hand_card1, public_cards) is not None
        assert is_one_pair(hand_card2, public_cards) is not None
        assert compare_one_pair(hand_card, public_cards) is 2

        hand_card1 = cards.HandCard(cards.Card(4, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(2, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(5, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_one_pair(hand_card, public_cards) is 1

        hand_card1 = cards.HandCard(cards.Card(6, cards.CardColor.diamond), cards.Card(10, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(2, cards.CardColor.club))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(7, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(5, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_one_pair(hand_card, public_cards) is None

class TestHighCards:
    def test_compare_high_cards(self):
        hand_card1 = cards.HandCard(cards.Card(6, cards.CardColor.diamond), cards.Card(14, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(12, cards.CardColor.spade))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_high_cards(hand_card, public_cards) is 1

        hand_card1 = cards.HandCard(cards.Card(6, cards.CardColor.diamond), cards.Card(14, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(6, cards.CardColor.heart), cards.Card(14, cards.CardColor.spade))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_high_cards(hand_card, public_cards) is 0

        hand_card1 = cards.HandCard(cards.Card(6, cards.CardColor.diamond), cards.Card(2, cards.CardColor.club))
        hand_card2 = cards.HandCard(cards.Card(11, cards.CardColor.heart), cards.Card(12, cards.CardColor.spade))
        hand_card = [hand_card1, hand_card2]
        public_card1 = cards.Card(10, cards.CardColor.heart)
        public_card2 = cards.Card(3, cards.CardColor.spade)
        public_card3 = cards.Card(4, cards.CardColor.club)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert compare_high_cards(hand_card, public_cards) is 2

if __name__ == "__main__":
    pytest.main()
