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

    def _set_tiles(self) -> None:
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

    def get_tile_statuses(self) -> list[list[TileStatus]]:
        return [[tile.status for tile in row] for row in self.tiles]

    def print_board(self) -> None:
        board_status = [[self.TILE_STATUS_MAP[tile.status.value] for tile in row] for row in self.tiles]
        for row in board_status:
            print(row[0], row[1], row[2], sep="|")

    def print_tile_statuses(self) -> None:
        tile_statuses = self.get_tile_statuses()
        for row in tile_statuses:
            print(*row)

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

    def set_tile(self, location: TileLocation, status: TileStatus) -> None:
        tile = self.tiles[location.row][location.column]
        tile.status = status

    def get_tile(self, location: TileLocation) -> BaseTile:
        return self.tiles[location.row][location.column]

    def reset_grid(self):
        self._set_tiles()