import pygame as pg
from pygame.locals import *


RGBS = {
    0 : (7,8,8), 1 : (153,51,17), 2 : (221,119,17), 3 : (255,255,51), 4 : (85,170,68), 
    5 : (17,85,34), 6 : (68,238,187), 7: (51,136,221), 8 : (85,68,170), 9 : (51,34,34), 
    10 : (119,68,51), 11 : (204,136,85), 12 : (255,221,85), 13 : (255,255,255), 14 : (170,187,187), 15 : (85,85,119)
    }

Palette = {
    "Black" : RGBS[0], "Red" : RGBS[1], "Orange" : RGBS[2], "Yellow" : RGBS[3], "Lime" : RGBS[4], "Green" : RGBS[5],
    "Cyan" : RGBS[6], "Blue" : RGBS[7], "Purple" : RGBS[8], "Brown" : RGBS[9], "LightBrown" : RGBS[10], "Skin" : RGBS[11],
    "Gold" : RGBS[12] , "White" : RGBS[13], "LightGray" : RGBS[14], "Gray" : RGBS[15]
}

#Dict that indictates the fading values range that each color can take. FULL RANGE: [-3, +4]
FADINGS = {
    0 : range(0,5), 1 : range(-1,5), 2 : range(-2,4), 3 : range(-3,3), 4 : range(-2,4), 5 : range(-1,5), 6 : range(-3,3),
    7 : range(-2,4), 8 : range(-1,5), 9 : range(0,4), 10 : range(-1,5), 11 : range(-2,4), 12 : range(-3,3),
    13 : range(-3,1), 14 : range(-2,2), 15 : range(-1,3)
}


class Sprite():
    
    def __init__(self, file, parentSurface, coords):
        self.image = pg.image.load(file)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.size = (self.width, self.height)
        self.rect = self.image.get_rect()
        self.parentSurface = parentSurface
        self.coords = coords

        self.draw();
    
    def draw(self):
        self.image.blit(self.parentSurface, self.coords)
        pg.draw.rect(self.parentSurface, Palette["Red"], self.rect)
        pg.display.update()