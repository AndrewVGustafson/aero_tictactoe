from base.base_models import TileStatus, TileLocation, BaseTile
from base.base_grid import BaseGrid

class Grid(BaseGrid):
    def __init__(self) -> None:
        super().__init__()

    def set_tile(self, location: TileLocation, status: TileStatus) -> None:
        tile = self.tiles[location.row][location.column]
        tile.status = status

    def get_tile(self, location: TileLocation) -> BaseTile:
        return self.tiles[location.row][location.column]
    
    def get_rows(self) -> list[list[TileStatus]]:
        rows = self.get_tile_statuses()
        return rows

    def get_columns(self) -> list[list[TileStatus]]:
        # Rotates board 90deg clockwise
        columns = list(zip(*self.get_tile_statuses()[::-1]))
        columns = [list(col) for col in columns]
        return columns
    
    def get_diagonals(self) -> list[list[TileStatus]]:
        diag_ascending = [tile[~i] for i, tile in enumerate(self.get_tile_statuses())]
        diag_descending = [tile[i] for i, tile in enumerate(self.get_tile_statuses())]
        return [diag_descending, diag_ascending]