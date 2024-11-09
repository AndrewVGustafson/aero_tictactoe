import pygame as pg
from pygame.locals import QUIT

from src.game.game_grid import GameGrid
# from pygame.locals import KEYDOWN, K_ESCAPE

# pygame.mouse.set_cursor(*pygame.cursors.ball)
# pygame.mouse.set_cursor(*pygame.cursors.broken_x)

bg = pg.image.load(r"images\background.png")
grid = GameGrid()

def check_if_exiting(events: list[pg.event.Event]) -> None:
    for event in events:
        # if event.type == KEYDOWN:
        #     if event.key == K_ESCAPE:
        #         raise SystemExit

        if event.type == QUIT:
            raise SystemExit

def main():
    pg.init()
    pg.rect.Rect.center
    pg.display.set_caption("Tic-Tac-Toe")
    screen = pg.display.set_mode((800, 800))


    while True:
        events = pg.event.get()
        check_if_exiting(events)
        grid.gametiles.update(events)

        screen.blit(bg, [0, 0])
        screen.blit(grid.image, [0, 0])
        grid.gametiles.draw(screen)

        pg.display.update()

            
if __name__ == "__main__":
    main()