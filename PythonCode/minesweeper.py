import pygame as pg
from pygame.locals import *
import random
import math


BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
VIOLET = (98, 0, 255)

pg.init()

running = True

clock = pg.time.Clock()

screenSize = [700, 700]
display = pg.display.set_mode(screenSize)
pg.display.set_caption("Los pinguinos me la van a mascar")

ROWS = 30
COLUMNS = 16



class Cell():
    def __init__(self, x = None, y = None, rect = None, x2 = None, y2 = None, isMine = False, nearMines = None):
        self.x = x;
        self.y = y;
        self.x2 = x+math.floor(min(screenSize[0], screenSize[1])/max(ROWS,COLUMNS));
        self.y2 = y+math.floor(min(screenSize[0], screenSize[1])/max(ROWS,COLUMNS));
        self.isMine = isMine
        self.rect = Rect(x, y, self.x2-x, self.y2-y);
        self.nearMines = nearMines;


class Grid():
    def __init__(self, bodies = [], mines = 99, rows = 16, columns = 30):
        self.bodies = bodies;
        self.mines = mines
        self.rows = rows;
        self.columns = columns;
    
    def populate(self):
        for column in range(0, self.columns):
            self.bodies.append([]);
            for row in range(0, self.rows):
                self.bodies[column].append(Cell(row*math.floor(min(screenSize[0], screenSize[1])/max(ROWS,COLUMNS)), column*math.floor(min(screenSize[0], screenSize[1])/max(ROWS,COLUMNS))));
                
    #NO FUNCIONA, ERROR DE INDEX, REVISAR
    def populate_mines(self):
        for i in range(self.mines):
            rx = random.randint(0, self.rows)
            ry = random.randint(0, self.columns)
            
            if self.bodies[rx][ry].isMine:
                while self.bodies[rx][ry].isMine:
                   rx = random.randint(0, self.columns)
                   ry = random.randint(0, self.rows)
                   
            self.bodies[rx][ry].isMine = True
                
    
    def draw(self, display):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                if self.bodies[column][row].isMine: pg.draw.rect(display, (0, 50, 75), self.bodies[column][row].rect, 0);
                else: pg.draw.rect(display, (200, 200, 200), self.bodies[column][row].rect, 1);






grid = Grid()
grid.populate()
grid.populate_mines()

while running:
    clock.tick(60)
    
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False
        
    display.fill(WHITE)
    grid.draw(display)
    
    pg.display.update()
    
    
    

pg.quit()    