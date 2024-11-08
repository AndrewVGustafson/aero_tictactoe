import pygame as pg
 
 
class ClickableSprite(pg.sprite.Sprite):
    def __init__(self, image, x, y, callback, a):
        super().__init__()
        self.image = image
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

    def update(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback(self)
 
 
def on_click(s):
    # sprite.image.get_at
    s.image = pg.image.load(r"images\cross.png")  
 
 
pg.init()
screen = pg.display.set_mode((700, 800))
 
sprite = ClickableSprite(pg.Surface((100, 100)), 50, 50, on_click, 1)
sprite2 = ClickableSprite(pg.Surface((100, 100)), 50, 350, on_click, 1)
group = pg.sprite.Group()
group.add(sprite)
group.add(sprite2)
 
running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
 
    group.update(events)
    screen.fill((255, 255, 255))
    group.draw(screen)
    pg.display.update()
 
pg.quit()