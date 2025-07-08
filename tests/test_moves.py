
import builtins
from unittest import mock

import sys
sys.path.append('Cards')

from deck import BuildDeck
from piles import Tableau
from moves import MoveStock, MoveFoundation


def setup_tableau():
    deck = BuildDeck()
    tableau = Tableau(deck)
    return tableau


def test_move_stock_req_loc_grab_sets_grab_card():
    tableau = setup_tableau()
    move = MoveStock(tableau)
    # before call grab_card is None
    assert move.grab_card is None
    move.req_loc_grab()
    assert move.grab_card is tableau.stock.stock[-1]


def test_move_foundation_req_loc_place_column():
    tableau = setup_tableau()
    move = MoveFoundation(tableau)
    with mock.patch.object(builtins, 'input', return_value='3'):
        move.req_loc_place()
    assert move.place_column == 3
    assert move.place_suit is None


def test_move_foundation_req_loc_place_suit():
    tableau = setup_tableau()
    move = MoveFoundation(tableau)
    with mock.patch.object(builtins, 'input', return_value='Hearts'):
        move.req_loc_place()
    assert move.place_suit == 'Hearts'
    assert move.place_column is None
=======
import sys
from types import SimpleNamespace
sys.path.append('Cards')

from cards import Card
from moves import MoveStock, MoveTableau
from piles import Stack


class DummyTableau:
    def __init__(self, piles):
        self.piles = piles
        self.stock = SimpleNamespace(stock=[])
        self.foundations = {}

    def __getitem__(self, idx):
        return self.piles[idx]


def test_move_stock_removes_card():
    stock_cards = [Card(0, 0), Card(1, 1)]
    tableau = DummyTableau([])
    tableau.stock = SimpleNamespace(stock=stock_cards)
    move = MoveStock(tableau)
    move.find_grab_card()
    assert move.grab_card == stock_cards[-1]
    move.remove_grab_card()
    assert len(stock_cards) == 1


def test_move_tableau_is_valid():
    target_stack = Stack.__new__(Stack)
    target_stack.row = [Card(2, 6), Card(-1, -1)]  # 7 of Spades then blank

    source_stack = Stack.__new__(Stack)
    source_stack.row = [Card(0, 5), Card(-1, -1)]  # 6 of Hearts then blank

    tableau = DummyTableau([target_stack, source_stack])

    move = MoveTableau(tableau)
    move.grab_column = 2
    move.grab_row = 1
    move.grab_tableau_column = tableau[1].row[0]
    move.place_column = 1
    move.place_tab_col = tableau[0]
    move.grab_card = move.grab_tableau_column
    move.place_card = tableau[0].row[0]

    assert move.is_valid()
