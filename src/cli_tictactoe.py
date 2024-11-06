from .grid import Grid
from .base.base_models import TileStatus, TileLocation, BaseTile

class TicTacToe:
    def __init__(self) -> None:
        self.grid = Grid()

    def start_game() -> None:
        print("Player 1, choose your starting ")