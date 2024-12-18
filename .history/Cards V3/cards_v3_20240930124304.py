"""
Elijah Andrae
04/5/2024
Solitaire Game, Board build
"""


import random


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

    def __init__(self, deck: BuildDeck) ->  None:
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

        row_num = 1
        row_lengths = []
        tableau_str = ""
        for col in columns:
            tableau_str += f"Row {row_num:<5} | "
            for card in col:
                # Format each card for consistent spacing, using the card's __str__ representation
                tableau_str += f"{str(card):<20}"
            tableau_str += "\n"  # Newline after each column
            
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


class Moveset:
    class Move:
        """Abstract base class for the solitaire moveset"""
        def __init__(self, tableau):
            self.tableau = tableau
            self.stock = tableau.stock.stock

        def is_valid(self):
            raise NotImplementedError()
        
        def execute(self):
            raise NotImplementedError()
        
        def get_coords(self):
            raise NotImplementedError()


    class FlipStock(Move):
        def __init__(self, tableau):
            super().__init__(tableau)
        
        def is_valid(self):
            if self.stock:
                return True
            return False
        
        def execute(self):
            if self.is_valid():
                card = self.stock.pop(-1)
                self.stock.insert(0, card)


    class MoveFromStock(Move):
        """Move a card from the stock to the tableau"""
        def __init__(self, tableau):
            super().__init__(tableau)

        def get_coords(self):
            column_num = int(input("What column would you like to move the stack card to (1-7): "))
            if column_num > 7 or column_num < 1:
                print("Invalid Column Number")
                return  # FIXME : Need to find way to tell rest of code its wrong input
            return column_num
        
        def is_valid(self, target_column, bottom_card_idx, top_stock_card) -> bool:
            if bottom_card_idx is None and top_stock_card.rank == 'King':
                return True
            elif top_stock_card.is_playable(target_column[bottom_card_idx]):
                return True
            print('Cannot move card.')
            return False
        
        def execute(self):
            top_stock_card = self.stock[-1] if self.stock else None
            move_col = self.get_coords()
            target_column = self.tableau.tableau[move_col-1]

            bottom_card_idx = self.tableau[move_col].find_bottom_card()
            if self.is_valid(target_column, bottom_card_idx, top_stock_card):
                card = self.tableau.stock.remove_top_card()
                insert_index = bottom_card_idx + 1 if bottom_card_idx is not None else 0
                target_column.row.insert(insert_index, card)
    class Position:
        def __init__(self, col=None, row=None):
            self.col = col
            self.row = row
            self.idx_col = col - 1 if col else None
            self.idx_row = row - 1 if row else None

    class GrabStack(Move):
        """Grabs from a specified point in the Tableau, determines if holding a singular card or a stack, calls either MoveStack or MoveSingularCard"""
        
        def __init__(self, tableau):
            super().__init__(tableau)
            self.src = Position()
            self.tgt = Position()
            
        def get_coords(self):
            try:
                col_src, row_src = map(int, input("Enter source column, row (e.g., 3,1): ").split(','))
                col_tgt = int(input("Enter target column 1-7: "))
                if col_src not in range(1, 8) or col_tgt not in range(1, 8):
                    print("Column numbers must be between 1 and 7")
                    return
                
                first_playable = self.tableau.tableau[col_src - 1].first_playable_card()
                if first_playable is None:
                    print ("No playable cards in this column")
                    return
                bottom_card_idx = self.tableau[col_src - 1].find_bottom_card()
                if bottom_card_idx is None:
                    print("Invalid column")
                    return
                row_grabbable_cards = range(first_playable, bottom_card_idx + 1) if bottom_card_idx >= first_playable else range(first_playable, first_playable + 1)
                
                print(row_grabbable_cards)
                if row_src not in row_grabbable_cards:
                    print("Invalid row number")
                    return
                self.col_src = col_src
                self.row_src = row_src
                self.col_tgt = col_tgt
                self.col_src_idx = col_src - 1
                self.row_src_idx = row_src - 1
                self.col_tgt_idx = col_tgt - 1
                
            except ValueError:
                print("Invalid input. Please provide numbers only.")
                return # FIXME
        
        def is_valid(self):
            return True
            # Ensure the coordinates are in the possible ranges of the tableau
            # Ensure you don't have an unfliped or not a card selected
            # If those don't work call get coords again

        def execute(self):
            self.get_coords()
            if not self.col_src: return
            src_column = self.tableau.tableau[self.col_src - 1]
            
            print(src_column)

    class MoveStack(GrabStack):
        """Moves a stack of cards from the tableau to another column"""
        def __init__(self, tableau):
            super().__init__(tableau)
            self.col_src_idx = self.col_src - 1
            self.row_src_idx = self.row_src - 1
            self.col_tgt_idx = self.col_tgt - 1

        def is_valid(self):
            pass

        def execute(self):
            pass

    class MoveSingularCard(GrabStack):
        def __init__(self, ):
            pass
    
            
class SolitaireGame:

    def __init__(self):
        self.deck = BuildDeck()
        self.tableau = Tableau(self.deck)
        self.game_on = True
        self.execute_action(Moveset.FlipStock)

    def request_move(self):
        input_options = {
                "flip": lambda: self.execute_action(Moveset.FlipStock),
                "move stock": lambda: self.execute_action(Moveset.MoveFromStock),
                "grab": lambda: self.execute_action(Moveset.GrabStack),
                }
        
        user_input = input("What would you like to do: ").lower()
        action = input_options.get(user_input)
        if action:
            action()
        else:
            print('Sorry, that is not a valid option')

    def execute_action(self, action_class):
        """Create an instance of MoveFromStock with current Tableau"""
        move_action = action_class(self.tableau)
        move_action.execute()

    def run(self):
        while self.game_on:
            print(self.tableau)
            print(f"The current card is: {self.tableau.stock.stock[-1]}")
            self.request_move()
            self.tableau.update()
            

def main():
    game = SolitaireGame()
    game.run()


if __name__ == "__main__":
    main()