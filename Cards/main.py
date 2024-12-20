from moves import FlipStock, Grab
from piles import Tableau
from deck import BuildDeck

class SolitaireGame:

    def __init__(self):
        self.deck = BuildDeck()
        self.tableau = Tableau(self.deck)
        self.game_on = True
        self.tableau.stock.flip_stock()

    def request_move(self):
        input_options = {
                "flip": lambda: self.tableau.stock.flip_stock(),
                "grab": lambda: self.execute_action(Grab),
                }
        
        user_input = input("What would you like to do [flip or grab]: ").lower()
        action = input_options.get(user_input)
        if action:
            action()
        else:
            print('Sorry, that is not a valid option')

    def execute_action(self, action_class):
        """Create an instance of MoveFromStock with current Tableau"""
        move_class = action_class(self.tableau)
        move_type = move_class.req_move_type()
        move_type.run(self.tableau)

    def run(self):
        while self.game_on:
            print(self.tableau)
            print(f"The current stock card is: {self.tableau.stock.stock[-1]}" +
                  f"Foundations: {self.tableau.foundations}")
            self.request_move()
            self.tableau.update()
            

def main():
    game = SolitaireGame()
    game.run()


if __name__ == "__main__":
    main()