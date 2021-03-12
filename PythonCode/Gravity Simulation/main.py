import pygame as pg
from pygame.locals import *
from math import sqrt


SIZE = 750
G = 6.67 * 10**-11

class Particle():
    
    def __init__(self, pos, m):
        self.x = pos[0]
        self.y = pos[1]
        self.v = 0                                #Particle's velocity, starts at 0
        self.d = SIZE-pos[1]                      #1px == 1m
        self.h = self.d                      
        self.m = m
        self.isFalling = True
        self.hasStopped = False
        self.historic = [0, 0]
        self.historicIndex = 0
    
    def checkHistoric(self):
        if self.historicIndex > 1: self.historicIndex = 0
        self.historic[self.historicIndex] = self.v
        self.historicIndex += 1
        flag = True
        for i in range(0, 2): 
            if self.v != self.historic[i]:
                flag = False
                break
        if flag: self.hasStopped = True

    def update(self, g):
        if not self.hasStopped:
            self.d = SIZE-self.y
            self.v += g/60                              #60 fps
            self.y += self.v/60                         #60 fps
            if self.y+20 >= SIZE and self.isFalling: 
                self.v = -self.v/1.5
                self.isFalling = False
            if not self.isFalling and self.v < 5 and self.v > -5:
                self.h = self.d
                self.isFalling = True
            self.checkHistoric()
            print(self.historic)
        else:
            self.y = SIZE-20
            self.v = 0




if __name__ == "__main__":
    #M = float(input("Introduce la masa del planeta en kg (Ejm, Tierra = ->5.97<- * 10**24):"))
    #expM = int(input("Introduce el exponente: (M *10^?)"))
    M = 5.97*10**12
    m = 1#float(input("Introduce la masa del objeto (kg): "))
    g = G*M

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
                particle = Particle(pg.mouse.get_pos(), m)
        
        screen.fill((255, 255, 255))
        if started:
            pg.draw.circle(screen, (255, 0, 0), (particle.x, particle.y), 20)
            particle.update(g)
            #print(f"v: {particle.v} | g: {g} | isFalling: {particle.isFalling} | hasStopped: {particle.hasStopped}")
        pg.display.update()
                