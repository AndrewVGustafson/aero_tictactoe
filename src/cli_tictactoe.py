from grid import Grid
from base.base_models import PlayerSymbol, TileLocation, TileStatus, BasePlayer

# TODO Fix issue where choosing symbol input: 2 [ENTER] x
# maybe use a while loop + match statement
# check other programs to see if that issue exists

class Player(BasePlayer):
    pass

class TicTacToe:
    def __init__(self) -> None:
        self.grid = Grid()
        self.player1: Player
        self.player2: Player

    def start_game(self) -> None:
        self._setup_players()
        self.do_move(self.player1)
        self.do_move(self.player2)
        self.do_move(self.player1)
        self.do_move(self.player2)
        
    def do_move(self, player: Player) -> None:
        print("Current Board")
        self.grid.print_board()
        print(f"\n{player.symbol.name}'s turn.")
        location = self.get_move()
        self.set_move(location, symbol=player.symbol)
        self._switch_turns()

    def get_move(self) -> TileLocation:
        row = self._get_row()
        col = self._get_col()
        location = TileLocation(row=row, column=col)
        if self._is_empty(location):
            return location
        else:
            print("Tile is full, try again.")
            self.get_move()
    
    def set_move(self, location: TileLocation, symbol: PlayerSymbol):
        self.grid.set_tile(location=location, status=symbol)


    def _is_empty(self, location: TileLocation) -> None:
        return self.grid.get_tile(location).status == TileStatus.EMPTY
        
    def _get_row(self) -> int:
        row  = int(input("Enter row: "))
        if row not in range(1, 4):
            self._get_row()
        return row - 1

    def _get_col(self) -> int:
        col  = int(input("Enter column: "))
        if col not in range(1, 4):
            self._get_col()
        return col - 1

    def _switch_turns(self) -> None:
        assert self.player1.has_turn != self.player2.has_turn
        if self.player1.has_turn:
            self.player1.has_turn = False
            self.player2.has_turn = True
        elif self.player2.has_turn:
            self.player2.has_turn = False 
            self.player1.has_turn = True

    def _setup_players(self) -> None:
        _player1_symbol = self._get_player_symbol()
        _player2_symbol = self._get_remaining_symbol(_player1_symbol)
        self.player1 = Player(symbol=_player1_symbol, has_turn=True)
        self.player2 = Player(symbol=_player2_symbol)

    def _get_player_symbol(self) -> PlayerSymbol:
        player_symbol = input("Player 1, enter your starting symbol (X or O): ").upper()
        if player_symbol == 'X':
            return PlayerSymbol.CROSS
        elif player_symbol == 'O':
            return PlayerSymbol.CIRCLE
        else:
            self._get_player_symbol()
        
    def _get_remaining_symbol(self, symbol: PlayerSymbol) -> PlayerSymbol:
        if symbol == PlayerSymbol.CIRCLE: return PlayerSymbol.CROSS
        elif symbol == PlayerSymbol.CROSS: return PlayerSymbol.CIRCLE
            

game = TicTacToe()
game.start_game()