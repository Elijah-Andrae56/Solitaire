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

    @classmethod
    def create(cls, tableau):

        


    def get_coords(self):
        """Get the coordinates or identifiers for the card(s) being grabbed."""
        raise NotImplementedError

    def is_valid(self):
        """Check if the chosen card(s) can be legally moved from this location."""
        raise NotImplementedError

    def execute(self):
        """Perform the actual grab and move of the card(s)."""

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
        
        return move_set[move_choice](self.tableau)

class GrabStock(Grab):
    """
    Grab a card from the stock. You might only have the top card accessible.
    After grabbing, you may place it onto a tableau stack or a foundation stack if valid.
    """

    def is_valid(self):
        # Check if the stock is not empty and if it's allowed to move from stock right now.
        return len(self.stock) > 0
    
    def prompt_move(self):
        loc = input('Where would you like to play the card? [tableau, foundations?]')

    def execute(self):
        if not self.is_valid():
            print("No cards available in stock to grab.")
            return
        card = self.stock.pop()  # Grab the top card
        # You'd then prompt or handle where to move this card.
        # This might involve calling another class or method to place the card.


class GrabFoundation(Grab):
    """
    Removes a card from the foundation, if your rules allow it.
    Typically, solitaire doesn't let you remove cards from the foundation,
    but if your variant does, implement that logic here.
    """

    def get_coords(self):
        # Prompt user for which foundation stack and which card (if there's a choice).
        suit_choice = input("Which foundation suit? [Hearts, Diamonds, Clubs, Spades]: ").title()
        return suit_choice

    def is_valid(self):
        suit_choice = self.get_coords()
        # Check if chosen foundation pile and card are removable
        pile = self.foundations.piles.get(suit_choice, [])
        return len(pile) > 0  # For example, if not empty.

    def execute(self):
        suit_choice = self.get_coords()
        if not self.is_valid():
            print("Cannot remove a card from that foundation pile.")
            return
        card = self.foundations.piles[suit_choice].pop()
        # Now you have the card, handle where it goes next (usually tableau).


class GrabTableau(Grab):
    """
    Grabs card(s) from the tableau. This is more complex since you can grab a single card or a stack.
    The logic here would involve:
    - Getting column and row coordinates.
    - Determining if you have a stack or a single card.
    - Based on that, you might delegate to GrabStack or GrabCard.
    """

    def __init__(self, tableau):
        super().__init__(tableau)
        self.col, self.row = self.get_coords()
        # After coordinates are obtained, determine if it's a stack or a single card
        # and potentially re-initialize as GrabStack or GrabCard.

    def get_coords(self):
        # Prompt user for the column and row of the card(s) they want to grab
        try:
            col = int(input("Enter the column number (1-7): "))
            row = int(input("Enter the row number in that column: "))
            return col, row
        except ValueError:
            print("Invalid input, please enter numbers only.")
            return None, None

    def is_valid(self):
        # Validate that col, row point to a playable, face-up card or a stack of cards.
        # This will also help determine if we deal with GrabStack or GrabCard.
        if self.col is None or self.row is None:
            return False
        # Additional logic: check if the chosen card is face-up and if the move is legal
        return True

    def execute(self):
        if not self.is_valid():
            print("Invalid move.")
            return
        # Determine if multiple cards form a stack or just a single card.
        # If multiple cards can be moved, create a GrabStack instance.
        # If a single card, create a GrabCard instance.

        # Example pseudo-logic:
        # is_stack = self.check_if_stack(self.col, self.row)
        # if is_stack:
        #     stack_mover = GrabStack(self.tableau, self.col, self.row)
        #     stack_mover.execute()
        # else:
        #     card_mover = GrabCard(self.tableau, self.col, self.row)
        #     card_mover.execute()


class GrabStack(GrabTableau):
    """
    Called by GrabTableau if multiple cards are selected.
    Moves a stack of cards onto another eligible stack or foundation.
    """
    def __init__(self, tableau, col, row):
        super().__init__(tableau)
        self.col = col
        self.row = row

    def get_coords(self):
        # Might be inherited or overridden, but in this case, coords are already given.
        return self.col, self.row

    def is_valid(self):
        # Check if the block of cards starting at (col, row) is a valid stack move.
        return True

    def execute(self):
        if self.is_valid():
            # Perform the move: remove those cards from the original column, and place them where user wants.
            pass


class GrabCard(GrabTableau):
    """
    Called by GrabTableau if a single card is selected.
    Moves a single card onto another stack or a foundation pile if valid.
    """
    def __init__(self, tableau, col, row):
        super().__init__(tableau)
        self.col = col
        self.row = row

    def get_coords(self):
        # Already have them
        return self.col, self.row

    def is_valid(self):
        # Validate single card move
        return True

    def execute(self):
        if self.is_valid():
            # Move the card
            pass
