import pygame as pg
from pygame.locals import *
import random
import math


BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
DEFAULT = (200, 200, 200)
BLUE = (0, 0, 255)         #1
GREEN = (0, 255, 0)        #2
RED = (255, 0, 0)          #3
VIOLET = (98, 0, 255)      #4
YELLOW = (255, 255, 0)     #5
CYAN = (0, 255, 255)       #6
ORANGE = (255,165,0)       #7
PINK = (255,192,203)       #8



#REFERENCES FOR COLORS
colorOrderedTuple = (DEFAULT, BLUE, GREEN, RED, VIOLET, YELLOW, CYAN, ORANGE, PINK)

pg.init()

running = True

clock = pg.time.Clock()

screenSize = [700, 700]
display = pg.display.set_mode(screenSize)
pg.display.set_caption("(1)BLUE, (2)GREEN, (3)RED, (4)VIOLET, (5)YELLOW, (6)CYAN, (7)ORANGE, (8)PINK")

ROWS = 30
COLUMNS = 16



class Cell():
    def __init__(self, x = None, y = None, rect = None, x2 = None, y2 = None, isMine = False, nearMines = 0, isVisible = False):
        self.x = x;
        self.y = y;
        self.x2 = x+math.floor(min(screenSize[0], screenSize[1])/max(ROWS,COLUMNS));
        self.y2 = y+math.floor(min(screenSize[0], screenSize[1])/max(ROWS,COLUMNS));
        self.isMine = isMine
        self.rect = Rect(x, y, self.x2-x, self.y2-y);
        self.nearMines = nearMines;
        self.isVisible = isVisible;


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
    
    def updateCellsAround(self, column, row):
        if self.bodies[column-1][row-1].nearMines == 0 and not self.bodies[column-1][row-1].isMine and not self.bodies[column-1][row-1].isVisible: 
            self.bodies[column-1][row-1].isVisible = True
            self.updateCellsAround(column-1, row-1)
        
        if self.bodies[column][row-1].nearMines == 0 and not self.bodies[column][row-1].isMine and not self.bodies[column][row-1].isVisible: 
            self.bodies[column][row-1].isVisible = True
            self.updateCellsAround(column, row-1)
        
        if self.bodies[column+1][row-1].nearMines == 0 and not self.bodies[column+1][row-1].isMine and not self.bodies[column+1][row-1].isVisible:
            self.bodies[column+1][row-1].isVisible = True
            self.updateCellsAround(column+1, row-1)
        
        if self.bodies[column+1][row].nearMines == 0 and not self.bodies[column+1][row].isMine and not self.bodies[column+1][row].isVisible:
            self.bodies[column+1][row].isVisible = True
            self.updateCellsAround(column+1, row)
        
        if self.bodies[column+1][row+1].nearMines == 0 and not self.bodies[column+1][row+1].isMine and not self.bodies[column+1][row+1].isVisible:
            self.bodies[column+1][row+1].isVisible = True
            self.updateCellsAround(column+1, row+1)

        if self.bodies[column][row+1].nearMines == 0 and not self.bodies[column][row+1].isMine and not self.bodies[column][row+1].isVisible:
            self.bodies[column][row+1].isVisible = True
            self.updateCellsAround(column, row+1)

        if self.bodies[column-1][row+1].nearMines == 0 and not self.bodies[column-1][row+1].isMine and not self.bodies[column-1][row+1].isVisible:
            self.bodies[column-1][row+1].isVisible = True
            self.updateCellsAround(column-1, row+1)

        if self.bodies[column-1][row].nearMines == 0 and not self.bodies[column-1][row].isMine and not self.bodies[column-1][row].isVisible:
            self.bodies[column-1][row].isVisible = True
            self.updateCellsAround(column-1, row)
    
    def uncoverCell(self):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                if not self.bodies[column][row].isVisible and pg.mouse.get_pos()[0] in range(self.bodies[column][row].x, self.bodies[column][row].x2) and pg.mouse.get_pos()[1] in range(self.bodies[column][row].y, self.bodies[column][row].y2):
                    self.bodies[column][row].isVisible = True
                    if self.bodies[column][row].nearMines == 0:
                        self.updateCellsAround(column, row)
    
    def clearMinesAround(self):
        cellsColumn = 0
        cellsRow = 0
        
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                if pg.mouse.get_pos()[0] in range(self.bodies[column][row].x, self.bodies[column][row].x2) and pg.mouse.get_pos()[1] in range(self.bodies[column][row].y, self.bodies[column][row].y2):
                    cellsColumn = column
                    cellsRow = row
        
        for column in range(cellsColumn-2, cellsColumn+2):
            for row in range(cellsRow-2, cellsRow+2):
                self.bodies[column][row].isMine = False
    
    
    def draw(self, display):
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                if not self.bodies[column][row].isVisible:
                    pg.draw.rect(display, DEFAULT, self.bodies[column][row].rect, 1)
                else:
                    if self.bodies[column][row].isMine: pg.draw.rect(display, (0, 50, 75), self.bodies[column][row].rect, 0);
                    else: pg.draw.rect(display, colorOrderedTuple[self.bodies[column][row].nearMines], self.bodies[column][row].rect, 0);
                
    
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

firstClickPerformed = False

while running:
    clock.tick(60)
    
    for event in pg.event.get():
        if event.type == pg.QUIT: running = False
        if event.type == MOUSEBUTTONDOWN and firstClickPerformed: grid.uncoverCell()
        elif event.type == MOUSEBUTTONDOWN and not firstClickPerformed:
            grid.clearMinesAround()
            grid.set_near_mines()
            grid.uncoverCell()
            firstClickPerformed = True
        
    display.fill(WHITE)
    grid.draw(display)
    
    pg.display.update()
    
    
    

pg.quit()    
