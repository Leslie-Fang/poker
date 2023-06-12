import cards
import compare_functions as cf

if __name__ == "__main__":
    hand_card1 = cards.HandCard(cards.Card(10, cards.CardColor.heart), cards.Card(10, cards.CardColor.club))
    hand_card2 = cards.HandCard(cards.Card(14, cards.CardColor.heart), cards.Card(2, cards.CardColor.heart))
    hand_cards = [hand_card1, hand_card2]
    public_cards = []
    cf.compare_hands(hand_cards, public_cards)