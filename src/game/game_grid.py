import pygame as pg
from src.base.base_grid import BaseGrid
from src.base.base_models import TileStatus, TileLocation
from src.game.game_tile import GameTile

class GameGrid(BaseGrid):
    def __init__(self) -> None:
        super().__init__()
        self.image = pg.image.load(r"images\grid.png")
        self.gametiles = pg.sprite.Group()

    def set_tile_status(self, gametile: GameTile, status: TileStatus):
        row, col = gametile.grid_location
        location = TileLocation(row=row, column=col)
        self.set_tile(location, status)
        gametile.set_tile_status(status)


    def setup_game_tiles(self, func) -> None:
        self._set_tiles()
        self.gametiles.empty()
        for row in range(3):
            for col in range(3):
                sprite = GameTile((row, col), TileStatus.EMPTY, callback=func)
                self.gametiles.add(sprite)

    def reset_tiles(self, func):
        self.setup_game_tiles(func)
        self.reset_grid()
