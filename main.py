import pygame as pg
from pygame.locals import QUIT

from src.game.tictactoe import TicTacToe




def check_if_exiting(events: list[pg.event.Event]) -> None:
    for event in events:
        if event.type == QUIT:
            raise SystemExit

def main():
    pg.init()
    pg.rect.Rect.center
    pg.display.set_caption("Tic-Tac-Toe")
    screen = pg.display.set_mode((800, 800))
    
    bg = pg.image.load(r"images\background.png")
    game = TicTacToe()
    game.start_game()

    while True:
        events = pg.event.get()
        check_if_exiting(events)
        game.update(events)

        screen.blit(bg, [0, 0])
        screen.blit(game.grid.image, [0, 0])
        game.grid.gametiles.draw(screen)

        pg.display.update()

            
if __name__ == "__main__":
    main()