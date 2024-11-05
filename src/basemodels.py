from pydantic import BaseModel
from enum import Enum

class TileStatus(Enum):
    EMPTY = 0
    CIRCLE = 1
    CROSS = 2

class TileLocation(BaseModel):
    row: int
    column: int

class BaseTile(BaseModel):
    location: TileLocation
    status: TileStatus

class BaseGrid:

    def __init__(self) -> None:
        self.tiles: list[list[BaseTile]] = [[None]*3]*3
        self._set_tiles()
        self.TILE_STATUS_MAP: dict = {
        0: '_',
        1: 'O',
        2: 'X'
    }

    def _set_tiles(self):
        for row in range(3):
            for column in range(3):
                tile = BaseTile(
                    location = TileLocation(row=row, column=column),
                    status = TileStatus.EMPTY
                )
                self.tiles[row][column] = tile

    def get_tile_statuses(self) -> list[list]:
        return [[tile.status.name for tile in row] for row in self.tiles]
    
    def print_board(self) -> None:
        board_status = [[self.TILE_STATUS_MAP[tile.status.value] for tile in row] for row in self.tiles]
        for row in board_status:
            print(*row)
    
    def print_tile_statuses(self) -> None:
        tile_statuses = self.get_tile_statuses()
        for row in tile_statuses:
            print(*row)