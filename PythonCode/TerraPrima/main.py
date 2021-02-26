import pygame as pg
from pygame.locals import *

#-----------------------------
import renderer 
from renderer import Palette

SIZE = 1840, 1000
WIDTH, HEIGHT = SIZE


class Pixel():
    
    def __init__(self, x=None, y=None, alpha=1.0, rect=None, color=None):
        self.x = x
        self.y = y
        self.rect = Rect(x,y,5,5)
        self.rawColor = Palette['Black']
        self.alpha = alpha
        self.color = self.setColor()
    
    def setColor(self):
        rgbList = list(self.rawColor)
        rgbList.append(self.alpha)
        rgbaColor = tuple(rgbList)
        print(rgbaColor)
        return rgbaColor


class PixelGrid():

    def __init__(self, pixels=[], rows=None, columns=None, pixAlpha=1.0):
        self.pixels = pixels
        self.rows = 1000
        self.columns = 1840
        self.pixAlpha = pixAlpha

        self.populate()

    def populate(self):
        for y in range(0, self.rows, 5):
            for x in range(0, self.columns, 5):
                self.pixels.append(Pixel(x, y, self.pixAlpha))

    def draw(self, screen):
        for pixel in self.pixels:
            pg.draw.rect(screen, pixel.color, pixel.rect)


def main():
    pg.init()

    clock = pg.time.Clock()
    screen = pg.display.set_mode(SIZE)
    pg.display.update()
    pg.display.set_caption("Terra Prima")
    screen.fill(Palette['Black']);
    #main_grid = PixelGrid()
    #Each pixel in fadeMask_grid starts with same alpha but can be changed at will (for future dithering)
    fadeMask_grid = PixelGrid(pixAlpha=0.0)
    running = True


    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == QUIT: running = False
            if event.type == MOUSEBUTTONDOWN:
                renderer.Sprite("PythonCode/TerraPrima/src/test.png", screen, pg.mouse.get_pos())

        #main_grid.draw(screen)
        fadeMask_grid.draw(screen)
        pg.display.update()
        
    
    pg.quit()


if __name__ == "__main__":
    main()