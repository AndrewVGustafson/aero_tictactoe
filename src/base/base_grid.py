# if __name__ == "base_grid":
#     from base_models import BaseTile, TileStatus, TileLocation
# else:
from .base_models import BaseTile, TileStatus, TileLocation

class BaseGrid:
    def __init__(self) -> None:
        self.tiles: list[list[BaseTile]]
        self._set_tiles()
        self.TILE_STATUS_MAP: dict = {
        0: '_',
        1: 'O',
        2: 'X'
    }

    def _set_tiles(self):
        self.tiles = []
        for row in range(3):
            row_list = []
            for column in range(3):
                tile = BaseTile(
                    location = TileLocation(row=row, column=column),
                    status = TileStatus.EMPTY
                )
                row_list.append(tile)
            self.tiles.append(row_list)

    def get_tile_statuses(self) -> list[list]:
        return [[tile.status for tile in row] for row in self.tiles]
    
    def print_board(self) -> None:
        board_status = [[self.TILE_STATUS_MAP[tile.status.value] for tile in row] for row in self.tiles]
        for row in board_status:
            print(row[0], row[1], row[2])
    
    def print_tile_statuses(self) -> None:
        tile_statuses = self.get_tile_statuses()
        for row in tile_statuses:
            print(*row)
            