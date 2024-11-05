from basemodels import BaseGrid, TileStatus, TileLocation, BaseTile

class Grid(BaseGrid):
    def __init__(self) -> None:
        super().__init__()

        self.set_tile(TileLocation(row=2, column=1), TileStatus.CROSS)

        self.get_tile_statuses()

    def set_tile(self, location: TileLocation, status: TileStatus):
        tile = self.get_tile(location)
        tile.status = status

    def get_tile(self, location: TileLocation) -> BaseTile:
        # print(location)
        return self.tiles[location.row][location.column]
        

grid = Grid()
grid.print_board()