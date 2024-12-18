"""
Elijah Andrae
04/5/2024
Solitaire Game, Board build"""


import random


class BuildDeck():
    """A class to create and shuffle a deck of cards for a solitaire game.

    The deck is represented as a list of tuples, where each tuple consists of
    two elements: the suit and the rank of a card.

    Attributes:
        deck (list of tuples): The deck of cards used for the solitaire game.

    Methods:
        __init__: Initializes a new deck and shuffles it.
        __str__: Returns a string representation of the deck.
        generate_deck: Generates a standard deck of 52 playing cards."""

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
            for rank in range(1, 14):
                card = [suit, rank]
                deck.append(card)

        return deck
    

class Card():
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
    def __init__(self, card: tuple) -> None:
       # Set the default values for a blank card
        self.is_blank = True
        self.suit = None
        self.rank = None
        self.color = None
        self.face_value = None
        self.suit_number = None
        self.rank_number = None
        if card != " ":
            """If the input is not a blank card, then decode it and set its attributes."""
            self.is_blank = False
            self.suit, self.rank = self.decode_card(card)
            self.face_value = False # Default to face down
            self.color = self.assign_color()
            self.suit_number = card[0] # 0-3 for spades, hearts, diamonds, clubs
            self.rank_number = card[1] # 1-13 for Ace, 2-13 for two, etc.


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
        """Returns a string representation of the card."""

        if self.is_blank:
            return " "
        elif not self.face_value:
            return "*"
        else:
            return f"{self.rank} of {self.suit}"
        

    def decode_card(self, card: list) -> tuple:
        """Decodes the deck."""

        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

        # Decode the card.
        suit = suits[card[0]]
        rank = ranks[card[1] - 1]

        # Create a new card object with the decoded values.
        return suit, rank
    
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
    

class Stock():
    """Represents the stack of remaining cards left in a solitaire deck. Ment to be iterated through, and generated in the When the """
    
    def __init__(self, stack: list) -> None:
        """Creates a new stack"""
        self.stack = stack
        self.face_value_up()

    def __str__(self) -> str:
        return f"The current card is: {self.stack[-1]}"

    def __repr__(self) -> str:
        return f"{self.stack}"

    def flip_stack(self) -> list:
        """Flips the stack."""
        if self.stack: # Check if the stack is empty
            card = self.stack.pop(-1)
            self.stack.insert(0, card)
            print(f"The current card is: {self.stack[-1]}")

    def face_value_up(self) -> bool:
        """Changes every card face value in the stack to true"""
        for card in self.stack:
            if not card.face_value:
                card.change_face_value()

    def remove_top_card(self) -> "Card":
        return self.stack.pop(-1)


class Foundations():
    """Represents the foundations of a solitaire deck"""

    def __init__(self) -> None:
        self.piles = {
            'Spades': [ ],
            'Clubs': [ ],
            'Diamonds': [ ],
            'Hearts': [ ]
        }


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



class Tableau():
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
        for i in range(1, 8):
            row = []
            for j in range(i):
                card = Card(deck.deck.pop(0))   
                row.append(card)
            self.tableau.append(row)
        self.stack = []
        for i in range(len(deck.deck)):
            card = Card(deck.deck[i])
            self.stack.append(card)
        
        self.stack.insert(0, Card(" "))  
        self.stack = Stock(self.stack)
        
        self.flip_bottom_cards()

        self.adjust_length()

        print(self.tableau)


    def print_columns(self) -> str:
        """
        Transposes the tableau for column-wise display and returns a string representation.
        
        Returns:
            str: A string representation of the tableau columns.
        """
        #self.adjust_length()
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
    
    def __str__(self) -> str:
        return self.print_columns()


    def flip_bottom_cards(self) -> None:
        """Flips the bottom card in the stack."""
        for row in self.tableau:
            if row:
                #print(row)
                row[-1].face_value = True


    def adjust_length(self):
        max_len = max([len(row) for row in self.tableau])
        for i in range(len(self.tableau)):
            for j in range(max_len - len(self.tableau[i])):
                self.tableau[i].append(Card(" "))


    def find_bottom_card(self, column_number: int):
        column = self.tableau[column_number - 1]
        for i in range(len(column)):
            if column[i].is_blank:
                return i - 1 if i > 0 else None  # Return the index of the last non-blank card or None if the column is empty
        return len(column) - 1  # If no blank cards, return the index of the last card
    

    def move_from_stock(self):
        top_stock_card = self.stack.stack[-1]
        
        # Move the card from the current column to the new column
        column_num = int(input("What column would you like to move the stack card to (1-7): "))
        if column_num > 7 or column_num < 1:
            print("Invalid Column Number")
            return
        
        target_column = self.tableau[column_num - 1]
        bottom_card_idx = self.find_bottom_card(column_num)
 
        print(top_stock_card.is_playable(target_column[bottom_card_idx]))

        if bottom_card_idx is None or top_stock_card.is_playable(target_column[bottom_card_idx]):
            card = self.stack.remove_top_card()
            insert_index = bottom_card_idx + 1 if bottom_card_idx is not None else 0
            self.tableau[column_num-1].insert(insert_index, card)
        else:
            print("Cannot move card")


    def move_stack(self):
        try:
            col_src, row_src = map(int, input("Enter source column, row (e.g., 3,1): ").split(','))
            col_tgt = int(input("Enter target column 1-7: "))
        except ValueError:
            print("Invalid input. Please provide numbers only.")
            return
        
        if col_src > 7 or col_src < 1 or col_tgt > 7 or col_tgt < 1:
            print("Column numbers must be between 1 and 7.")
            return
        
        source_column = self.tableau[col_src - 1]
        print(source_column)
        target_column = self.tableau[col_tgt - 1]

        # bottom_card_idx = self.find_bottom_card(col_number)

        # if col_number > 7 or col_number < 1:   # Checking to see if coordinates are valid
        #     print("Invalid Column Number")
        #     return
        # print(f'The bottom ndex is {bottom_card_idx}')
        # if row_number < 1 or row_number > bottom_card_idx:   # Checking to see if coordinates are valid
        #     print("Invalid Row Number")
        #     return
        
        # target_column = self.tableau[col_number - 1] # Grabbing the column of the cards we want to move

        # if target_column is None:  # Making sure not an empty column
        #     print("Invalid Column Number")
        #     return
        
        # cards_to_move = target_column[row_number - 1:] # Selecting cards we want from the target column

        # new_column_idx = int(input('Please enter the column you would like to move the selected stack to'))
        # new_column = self.tableau[new_column_idx - 1]
        
        # top_in_old_col = cards_to_move[0] # Grabbing the top card in the old column
        # print(top_in_old_col)
        # bottom_idx_new_col = self.find_bottom_card(new_column)
        # bottom_card_new_col = self.tableau[new_column_idx - 1][bottom_idx_new_col]

        # if top_in_old_col.is_playable(bottom_idx_new_col): # Checking to see if the top card is playable
        #     pass


        ## ask for new column
        ## if possible move, move selection to new row and delete old selection
        ## Check if possible with card.is_playable() 
        ## flip bottom card on old column if necissary
        

class SolitaireGame:

    def __init__(self):
        self.deck = BuildDeck()
        self.tableau = Tableau(self.deck)
        self.game_on = True
        print(self.tableau)

    def request_move(self):
        input_options = {
                "flip": self.tableau.stack.flip_stack,
                "move card": self.tableau.move_from_stock,
                # "move foundation": pass
                "move stack": self.tableau.move_stack
                }
        user_input = input("What would you like to do: ").lower()
        action = input_options.get(user_input)
        if action:
            action()
        else:
            print('Sorry, that is not a valid option')

    def run(self):
        while self.game_on:
            self.request_move()
            print(self.tableau)


def main():
    game = SolitaireGame()
    game.run()


if __name__ == "__main__":
    main()
        
        


""" 
Needed: 
    - Way to move cards to foundation and vice versa
    - Way to move stacks of cards to other stacks
    - Uncover top card when stack is moved
    - End game when done"""



