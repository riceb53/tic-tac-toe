import abc
import time
import random

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import Mark, GameState, Move

class Player(metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark) -> None: 
        self.mark = Mark

    
    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No possible moves")
        else:
            raise InvalidMove("It's the other player's turn")
        
    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """return current player's move in given game state"""

class ComputerPlayer(Player, metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark, delay_seconds: float = 0.25) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds
    
    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)
    
    @abc.abstractmethod
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """return computer's move in any game state"""

    
class RandomComputerPlayer(ComputerPlayer):
    def get_computer_move(self, game_state: GameState) -> Move | None:
        try: 
            return random.choice(game_state.possible_moves)
        except IndexError:
            return None
    
    