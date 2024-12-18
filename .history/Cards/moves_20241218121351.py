class FlipStock:
    def __init__(self, tableau):
        self.tableau = tableau
        self.stock = tableau.stock.stock
    
    def is_valid(self):
        if self.stock:
            return True
        return False
    
    def execute(self):
        if self.is_valid():
            card = self.stock.pop(-1)
            self.stock.insert(0, card)

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

        self.card_pos = None
        self.move_pos = None

        move = self.req_move_type()
        move.run(self.tableau)

    @classmethod
    def run(cls, tableau):
        object = cls(tableau)
        object.get_coords()
        if object.is_valid():
            object.ex
            

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
        
        return move_set[move_choice]

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
    pass



class GrabFoundation(Grab):
    """
    Removes a card from the foundation, if your rules allow it.
    Typically, solitaire doesn't let you remove cards from the foundation,
    but if your variant does, implement that logic here.
    """
    pass

class GrabTableau(Grab):
    pass

class GrabStack(GrabTableau):
    pass


class GrabCard(GrabTableau):
    pass

# req_move, is_valid, execute