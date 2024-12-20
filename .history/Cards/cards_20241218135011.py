class Card:
    """
     Represents a single playing card with various attributes.

    Attributes:
        is_blank (bool): Indicates whether the card is a placeholder for an empty space.
        suit (str): The suit of the card (e.g., 'Hearts', 'Diamonds', 'Spades', 'Clubs').
        rank (str/int): The rank of the card (e.g., 'Ace', 2, 3, ..., 'King').
        color (str): The color of the card ('Red' or 'Black').
        face_value (bool): Indicates whether the card is face up (True) or face down (False).
        suit_number (int): The index number representing the suit (0-3).
        rank_number (int): The number representing the rank (1-13).

    Methods:
        __init__: Initializes a new card with the given suit and rank.
        __str__: Returns a string representation of the card for display.
        __repr__: Returns a string representation of the card for debugging.
        decode_card: Decodes the suit and rank from a list representing the card.
        assign_color: Assigns the color attribute based on the suit of the card.
        change_face_value: Flips the card face up or face down.
        is_playable: Determines if the card can be played on top of another card.
    """

    def __init__(self, suit_number: int, rank_number: int) -> None:
        self.suit_number = suit_number # 0-3 for spades, hearts, diamonds, clubs
        self.rank_number = rank_number # 0-13 for Ace, 2-13 for two, etc.
        # Empty card is represented by suit and rank of -1
        
        # Set the default values for a blank card
        self.is_blank = True
        self.suit = None
        self.rank = None
        self.color = None
        self.face_value = None
        if self.suit_number != -1 and self.rank_number != -1:
            """If the input is not a blank card, then decode it and set its attributes."""
            self.is_blank = False
            self.suit, self.rank = self.decode_card()
            self.face_value = False # Default to face down
            self.color = self.assign_color()

    def __str__(self) -> str:
        """Returns a string representation of the card."""

        red = "\033[31m"  # ANSI code for red
        reset = "\033[0m"  # ANSI code to reset color
        
        if self.is_blank:
            return " ".ljust(20)
        else:
            card_str = f"{self.rank} of {self.suit}"
        if not self.face_value:
            return "*".ljust(20)
        elif self.color == "Red":
            return f"{red}{card_str}{reset}".ljust(20+len(red)+len(reset))  # Add color codes for red cards
        else:
            return card_str.ljust(20)
    
    def __repr__(self) -> str:
        """Returns a string representation of the card. (Use if you need an empty card)"""

        if self.is_blank:
            return " "
        elif not self.face_value:
            return "*"
        else:
            return f"{self.rank} of {self.suit}"
        
    def decode_card(self) -> tuple:
        """Decodes the deck."""
        if not self.is_blank:
            suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
            ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

            # Decode the card.
            suit = suits[self.suit_number]
            rank = ranks[self.rank_number]

            # Create a new card object with the decoded values.
            return suit, rank
        return None
    
    def assign_color(self) -> str:
        if not self.is_blank:
            if self.suit in ("Hearts", "Diamonds"):
                return "Red"
            else:
                return "Black"
     
    def change_face_value(self) -> bool:
        if not self.is_blank:
            self.face_value = not self.face_value

    def is_playable(self, other_card: "Card") -> bool:
        if not self.is_blank:
            if self.rank_number == other_card.rank_number - 1 and self.color != other_card.color:
                return True
        return False
    