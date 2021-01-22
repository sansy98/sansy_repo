import pygame as pg
from pygame.locals import *
import math

class Cell():
    def __init__(self, x = None, y = None, rect = None, x2 = None, y2 = None, alive = False, fAlive = False, nearLiving = None):
        self.x = x;
        self.y = y;
        self.x2 = x+10;
        self.y2 = y+10;
        self.alive = alive;
        self.fAlive = fAlive;
        self.rect = Rect(x, y, 10, 10);
        self.nearLiving = nearLiving;


class Grid():
    def __init__(self, bodies = [], rows = 126, columns = 75):
        self.bodies = bodies;
        self.rows = rows;
        self.columns = columns;
    
    def populate(self):
        for column in range(0, self.columns):
            self.bodies.append([]);
            for row in range(0, self.rows):
                self.bodies[column].append(Cell(row*10, column*10));
    
    def draw(self, screen):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                if self.bodies[column][row].alive: pg.draw.rect(screen, (0, 50, 75), self.bodies[column][row].rect, 0);
                else: pg.draw.rect(screen, (200, 200, 200), self.bodies[column][row].rect, 1);

    
    def setLiving(self):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                if not self.bodies[column][row].alive and pg.mouse.get_pos()[0] in range(self.bodies[column][row].x, self.bodies[column][row].x+10) and pg.mouse.get_pos()[1] in range(self.bodies[column][row].y, self.bodies[column][row].y+10):
                    self.bodies[column][row].alive = True;
                elif self.bodies[column][row].alive and pg.mouse.get_pos()[0] in range(self.bodies[column][row].x, self.bodies[column][row].x+10) and pg.mouse.get_pos()[1] in range(self.bodies[column][row].y, self.bodies[column][row].y+10):
                    self.bodies[column][row].alive = False;

    def checkStatus(self):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                self.bodies[column][row].nearLiving = 0;
                try:    
                    if self.bodies[column][row-1].alive: self.bodies[column][row].nearLiving += 1;
                except IndexError as e: pass;
                try:    
                    if self.bodies[column][row+1].alive: self.bodies[column][row].nearLiving += 1;
                except IndexError as e: pass;
                try:    
                    if self.bodies[column-1][row].alive: self.bodies[column][row].nearLiving += 1;
                except IndexError as e: pass;
                try:    
                    if self.bodies[column+1][row].alive: self.bodies[column][row].nearLiving += 1;
                except IndexError as e: pass;
                try:
                    if self.bodies[column-1][row-1].alive: self.bodies[column][row].nearLiving += 1;
                except IndexError as e: pass;
                try:
                    if self.bodies[column-1][row+1].alive: self.bodies[column][row].nearLiving += 1;
                except IndexError as e: pass;
                try:
                    if self.bodies[column+1][row-1].alive: self.bodies[column][row].nearLiving += 1;
                except IndexError as e: pass;
                try:
                    if self.bodies[column+1][row+1].alive: self.bodies[column][row].nearLiving += 1;
                except IndexError as e: pass;
                if self.bodies[column][row].nearLiving < 2 or self.bodies[column][row].nearLiving > 3:    self.bodies[column][row].fAlive = False;
                elif self.bodies[column][row].nearLiving == 2 and self.bodies[column][row].alive:    self.bodies[column][row].fAlive = True;
                elif self.bodies[column][row].nearLiving == 3: self.bodies[column][row].fAlive = True;
        self.updateStatus();
                
    def updateStatus(self):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                self.bodies[column][row].alive = self.bodies[column][row].fAlive;

    def restart(self):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                self.bodies[column][row].alive = False;

                

WIDTH = 1260;
HEIGHT = 750;
running = True;

clock = pg.time.Clock();
screen = pg.display.set_mode((WIDTH, HEIGHT));
grid = Grid();
grid.populate();
simulationStart = False;

while running:
    clock.tick(60);
    for event in pg.event.get():
        if event.type == QUIT:
            running = False;
        if event.type == MOUSEBUTTONDOWN:
            grid.setLiving();
        if event.type == KEYDOWN:
            if event.key == K_SPACE and not simulationStart:    simulationStart = True;
            elif event.key == K_SPACE and simulationStart:      simulationStart = False;
            if event.key == K_r: grid.restart();

    
    if simulationStart: grid.checkStatus();
    screen.fill((255, 255, 255));
    grid.draw(screen);
    pg.display.update();

pg.quit();
