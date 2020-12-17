import pygame as pg
from pygame.locals import *
import math

class BodyPart():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class Snake():
    def __init__(self, bodies = [BodyPart(500, 0), BodyPart(520, 0)]):
        self.bodies = bodies;

    def update(self):
        draw();
    
    def draw(self):
        for BodyPart() in bodies:
            pg.draw.rect(screen, (255, 0, 0), Rect(BodyPart.x, BodyPart.y, 30, 30));


def drawGrid():
    cellWidth = 30;
    cellHeight = 30;
    rows = round(width / cellWidth);
    columns = math.floor(height / cellHeight);

    for column in range(0, columns):
        for row in range(0, rows):
            pg.draw.rect(screen, (255, 255, 255), Rect(cellWidth * row, cellHeight * column, cellWidth, cellHeight), 1);


BLACK = (0, 0, 0);
WHITE = (255, 255, 255);
width = 1260;
height = 750;

pg.init();
screen = pg.display.set_mode((width, height));
pg.display.set_caption("Snek gaem");
running = True;

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False;
    
    screen.fill(BLACK);
    drawGrid();
    
    pg.display.update();

pg.quit();