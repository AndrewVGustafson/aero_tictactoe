from .base_grid import BaseGrid
from .base_models import PlayerSymbol, TileLocation, TileStatus, Player

from abc import ABC, abstractmethod

class BaseTicTacToe(ABC):
    def __init__(self) -> None:
        self.grid = BaseGrid()
        self.player1 = Player(num=1, symbol=PlayerSymbol.NULL)
        self.player2 = Player(num=2, symbol=PlayerSymbol.NULL)

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def do_move(self):
        pass
    
    # @abstractmethod
    # def get_move(self):
    #     pass
    
    @abstractmethod
    def setup_game(self):
        pass
    
    @abstractmethod
    def setup_players(self):
        pass

    def check_win(self) -> PlayerSymbol:
        rows = self.grid.get_rows()
        cols = self.grid.get_columns()
        diagonals = self.grid.get_diagonals()

        possible_lines = [rows, cols, diagonals]

        for lines in possible_lines:
            if winner := self._check_lines(lines):
                return winner
            
        if self._check_tie():
            return PlayerSymbol.NULL
        
    def _check_tie(self) -> bool:
        tiles = self.grid.get_tile_statuses()
        tiles = tiles[0] + tiles[1] + tiles[2]
        
        if TileStatus.EMPTY not in tiles:
                return True
        return False

    def _check_lines(self, lines: list) -> PlayerSymbol:
        for line in lines:
            if TileStatus.EMPTY in line:
                continue
            if len(set(line)) == 1:
                winner = self.tile_to_player_symbol(line[0])
                return winner

    def tile_to_player_symbol(self, tile_status: TileStatus) -> PlayerSymbol:
        assert tile_status != TileStatus.EMPTY
        if tile_status == TileStatus.CIRCLE:
            return PlayerSymbol.Circle
        elif tile_status == TileStatus.CROSS:
            return PlayerSymbol.Cross
        
    def player_symbol_to_tile(self, player_symbol: PlayerSymbol) -> TileStatus:
        if player_symbol == PlayerSymbol.Circle:
            return TileStatus.CIRCLE
        elif player_symbol == PlayerSymbol.Cross:
            return TileStatus.CROSS
    
    def set_move(self, location: TileLocation, symbol: PlayerSymbol):
        tile_status = self.player_symbol_to_tile(symbol)
        self.grid.set_tile(location=location, status=tile_status)

    def is_empty(self, location: TileLocation) -> bool:
        return self.grid.get_tile(location).status == TileStatus.EMPTY
    
    def opposite_player(self, player: Player) -> Player:
        if player.num == 1:
            return self.player2
        elif player.num == 2:
            return self.player1

    def switch_turns(self) -> None:
        assert self.player1.has_turn != self.player2.has_turn
        if self.player1.has_turn:
            self.player1.has_turn = False
            self.player2.has_turn = True
        elif self.player2.has_turn:
            self.player2.has_turn = False 
            self.player1.has_turn = True