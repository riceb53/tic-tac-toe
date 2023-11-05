import pdb

from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.renderers import ConsoleRenderer
from console.players import ConsolePlayer

player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

# pdb.set_trace()

TicTacToe(player1, player2, ConsoleRenderer()).play()
