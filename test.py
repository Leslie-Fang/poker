import cards
import copy
import utils
import itertools
import pytest
from straight_flush import is_straight_flush
from four_of_kind import is_four_of_a_kind
from full_house import is_full_house

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



if __name__ == "__main__":
    pytest.main()
