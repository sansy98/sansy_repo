import pygame as pg
from pygame.locals import *
#-----------------------------
from renderer import *


SIZE = 1840, 1000
WIDTH, HEIGHT = SIZE


class Pixel():
    
    def __init__(self, x=None, y=None, rect=None, color=None):
        self.x = x
        self.y = y
        self.rect = Rect(x,y,5,5)
        self.color = Palette['Black']


class PixelGrid():

    def __init__(self, pixels=[], rows=None, columns=None):
        self.pixels = pixels
        self.rows = 1000
        self.columns = 1840
        self.populate()

    def populate(self):
        for y in range(0, self.rows, 5):
            for x in range(0, self.columns, 5):
                self.pixels.append(Pixel(x, y))

    def draw(self, screen):
        i = 0;
        for pixel in self.pixels:
            if i >= 15: i = 0
            pixel.color = RGBS[i]
            i += 1
            pg.draw.rect(screen, pixel.color, pixel.rect)


def main():
    pg.init()

    clock = pg.time.Clock()
    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption("Terra Prima")
    screen.fill(Palette['Black']);
    grid = PixelGrid()
    running = True


    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == QUIT: running = False

        grid.draw(screen)
        pg.display.update();
        
    
    pg.quit()


if __name__ == "__main__":
    main()
