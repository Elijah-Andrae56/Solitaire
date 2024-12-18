from cards import Card

class Stock:
    """Represents the stack of remaining cards left in a solitaire deck. Ment to be iterated through, and generated in the When the """
    
    def __init__(self, stock: list) -> None:
        """Creates a new stack"""
        self.stock = stock
        self.face_value_up()

    def __str__(self) -> str:
        return f"The current card is: {self.stock[-1]}"

    def __repr__(self) -> str:
        return f"{self.stock}"          

    def face_value_up(self) -> bool:
        """Changes every card face value in the stack to true"""
        for card in self.stock:
            if not card.face_value:
                card.change_face_value()

    def remove_top_card(self) -> "Card":
        return self.stock.pop(-1)


class Foundations:
    """Represents the foundations of a solitaire deck"""

    def __init__(self) -> None:
        self.piles = {
            'Spades': [ ],
            'Clubs': [ ],
            'Diamonds': [ ],
            'Hearts': [ ]
        }

    def __str__(self) -> str:
        display_cards = []
        for suit in self.piles:
            display_cards.append(str(suit[-1]))

    def play_to_foundation(self, card: Card):
        """Checks if a card can be played on the foundations, moves card if possible. Does not remove card from stock or stack"""
        suit = card.suit
        rank = card.rank_number
        top_card = self.piles[suit][-1] if self.piles[suit] else None  # Get the top card in the
        if top_card == None and rank == 1:
            self.piles[suit].append(card) 
        elif top_card.rank_number == rank - 1:
            self.piles[suit].append(card)
        else:
            print("Sorry, that is not a valid move")


class Stack:
    def __init__(self, deck: list[Card], num_cards): 
        self.row = []
        for card in range(num_cards):
            self.row.append(deck.deck.pop())
    
    def __len__(self):
        return len(self.row)
    
    def __iter__(self): # Not really sure about this one. Gonna have to ask someone
        for card in self.row:
            yield card

    def __getitem__(self, index):
        return self.row[index]

    def flip_bottom_card(self) -> Card:
        bottom_card = self.row[-1]
        # print(self.row[-1])
        if bottom_card.face_value == False:
            bottom_card.change_face_value()

    def first_playable_card(self):
        for idx, card in enumerate(self.row):
            if card.face_value:
                return idx  # Return index of the first face-up card
        return None  # Returns None if no face-up cards found
    
    def find_bottom_card(self):
        """ returns the bottom non-empty card index"""
        for idx, card in enumerate(self.row):
            if card.is_blank:
                return idx
        return None


class Tableau:
    """
    Represents the tableau in a game of Solitaire, which is the main layout where most of the gameplay takes place.
    
    The tableau consists of a number of piles of cards, with the top card of each pile being face up and the rest face down. 
    Cards can be moved between piles according to certain rules, with the goal of eventually moving them to the foundation piles.
    
    Attributes:
        tableau (list): A list of lists representing the rows of the tableau.
        stack (list): A list representing the remaining deck of cards after building the tableau.
    
    Methods:
        __init__: Constructs the tableau by dealing cards from the deck into piles.
        print_columns: Transposes the tableau for column-wise display.
        __str__: Returns a string representation of the tableau for printing.
        __repr__: Returns a string representation of the object for debugging.
        adjust_length: Ensures all rows in the tableau have the same length by adding blank cards as needed.
    """

    def __init__(self, deck) ->  None:
        """Constructs the tableau by dealing cards from the deck into piles."""
        self.tableau = []
        self.num_rows = 0
        self.stock = []
        self.foundations = Foundations()

        self.build_tableau(deck)

        self.flip_bottom_cards()
        self.adjust_length()

    def build_tableau(self, deck) -> None:
        """Builds the tableau by dealing cards from the deck into piles. Initiates the foundations."""
        for i in range(1, 8):
            column = Stack(deck, i)
            self.tableau.append(column)

        for i in range(len(deck.deck)):
            card = deck.deck[i]
            self.stock.append(card)

        self.stock.insert(0, Card(-1, -1)) # Empty card
        self.stock = Stock(self.stock)
    
def __str__(self) -> str:
    """
    Transposes the tableau for column-wise display and returns a string representation.
    
    Returns:
        str: A string representation of the tableau columns.
    """
    # Transpose the tableau to get columns
    columns = list(map(list, zip(*self.tableau)))
    # Create a string to represent the tableau
    column_labels = [" ", "Column 1", "Column 2", "Column 3", "Column 4", "Column 5", "Column 6", "Column 7"]
    
    column_str = ""
    for column in column_labels:
        if column == " ":
            column_str += f"{'':<15}"
        else:   
            column_str += f"{(column):<20}"
    print(column_str)
    print("\n")

    # Define a dashed line separator
    total_width = len(column_labels) * 20  # Total width based on column spacing
    dashed_line = "-" * total_width + "\n"

    row_num = 1
    row_lengths = []
    tableau_str = ""
    
    for col in columns:
        tableau_str += f"Row {row_num:<5} | "
        for card in col:
            # Format each card for consistent spacing, using the card's __str__ representation
            tableau_str += f"{str(card):<20}"
        tableau_str += "\n"  # Newline after each row
        tableau_str += dashed_line  # Add dashed line after each row
        
        row_lengths.append(row_num)
        row_num += 1

    self.num_rows = max(row_lengths)
    return tableau_str

    
    def __getitem__(self, key):
        """'Magic Method': Allows for indexing a column from the Tableau"""
        return self.tableau[key]
    
    def update(self):
        """Updates tableau column lengths to match"""
        self.adjust_length()
        self.flip_bottom_cards()

    def flip_bottom_cards(self) -> None:
        """Flips the bottom card in the stack."""
        for row in self.tableau:
            row.flip_bottom_card()

    def adjust_length(self):
        max_len = max([len(row) for row in self.tableau])
        for i in range(len(self.tableau)):
            for j in range(max_len - len(self.tableau[i])):
                self.tableau[i].row.append(Card(-1, -1))