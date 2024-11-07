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
        # self.grid.set_tile(TileLocation(row=0, column=0), TileStatus.CROSS)
        # self.grid.set_tile(TileLocation(row=0, column=1), TileStatus.CROSS)
        self.grid.print_board()
        self.do_move(self.player1)
        self.do_move(self.player2)
        self.do_move(self.player1)
        self.do_move(self.player2)
        self.do_move(self.player1)
        self.do_move(self.player2)
        self.do_move(self.player1)
        self.do_move(self.player2)
        
    def do_move(self, player: Player) -> None:
        if winner := self.check_win():
            print(f"{winner.name}, YOU WIN!")
            return
        
        print(f"\n{player.symbol.name}'s turn.")
        
        location = self.get_move()
        self.set_move(location, symbol=player.symbol)
        self._switch_turns()

        print()
        print("Current Board")
        self.grid.print_board()

    def check_win(self) -> PlayerSymbol:
        rows = self.grid.get_rows()
        cols = self.grid.get_columns()

        for row in rows:
            if TileStatus.EMPTY in row:
                continue
            if len(set(row)) == 1:
                winner = self._tile_to_player_symbol(row[0])
                return winner

        for col in cols:
            if TileStatus.EMPTY in col:
                continue
            if len(set(col)) == 1:
                winner = self._tile_to_player_symbol(col[0])
                return winner

    def _tile_to_player_symbol(self, tile_status: TileStatus) -> PlayerSymbol:
        assert tile_status != TileStatus.EMPTY
        if tile_status == TileStatus.CIRCLE:
            return PlayerSymbol.Circle
        elif tile_status == TileStatus.CROSS:
            return PlayerSymbol.Cross
        
    def _player_symbol_to_tile(self, player_symbol: PlayerSymbol) -> TileStatus:
        if player_symbol == PlayerSymbol.Circle:
            return TileStatus.CIRCLE
        elif player_symbol == PlayerSymbol.Cross:
            return TileStatus.CROSS

    def get_move(self) -> TileLocation:
        while True:
            row = self._get_row()
            col = self._get_col()
            location = TileLocation(row=row, column=col)
            if self._is_empty(location):
                return location
            else:
                print("Tile is full, try again.")
                continue
    
    def set_move(self, location: TileLocation, symbol: PlayerSymbol):
        tile_status = self._player_symbol_to_tile(symbol)
        self.grid.set_tile(location=location, status=tile_status)

    def _is_empty(self, location: TileLocation) -> None:
        return self.grid.get_tile(location).status == TileStatus.EMPTY
        
    def _get_row(self) -> int:
        while True:
            try:
                row  = int(input("Enter row: "))
            except ValueError:
                print("Invalid row. Try again.")
                continue
            if row in range(1, 4):
                return row - 1
            else:
                print("Invalid row. Try again.")
                continue

    def _get_col(self) -> int:
        while True:
            try:
                col  = int(input("Enter column: "))
            except ValueError:
                print("Invalid row. Try again.")
                continue
            if col in range(1, 4):
                return col - 1
            else:
                print("Invalid column. Try again.")
                continue

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
        while True:
            player_symbol = input("Player 1, enter your starting symbol (X or O): ").upper()
            match player_symbol:
                case 'X':
                    return PlayerSymbol.Cross
                case 'O':
                    return PlayerSymbol.Circle
                case _:
                    print("Invalid symbol. Try again.")
                    continue
        
    def _get_remaining_symbol(self, symbol: PlayerSymbol) -> PlayerSymbol:
        if symbol == PlayerSymbol.Circle:
            return PlayerSymbol.Cross
        elif symbol == PlayerSymbol.Cross:
            return PlayerSymbol.Circle


game = TicTacToe()
game.start_game()