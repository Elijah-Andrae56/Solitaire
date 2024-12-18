# class MoveSet:
#     class Move:
#         """Abstract base class for the solitaire MoveSet"""
#         def __init__(self, tableau):
#             self.tableau = tableau
#             self.stock = tableau.stock.stock

#         def is_valid(self):
#             raise NotImplementedError()
        
#         def execute(self):
#             raise NotImplementedError()
        
#         def get_coords(self):
#             raise NotImplementedError()


#     class FlipStock(Move):
#         def __init__(self, tableau):
#             super().__init__(tableau)
        
#         def is_valid(self):
#             if self.stock:
#                 return True
#             return False
        
#         def execute(self):
#             if self.is_valid():
#                 card = self.stock.pop(-1)
#                 self.stock.insert(0, card)


#     class MoveFromStock(Move):
#         """Move a card from the stock to the tableau"""
#         def __init__(self, tableau):
#             super().__init__(tableau)

#         def get_coords(self):
#             column_num = int(input("What column would you like to move the stack card to (1-7): "))
#             if column_num > 7 or column_num < 1:
#                 print("Invalid Column Number")
#                 return  # FIXME : Need to find way to tell rest of code its wrong input
#             return column_num
        
#         def is_valid(self, target_column, bottom_card_idx, top_stock_card) -> bool:
#             if bottom_card_idx is None and top_stock_card.rank == 'King':
#                 return True
#             elif top_stock_card.is_playable(target_column[bottom_card_idx]):
#                 return True
#             print('Cannot move card.')
#             return False
        
#         def execute(self):
#             top_stock_card = self.stock[-1] if self.stock else None
#             move_col = self.get_coords()
#             target_column = self.tableau.tableau[move_col-1]

#             bottom_card_idx = self.tableau[move_col].find_bottom_card()
#             if self.is_valid(target_column, bottom_card_idx, top_stock_card):
#                 card = self.tableau.stock.remove_top_card()
#                 insert_index = bottom_card_idx + 1 if bottom_card_idx is not None else 0
#                 target_column.row.insert(insert_index, card)
    
#     class Position:
#         def __init__(self, col=None, row=None):
#             self.col = col
#             self.row = row
#             self.idx_col = col - 1 if col else None
#             self.idx_row = row - 1 if row else None

#     class GrabStack(Move):
#         """Grabs from a specified point in the Tableau, determines if holding a singular card or a stack, calls either MoveStack or MoveSingularCard"""
        
#         def __init__(self, tableau):
#             super().__init__(tableau)
#             self.src = MoveSet.Position()
#             self.tgt = MoveSet.Position()
            
#         def get_coords(self):
#             try:
#                 col_src, row_src = map(int, input("Enter source column, row (e.g., 3,1): ").split(','))
#                 col_tgt = int(input("Enter target column 1-7: "))
#                 if col_src not in range(1, 8) or col_tgt not in range(1, 8):
#                     print("Column numbers must be between 1 and 7")
#                     return
                
#                 first_playable = self.tableau.tableau[col_src - 1].first_playable_card()
#                 if first_playable is None:
#                     print ("No playable cards in this column")
#                     return
#                 bottom_card_idx = self.tableau[col_src - 1].find_bottom_card()
#                 if bottom_card_idx is None:
#                     print("Invalid column")
#                     return
#                 row_grabbable_cards = range(first_playable, bottom_card_idx + 1) if bottom_card_idx >= first_playable else range(first_playable, first_playable + 1)
                
#                 print(row_grabbable_cards)
#                 if row_src not in row_grabbable_cards:
#                     print("Invalid row number")
#                     return
#                 self.col_src = col_src
#                 self.row_src = row_src
#                 self.col_tgt = col_tgt
#                 self.col_src_idx = col_src - 1
#                 self.row_src_idx = row_src - 1
#                 self.col_tgt_idx = col_tgt - 1
                
#             except ValueError:
#                 print("Invalid input. Please provide numbers only.")
#                 return # FIXME
        
#         def is_valid(self):
#             return True
#             # Ensure the coordinates are in the possible ranges of the tableau
#             # Ensure you don't have an unfliped or not a card selected
#             # If those don't work call get coords again

#         def execute(self):
#             self.get_coords()
#             if not self.col_src: return
#             src_column = self.tableau.tableau[self.col_src - 1]
            
#             print(src_column)

#     class MoveStack(GrabStack):
#         """Moves a stack of cards from the tableau to another column"""
#         def __init__(self, tableau):
#             super().__init__(tableau)
#             self.col_src_idx = self.col_src - 1
#             self.row_src_idx = self.row_src - 1
#             self.col_tgt_idx = self.col_tgt - 1

#         def is_valid(self):
#             pass

#         def execute(self):
#             pass

#     class MoveSingularCard(GrabStack):
#         def __init__(self, ):
#             pass
def place_tableau(row, column):
    """Places card or stack of cards onto the tableau. Used in correlation with is_valid before and a method to remove the card from the location after"""

class Grab:
     '''Choose from Stock, Tableau, or Foundations'''
     def __init__(self, tableau):
        move_choice = str(input('Where would you like to grab a your card(s) from? [foundation, stock, tableau]'))
        move_set = {
            'foundation': GrabFoundation,
            'stock': GrabStock,
            'tableau': GrabTableau
        }
        selection = move_set[move_choice]
        self.tableau = tableau
        self.stock = tableau.stock.stock
        
        def get_coords(self):
            raise NotImplementedError()

        def is_valid(self):
            raise NotImplementedError()
        
        def execute(self):
            raise NotImplementedError()

class GrabStock(Grab): '''Grab a card from the stock. Able to move to foundations or onto tableau if playable.'''

class GrabFoundation(Grab): '''Removes a card from the foundation. '''

class GrabTableau(Grab):  
    '''Requests coordinates of card(s) you want to grab from the Tableau. Determines if you have a singular card or multiple.'''
    def __init__(self):
        self.row, self.col = self.get_coords()

    def get_coords(self):
        pass


class GrabStack(GrabTableau): '''Called in GrabTableau. Allows to move a stack of cards onto another eligible stack.'''
class GrabCard(GrabTableau): '''Called in GrabTableau. Allows to mode a singular card onto another stack or onto eligible foundation.'''