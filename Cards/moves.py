# I believe all i need to do is implement the move validation logic and the actual make move logic
from cards import Card
class Grab:
    """
    Base class to choose where to grab cards from: Stock, Foundation, or Tableau.
    This class acts as a factory: it asks the user where they want to grab from,
    and then returns the appropriate specialized Grab object.
    """

    def __init__(self, tableau):
        self.tableau = tableau
        self.stock = tableau.stock.stock
        self.foundations = tableau.foundations

        # Initialize the grab and place types.
        self.grab_type = None # class
        self.place_type = None # class

        # Initialize the grab and place locations for tableau.
        self.grab_column = None # int
        self.grab_row = None # int
        self.place_column = None # int
        self.place_row = None # int


        # Each Category has a different set of options for placing the card.
        self.place_types = None # dict

        # We need to store the cards we need to test in a list. This will allow us to iterate through when moving a stack
        self.grab_card = None # Card
        self.grab_cards = None # List[Card] used for moving stacks on tableau
        self.place_card = None # Card

        # Initialize the grab and place locations for foundation.
        self.grab_suite = None # str
        self.place_suit = None # str

        self.class_types = {
            'stock': MoveStock,
            'tableau': MoveTableau,
            'foundation': MoveFoundation
            }
        self.place_types = self.class_types.copy()

        
    def request_move(self):
        move_input = input("Where would you like to grab from? [tableau, stock, foundation]: ").lower()

        if move_input not in self.class_types.keys():
            print('Sorry, that is not a valid option')
            return
        
        # Initialize the grab process, we will ask where they would like to place in the req_loc_place
        self.grab_type = self.class_types[move_input](self.tableau)

        self.grab_type.req_loc_grab()
        key_str = ', '.join(self.grab_type.place_types.keys())
        place_input = input(
            f"Where would you like to place the card? [{key_str}]: "
            ).strip().lower()
        
        self.place_type = self.place_types[place_input](self.tableau)
        self.place_type.req_loc_place()
        
        self.run_move()
        

    def run_move(self):
        self.grab_type.find_grab_card()
        self.place_type.find_place_card()
        if self.place_type.is_valid():
            self.grab_type.remove_grab_card()
            self.place_type.play_card()


    def req_loc_grab(self): # Not needed for stock.
        raise NotImplementedError

    def req_loc_place(self):
        raise NotImplementedError

    def find_grab_card(self):
        raise NotImplementedError

    def find_place_card(self): # Not needed, cannot place card on stock
        raise NotImplementedError

    def is_valid(self) -> bool:
        raise NotImplementedError
    
    def remove_grab_card(self):
        raise NotImplementedError
        
    def place_card(self): 
        raise NotImplementedError  

class MoveTableau(Grab):
    def __init__(self, tableau):
        super().__init__(tableau)
        del self.place_types['stock']
        self.grab_tableau_column = None
        self.place_tab_col = None

    def req_loc_grab(self):
        self.grab_column = int(input('What column would you like to grab from?: '))
        self.grab_row = int(input('What row would you like to grab from: '))

        self.grab_tableau_column = self.tableau[self.grab_column - 1].row[self.grab_row - 1]

    def req_loc_place(self):
        self.place_column = int(input("What column would you like to place onto? "))
        print(self.place_column)

    def find_grab_card(self):
        self.grab_card = self.grab_tableau_column
        
    def find_place_card(self):
        self.place_tab_col = self.tableau[self.place_column-1]#.row
        bottom_idx = self.place_tab_col.find_bottom_card()
        self.place_card = self.place_tab_col[bottom_idx]

    def is_valid(self) -> bool:
        return self.grab_card.is_playable(self.place_card)
    
    def remove_grab_card(self):
        grab_column = self.tableau[self.grab_column - 1].row
        self.grab_card = grab_column[self.grab_row - 1:]
        del grab_column[self.grab_row - 1:]

    def play_card(self):
        bottom_idx = self.place_tab_col.find_bottom_card()
        self.grab_tableau_column.insert(bottom_idx, self.grab_card)


class MoveStock(Grab):
    def __init__(self, tableau):
        super().__init__(tableau)
        del self.place_types['stock']

    def req_loc_place(self):
        place_type = input("Where would you like to place the card? [tableau, foundation]: ").lower()

    def req_loc_grab(self):
        """Automatically select the next card from the stock."""
        if self.stock:
            # The playable stock card is always the last one in the list
            self.grab_card = self.stock[-1]

    def find_grab_card(self):
        self.grab_card = self.stock[-1]

    def remove_grab_card(self):
        self.stock.pop(-1)


class MoveFoundation(Grab):
    def __init__(self, tableau):
        super().__init__(tableau)
        del self.place_types['stock']


    def req_loc_grab(self):
        self.grab_suit = str(input('What suit would you like to grab from?'))

    def req_loc_place(self):
        """Ask the user where the grabbed card should be placed."""
        destination = input(
            "Enter tableau column number or foundation suit to place the card: "
        ).strip()

        if destination.isdigit():
            self.place_column = int(destination)
            self.place_suit = None
        else:
            self.place_suit = destination
            self.place_column = None

    def find_grab_card(self):
        self.grab_card = self.foundations[self.grab_suit][-1]

    def find_place_card(self):
        place_suite = self.grab_card.suit
        self.place_card = self.foundations[place_suite][-1]

    def is_valid(self) -> bool:
        return self.grab_card.is_playable(self.place_card)

    def remove_grab_card(self):
        self.foundations[self.grab_suit].pop(-1)

    def play_card(self):
        self.foundations[self.place_card.suit].append(self.grab_card)
