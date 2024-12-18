import random

from cards import Card


class BuildDeck:
    """A class to create and shuffle a deck of cards for a solitaire game.

    The deck is represented as a list of tuples, where each tuple consists of
    two elements: the suit and the rank of a card.

    Attributes:
        deck (list of tuples): The deck of cards used for the solitaire game.

    Methods:
        __init__: Initializes a new deck and shuffles it.
        __str__: Returns a string representation of the deck.
        generate_deck: Generates a standard deck of 52 playing cards.
        """

    def __init__(self) -> None:
        """Initializes and shuffles the deck of cards."""
        """Builds the solitaire game board."""
        self.deck = self.generate_deck()
        random.shuffle(self.deck)

    def __str__(self) -> str:
        """Convert each card tuple to a string and join them with a newline"""
        cards_list = [str(i) for i in self.deck]
        return '\n'.join(cards_list)

    def generate_deck(self) -> list:
        """Generate a deck of cards."""

        # Create an empty deck.
        deck = []

        # Add 13 cards to the deck.
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                deck.append(card)

        return deck