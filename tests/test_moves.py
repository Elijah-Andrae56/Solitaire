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
