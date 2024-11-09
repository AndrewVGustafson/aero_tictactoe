import pygame as pg
from src.base.base_tictactoe import BaseTicTacToe
from src.base.base_models import Player, PlayerSymbol, TileLocation
from src.game.game_grid import GameGrid
from src.game.game_tile import GameTile


class TicTacToe(BaseTicTacToe):
    def __init__(self) -> None:
        super().__init__()

        self.grid = GameGrid()
        self.grid.setup_game_tiles(self.on_tile_click)


    def start_game(self):
        self.setup_game()

    def on_tile_click(self, sprite: GameTile):
        if self.player1.has_turn:
            self.do_move(sprite, self.player1)
        elif self.player2.has_turn:
            self.do_move(sprite, self.player2)
        else:
            raise Exception("No player has turn")



    def do_move(self, gametile: GameTile, player: Player):
        if symbol := self.check_win():
            if symbol == PlayerSymbol.NULL:
                print("It's a tie!")
                return
            winner = self.opposite_player(player)
            print(f"Player {winner.num}, YOU WIN!")
            return
        

        if not self.is_gametile_empty(gametile):
            print("Tile is full")
            return

        new_status = self.player_symbol_to_tile(player.symbol)

        self.grid.set_tile_status(gametile, new_status)
        self.switch_turns()

        print("\nCurrent Board")
        self.grid.print_board()
        next_player = self.opposite_player(player)
        print(f"\nPlayer {next_player.num}'s turn. ({next_player.symbol.name})")
        

    def is_gametile_empty(self, sprite: GameTile) -> bool:
        row, col = sprite.grid_location
        location = TileLocation(row=row, column=col)
        if self.is_empty(location):
            return True
        return False

    def setup_game(self):
        self.setup_players()

    def setup_players(self):
        self.player1 = Player(num=1, symbol=PlayerSymbol.Cross, has_turn=True)
        self.player2 = Player(num=2, symbol=PlayerSymbol.Circle, has_turn=False)

    def update(self, events: list[pg.event.Event]) -> None:
        self.grid.gametiles.update(events)

    def reset_game(self):
        self.grid.reset_tiles(self.on_tile_click)