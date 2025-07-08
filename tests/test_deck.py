import sys
sys.path.append('Cards')

from deck import BuildDeck
from cards import Card


def test_build_deck_unique_cards():
    deck = BuildDeck()
    deck.deck = deck.generate_deck()  # use ordered deck to avoid shuffle
    unique = {(c.suit_number, c.rank_number) for c in deck.deck}
    assert len(deck.deck) == 52
    assert len(unique) == 52

def test_card_playable_rules():
    red_six = Card(0, 5)  # 6 of Hearts (Red)
    black_seven = Card(2, 6)  # 7 of Spades (Black)
    assert red_six.is_playable(black_seven)
    assert not black_seven.is_playable(red_six)

def test_card_playable_foundation():
    lower = Card(0, 5)  # 6 of Hearts
    higher = Card(0, 6)  # 7 of Hearts
    assert lower.is_playable_foundation(higher)
    other_suit = Card(1, 6)  # Diamonds 7
    assert not lower.is_playable_foundation(other_suit)
