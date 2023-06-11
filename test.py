import cards
import copy
import utils
import itertools
import pytest

class TestFunctions:
    def test_straight_flush(self):
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(5, cards.CardColor.heart)
        public_card4 = cards.Card(6, cards.CardColor.heart)
        public_card5 = cards.Card(7, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]

        assert utils._is_flush(public_cards)
        assert utils._is_straight(public_cards)

    def test_straight_flush2(self):
        hand_card = cards.HandCard(cards.Card(10, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(6, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert utils.is_straight_flush(hand_card, public_cards) is not None

        public_card1 = cards.Card(3, cards.CardColor.heart)
        public_card2 = cards.Card(4, cards.CardColor.heart)
        public_card3 = cards.Card(7, cards.CardColor.heart)
        public_card4 = cards.Card(8, cards.CardColor.heart)
        public_card5 = cards.Card(9, cards.CardColor.heart)
        public_cards = [public_card1, public_card2, public_card3, public_card4, public_card5]
        assert utils.is_straight_flush(hand_card, public_cards) is None

if __name__ == "__main__":
    pytest.main()
