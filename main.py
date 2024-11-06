import pygame as pg
from pygame.locals import QUIT
# from pygame.locals import KEYDOWN, K_ESCAPE
from src.grid import Grid


# pygame.mouse.set_cursor(*pygame.cursors.ball)
# pygame.mouse.set_cursor(*pygame.cursors.broken_x)
bg = pg.image.load(r"images\background.png")

def check_if_exiting() -> None:
    for event in pg.event.get():
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
    screen.blit(bg, [0, 0])
    grid = Grid().print_tile_statuses()

    while True:

        pg.display.update()
        check_if_exiting()



            
if __name__ == "__main__":
    main()