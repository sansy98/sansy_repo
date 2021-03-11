import pygame as pg
from pygame.locals import *


SIZE = 750
G = 6.67 * 10**-11
g = 0


class Particle():
    
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.v = 0                                #Particle's velocity, starts at 0
        self.rect = Rect(self.x, self.y, 10, 10)



if __name__ == "__main__":
    M = input("Introduce la masa del planeta en kg (Ejm, Tierra = 5.97 * 10**24): ")

    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((SIZE, SIZE))
    pg.display.set_caption("Gravity Simulator")
    running = True
    started = False

    #Simulation main loop
    while running:
        
        for event in pg.event.get():
            if event.type == QUIT: running = False
            if event.type == MOUSEBUTTONDOWN and not started:
                started = True
                particle = Particle(pg.mouse.get_pos())
        
        screen.fill((255, 255, 255))
        #CODE HERE
        pg.display.update()
                