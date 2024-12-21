# I believe all i need to do is implement the move validation logic and the actual make move logic

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
        self.grab_type = None
        self.place_type = None

        # Initialize the grab and place locations for tableau.
        self.grab_column = None
        self.grab_row = None
        self.place_column = None
        self.place_row = None

        # Initialize the grab and place locations for foundation.
        self.grab_suite = None
        self.place_suit = None

        # Each Category has a different set of options for placing the card.
        self.place_types = None

        self.class_types = {
            'stock': MoveStock,
            'tableau': MoveTableau,
            'foundation': MoveTableau
            }
        self.place_types = self.class_types.copy()
        
        
    def request_move(self):
        move_input = input("Where would you like to grab from? [Tableau, Stock, Foundation]: ").lower()

        if move_input not in self.class_types.keys():
            print('Sorry, that is not a valid option')
            return
        
        # Initialize the grab process, we will ask where they would like to place in the req_loc_place
        self.grab_type = self.class_types[move_input](self.tableau)

        self.grab_type.req_loc_grab()
        key_str = ', '.join(self.grab_type.place_types.keys())
        self.place_type = input(
            f"Where would you like to place the card? [{key_str}]: "
            ).strip().lower()

    
class MoveTableau(Grab):
    def __init__(self, tableau):
        super().__init__(tableau)
        del self.place_types['stock']

    def req_loc_grab(self):
        self.column = int(input('What column would you like to grab from?'))
        self.row = int(input('What row would you like to grab from'))

    def req_loc_place(self):
        self.place_column = int(input("What column would you like to place onto?"))


class MoveStock(Grab):
    def __init__(self, tableau):
        super().__init__(tableau)
        del self.place_types['stock']

    def req_loc_grab(self): # Not needed for stock.
        pass

    def req_loc_place(self):
        place_type = input("Where would you like to place the card? [Tableau, Foundation]: ").lower()


class MoveFoundation(Grab):
    def __init__(self, tableau):
        super().__init__(tableau)
        del self.place_types['foundation', 'stock']

    def req_loc_grab(self):
        self.grab_suit = str(input('What suit would you like to grab from?'))

    def req_loc_place(self): # Not needed for foundation.
        pass



"""
Outline of my operations methods:

    Card Methods:
    - is_playable(self, other_card: "Card") -> bool
    - is_playable_foundation(self, other: "Card") -> bool

    Stock Methods:
    - flip_stock(self)
    - remove_card(self)

    Foundation Methods: 
    - remove_card(self, card) # Probably need to change to suite input.
    - play_card(self, card)

    Tableau Methods:
    - remove_card(self, column, row)
    - play_card(self, column, card)

            self.options = {
            'stock': ['tableau', 'foundation'],
            'tableau': ['tableau', 'foundation'],
            'foundation': ['tableau']
            }

"""