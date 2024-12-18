from moves import Moveset
from piles import Tableau
from deck import BuildDeck

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