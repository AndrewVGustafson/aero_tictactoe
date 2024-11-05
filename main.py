import pygame

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


# pygame.mouse.set_cursor(*pygame.cursors.ball)
# pygame.mouse.set_cursor(*pygame.cursors.broken_x)
test_rect = pygame.Rect((300, 250, 50, 50))
red = pygame.Color(255, 0, 0)

def main():
    pygame.init()
    pygame.display.set_caption("Tic-Tac-Toe")
    screen = pygame.display.set_mode((800, 800))


    while True:
        pygame.draw.rect(screen, red, test_rect, 10)
        pygame.display.update()



        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    raise SystemExit

            elif event.type == QUIT:
                raise SystemExit
            
if __name__ == "__main__":
    main()