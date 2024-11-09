from src.base.base_models import TileStatus
import pygame as pg


class GameTile(pg.sprite.Sprite):
    def __init__(self, grid_location: tuple[int, int], status: TileStatus, callback) -> None:
        pg.sprite.Sprite.__init__(self)
        self.grid_location = grid_location
        self.position = self.get_position(self.grid_location)
        self.status = status
        self.callback = callback

        self.image: pg.Surface
        self.set_tile_status(self.status)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position


    def set_tile_status(self, status: TileStatus) -> None:
        self.status = status
        match status:
            case TileStatus.EMPTY:
                self.image = pg.image.load(r"images\emptytile.png")
            case TileStatus.CIRCLE:
                self.image = pg.image.load(r"images\circle.png")
            case TileStatus.CROSS:
                self.image = pg.image.load(r"images\cross.png")       
                

    def get_position(self, grid_location: tuple[int, int]) -> tuple[int, int]:
        positions = {"rows":{0:80, 1:301, 2:521}, "cols":{0:79, 1:299, 2:518}}
        rows = positions["rows"]
        cols = positions["cols"]
        
        row, col = grid_location
        position = (rows[col], cols[row])
        return position


    def update(self, events: list[pg.event.Event]):
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback(self)
