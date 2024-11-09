import pygame as pg
 
 
class ClickableSprite(pg.sprite.Sprite):
    def __init__(self, image: pg.Surface, x, y, callback, a):
        super().__init__()
        self.image: pg.Surface = image
        self.set_tile_status(a)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
 
    def set_tile_status(self, status: int) -> None:
        self.status = status
        match status:
            case 0:
                self.image = pg.image.load(r"images\emptytile.png")
            case 1:
                self.image = pg.image.load(r"images\circle.png")
            case 2:
                self.image = pg.image.load(r"images\cross.png")  

    def update(self, events: list[pg.event.Event]):
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback(self)
 
 
def on_click(s):
    global a
    s.set_tile_status(2 if a % 2 == 1 else 1)
    a+=1
 
a = 1
pg.init()
screen = pg.display.set_mode((700, 800))
 
sprite = ClickableSprite(pg.Surface((100, 100)), 50, 50, on_click, 1)
sprite2 = ClickableSprite(pg.Surface((100, 100)), 50, 350, on_click, 1)
gametiles = pg.sprite.Group()
gametiles.add(sprite)
gametiles.add(sprite2)
 
bg = pg.image.load(r"images/background.png")
grid = pg.image.load(r"images/grid.png")

running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
 
    gametiles.update(events)
    screen.blit(bg, [0, 0])
    screen.blit(grid, [0, 0])
    gametiles.draw(screen)
    pg.display.update()
 
pg.quit()