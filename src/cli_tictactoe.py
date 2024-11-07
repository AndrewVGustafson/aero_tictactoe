from grid import Grid
from base.base_models import PlayerSymbol, TileLocation, TileStatus, BasePlayer

# TODO Move player methods from tictactoe classes into Player class
# make check_win() return location of win instead of PlayerSymbol

class Player(BasePlayer):
    pass


class BaseTicTacToe:
    def __init__(self) -> None:
        self.grid = Grid()
        self.player1 = Player(num=1, symbol=PlayerSymbol.NULL)
        self.player2 = Player(num=2, symbol=PlayerSymbol.NULL)


    def check_win(self) -> PlayerSymbol:
        rows = self.grid.get_rows()
        cols = self.grid.get_columns()
        diagonals = self.grid.get_diagonals()

        possible_lines = [rows, cols, diagonals]

        for lines in possible_lines:
            if winner := self._check_lines(lines):
                return winner

    def _check_lines(self, lines: list) -> PlayerSymbol:
        for line in lines:
            if TileStatus.EMPTY in line:
                continue
            if len(set(line)) == 1:
                winner = self._tile_to_player_symbol(line[0])
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
    
    def set_move(self, location: TileLocation, symbol: PlayerSymbol):
        tile_status = self._player_symbol_to_tile(symbol)
        self.grid.set_tile(location=location, status=tile_status)

    def _is_empty(self, location: TileLocation) -> bool:
        return self.grid.get_tile(location).status == TileStatus.EMPTY
    

    def _switch_turns(self) -> None:
        assert self.player1.has_turn != self.player2.has_turn
        if self.player1.has_turn:
            self.player1.has_turn = False
            self.player2.has_turn = True
        elif self.player2.has_turn:
            self.player2.has_turn = False 
            self.player1.has_turn = True

    def opposite_player(self, player: Player) -> Player:
        if player.num == 1:
            return self.player2
        elif player.num == 2:
            return self.player1


class CLI_TicTacToe(BaseTicTacToe):
    def __init__(self):
        super().__init__()

    def start_game(self, starting_player_num: int = 1) -> None:
        self._setup_game(starting_player_num)
        self.grid.print_board()
        has_won = False
        while not has_won:
            if self.player1.has_turn:
                has_won = self.do_move(self.player1)
            elif self.player2.has_turn:
                has_won = self.do_move(self.player2)
        self.grid.reset_grid()
        
    def do_move(self, player: Player) -> bool:
        if self.check_win():
            winner = self.opposite_player(player)
            print(f"Player {winner.num}, YOU WIN!")
            return True
        
        print(f"\nPlayer {player.num}'s turn. ({player.symbol.name})")
        
        location = self.get_move()
        self.set_move(location, symbol=player.symbol)
        self._switch_turns()

        print()
        print("Current Board")
        self.grid.print_board()
        return False
    
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

    def _setup_game(self, starting_player_num: int = 1):
        assert starting_player_num in [1, 2]
        if starting_player_num == 1:
            self._setup_players(starting_player=self.player1)
        elif starting_player_num == 2:
            self._setup_players(starting_player=self.player2)

    def _setup_players(self, starting_player: Player) -> None:
        if starting_player.num == 1:
            _player1_symbol = self._get_player_symbol(starting_player)
            _player2_symbol = self._get_remaining_symbol(_player1_symbol)
            self.player1 = Player(num=1, symbol=_player1_symbol, has_turn=True)
            self.player2 = Player(num=2, symbol=_player2_symbol, has_turn=False)
        elif starting_player.num == 2:
            _player2_symbol = self._get_player_symbol(starting_player)
            _player1_symbol = self._get_remaining_symbol(_player2_symbol)
            self.player1 = Player(num=1, symbol=_player1_symbol, has_turn=False)
            self.player2 = Player(num=2, symbol=_player2_symbol, has_turn=True)


    def _get_player_symbol(self, player: Player) -> PlayerSymbol:
        while True:
            player_symbol = input(f"Player {player.num}, enter your starting symbol (X or O): ").upper()
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

game = CLI_TicTacToe()
while True:
    game.start_game(1)
    game.start_game(2)