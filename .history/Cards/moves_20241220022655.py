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

        self.move_type = None

        self.card = None
        self.other_card = None

        self.card_pos = None
        self.move_pos = None

    @classmethod
    def run(cls, tableau):
        object = cls(tableau)
        object.get_coords()
        if object.is_valid():
            object.execute()

    def move_position(self):
        loc_type = input('Where would you like to place the card [tableau, foundation]').lower()
        responses = {
            'tableau': self.tableau,
            'foundation': self.tableau.foundations
            }
        if loc_type in responses.keys():
            self.move_location = responses[loc_type]
        else:
            print("Sorry that's not a valid response")

        self.card = self.stock[-1] if len(self.stock) > 0 else None
        self.other_card = responses[loc_type].compare_card(self.card)

    def req_move_type(self):
        """Runs the appropriate grab class based on where to grab from."""
        move_choice = input(
        'Where would you like to grab your card(s) from? [foundation, stock, tableau]: '
            ).strip().lower()
        
        move_set = {
            'foundation': GrabFoundation,
            'stock': GrabStock,
            'tableau': GrabTableau
        }

        if move_choice not in move_set:
            print("Invalid choice. Please select 'foundation', 'stock', or 'tableau'.")
            return None
        
        return move_set[move_choice]  # I should build this to ask what card you want on the tableau and where you want to move it to

    def get_coords(self):
        """Get the coordinates or identifiers for the card(s) being grabbed."""
        raise NotImplementedError

    def is_valid(self):
        '''Determine if the move is executable'''
        raise NotImplementedError

    def execute(self):
        """After verifying that the card is playable make the move."""
        raise NotImplementedError


class GrabStock(Grab):
    """
    Grab a card from the stock. You might only have the top card accessible.
    After grabbing, you may place it onto a tableau stack or a foundation stack if valid.
    """
    def __init__(self, tableau):
        super().__init__(tableau)

    def get_coords(self):
        self.move_position()
    
    def is_valid(self):
        if self.stock:
            return True
        return False
    
    def execute(self):
        if self.is_valid():
            card = self.stock.pop(-1)


class GrabFoundation(Grab):
    """
    Removes a card from the foundation, if your rules allow it.
    Typically, solitaire doesn't let you remove cards from the foundation,
    but if your variant does, implement that logic here.
    """
    def __init__(self):
        super().__init__(Grab)

    def get_coords(self):
        self.move_position()
        pass

    def is_valid(self, card: Card):
          """Checks if a card can be played on the foundations, moves card if possible. Does not remove card from stock or stack"""
          suit = card.suit
          rank = card.rank_number

          top_card = self.piles[suit][-1] if self.piles[suit] else None  # Get the top card in the
          if (top_card == None and rank == 1) or (top_card.rank_number == rank - 1):
            return True

          print("Sorry, that is not a valid move")
          return False      

    def execute(self):
        pass
        

class GrabTableau(Grab):
    pass

class GrabStack(GrabTableau):
    pass


class GrabCard(GrabTableau):
    pass

    

# Need to prompt where to grab, what to grab (if needed), where to place.