import pygame as pg
from pygame.locals import *
import random
import math


BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)         #1
GREEN = (0, 255, 0)        #2
RED = (255, 0, 0)          #3
VIOLET = (98, 0, 255)      #4
YELLOW = (255, 255, 0)     #5
CYAN = (0, 255, 255)       #6
ORANGE = (255,165,0)       #7
PINK = (255,192,203)       #8



#REFERENCES FOR COLORS
C1 = BLUE
C2 = GREEN
C3 = RED
C4 = VIOLET
C5 = YELLOW
C6 = CYAN
C7 = ORANGE
C8 = PINK

pg.init()

running = True

clock = pg.time.Clock()

screenSize = [700, 700]
display = pg.display.set_mode(screenSize)
pg.display.set_caption("(1)BLUE, (2)GREEN, (3)RED, (4)VIOLET, (5)YELLOW, (6)CYAN, (7)ORANGE, (8)PINK")

ROWS = 30
COLUMNS = 16



class Cell():
    def __init__(self, x = None, y = None, rect = None, x2 = None, y2 = None, isMine = False, nearMines = 0):
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
         
                
    def populate_mines(self):
        for i in range(self.mines):
            rx = random.randint(0, self.columns-1)
            ry = random.randint(0, self.rows-1)

            if self.bodies[rx][ry].isMine:
                while self.bodies[rx][ry].isMine:
                   rx = random.randint(0, self.columns-1)
                   ry = random.randint(0, self.rows-1)
                   
            self.bodies[rx][ry].isMine = True


    def set_near_mines(self):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                if not self.bodies[column][row].isMine:
                    #UPPER-LEFT
                    if column == 0 or row == 0:
                        pass
                    elif self.bodies[column-1][row-1].isMine: self.bodies[column][row].nearMines += 1
                    
                    #UP
                    if row == 0:
                        pass
                    elif self.bodies[column][row-1].isMine: self.bodies[column][row].nearMines += 1
                    
                    #UPPER-RIGHT
                    if column == self.columns-1 or row == 0:
                        pass
                    elif self.bodies[column+1][row-1].isMine: self.bodies[column][row].nearMines += 1
                    
                    #RIGHT
                    if column == self.columns-1:
                        pass
                    elif self.bodies[column+1][row].isMine: self.bodies[column][row].nearMines += 1
                    
                    #BOTTOM-RIGHT
                    if column == self.columns-1 or row == self.rows-1:
                        pass
                    elif self.bodies[column+1][row+1].isMine: self.bodies[column][row].nearMines += 1
                    
                    #BOTTOM
                    if row == self.rows-1:
                        pass
                    elif self.bodies[column][row+1].isMine: self.bodies[column][row].nearMines += 1
                    
                    #BOTTOM-LEFT
                    if column == 0 or row == self.rows-1:
                        pass
                    elif self.bodies[column-1][row+1].isMine: self.bodies[column][row].nearMines += 1
                    
                    #LEFT
                    if column == 0:
                        pass
                    elif self.bodies[column-1][row].isMine: self.bodies[column][row].nearMines += 1
                    
    
    
    def draw(self, display):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                if self.bodies[column][row].isMine: pg.draw.rect(display, (0, 50, 75), self.bodies[column][row].rect, 0);
                elif self.bodies[column][row].nearMines == 1: pg.draw.rect(display, C1, self.bodies[column][row].rect, 0);
                elif self.bodies[column][row].nearMines == 2: pg.draw.rect(display, C2, self.bodies[column][row].rect, 0);
                elif self.bodies[column][row].nearMines == 3: pg.draw.rect(display, C3, self.bodies[column][row].rect, 0);
                elif self.bodies[column][row].nearMines == 4: pg.draw.rect(display, C4, self.bodies[column][row].rect, 0);
                elif self.bodies[column][row].nearMines == 5: pg.draw.rect(display, C5, self.bodies[column][row].rect, 0);
                elif self.bodies[column][row].nearMines == 6: pg.draw.rect(display, C6, self.bodies[column][row].rect, 0);
                elif self.bodies[column][row].nearMines == 7: pg.draw.rect(display, C7, self.bodies[column][row].rect, 0);
                elif self.bodies[column][row].nearMines == 8: pg.draw.rect(display, C8, self.bodies[column][row].rect, 0);
                else: pg.draw.rect(display, (200, 200, 200), self.bodies[column][row].rect, 1);
                
    
    def initialise(self):
        grid.populate()
        grid.populate_mines()
        grid.set_near_mines()

    #DEBUG METHODS
    
    #Prints a matrix with the mines and the values of nearmines in the console
    def DEBUG_visualPrint_nearMines(self):
        print("[", end=" ")
        
        for column in range(0, self.columns):
            print("  [", end=" ")
            for row in range(0, self.rows):
                if not self.bodies[column][row].isMine:
                    print(self.bodies[column][row].nearMines, end=", ")
                else:
                    print("X", end=", ")
            
            print("]")
        
        print("]")
    



grid = Grid()
grid.initialise()


while running:
    clock.tick(60)
    
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False
        
    display.fill(WHITE)
    grid.draw(display)
    
    pg.display.update()
    
    
    

pg.quit()    
