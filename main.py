import pygame as pg
from pygame.locals import QUIT

from src.game.tictactoe import TicTacToe


def check_if_exiting(events: list[pg.event.Event]) -> None:
    for event in events:
        if event.type == QUIT:
            raise SystemExit

def draw_text(screen, text, color, x, y, font=None):
    font = pg.font.SysFont("arialblack", 40) if font is None else font
    image = font.render(text, True, color)
    screen.blit(image, (x, y))


def main():
    pg.init()
    pg.rect.Rect.center
    pg.display.set_caption("Tic-Tac-Toe")
    screen = pg.display.set_mode((800, 800))
    
    game = TicTacToe()
    game.start_game()

    while True:
        events = pg.event.get()
        check_if_exiting(events)
        game.update(screen, events)

        pg.display.update()

            
if __name__ == "__main__":
    main()