# from cards import Card

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

        self.grab_column = None
        self.grab_row = None

        self.grab_suite = None

        self.class_types = {
            'stock': MoveStock,
            'tableau': MoveTableau,
            'foundation': MoveTableau
            }
        move_input = input("Where would you like to grab from? [Tableau, Stock, Foundation]: ").lower()

        if move_input not in self.class_types.keys():
            print('Sorry, that is not a valid option')
            return
        self.move_type = self.options[move_input]()
    

class MoveTableau(Grab):
    def __init__(self):
        super().__init__()

    def req_loc_grab(self):
        self.column = int(input('What column would you like to grab from?'))
        self.row = int(input('What row would you like to grab from'))

    def req_loc_place(self):
        self.place_column = int(input("What column would you like to place onto?"))


class MoveStock(Grab):
    def __init__(self):
        super().__init__()

    def req_loc_grab(self): # Not needed for stock.
        pass

    def req_loc_place(self):
        place_type = input("Where would you like to place the card? [Tableau, Foundation]: ").lower()


class MoveFoundation(Grab):
    def __init__(self):
        super().__init__()

    def req_loc_grab(self):
        self.grab_suit = str(input('What suit would you like to grab from?'))

    def req_loc_place(self):
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