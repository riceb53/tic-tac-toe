from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
      from tic_tac_toe.game.players import Player
      from tic_tac_toe.logic.models import Grid, GameState, Mark

import re
from tic_tac_toe.logic.exceptions import InvalidGameState
# from tic_tac_toe.models import Grid

def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
            raise ValueError("Must contain 9 cells of space/X/O")

def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(game_state.grid, game_state.starting_mark, game_state.winner)
      
def validate_number_of_marks(grid: Grid) -> None:
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Wrong number of Xs and Os")

def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    if grid.x_count > grid.o_count:
        if starting_mark != 'X':
            raise InvalidGameState("Wrong Starting Mark")
    elif grid.o_count > grid.x_count:
        if starting_mark != 'O':
            raise InvalidGameState("Wrong Starting Mark")            

def validate_winner(grid: Grid, starting_mark: Mark, winner: Mark | None) -> None:
    if winner == 'X':
        if starting_mark == 'X':
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Wrong Number of Xs")  
        else: 
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Wrong Number of Xs")  
    elif winner == 'O':
        if starting_mark == 'O':
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("Wrong Number of Os")  
        else: 
            if grid.o_count != grid.x_count:
                raise InvalidGameState("Wrong Number of Os")  

def validate_players(player1: Player, player2: Player):
    if player1.mark is player2.mark:
        raise ValueError("Players must have different marks")
