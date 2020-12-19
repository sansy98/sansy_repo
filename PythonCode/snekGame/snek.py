import pygame as pg
from pygame.locals import *
import math

CELL = 20;

class bodyPart():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        

class Snake():
    def __init__(self, bodies = [bodyPart(620, 60), bodyPart(600, 60)], direction = (1, 0), waitT = pg.time.get_ticks()):
        self.bodies = bodies;
        self.direction = direction;
        self.waitT = waitT;

    def updateLocVars(self):
        for body in self.bodies:
            #Adding key with assigned value to globals() creating in result a new global variable :D
            globals()["PrevX" + str(self.bodies.index(body))] = body.x;
            globals()["PrevY" + str(self.bodies.index(body))] = body.y;

    def update(self):
        #Snake direction update
        pressed = pg.key.get_pressed();
        if pressed[pg.K_RIGHT] and self.direction != (-1, 0): self.direction = (1, 0);
        elif pressed[pg.K_LEFT] and self.direction != (1, 0): self.direction = (-1, 0);
        elif pressed[pg.K_DOWN] and self.direction != (0, -1): self.direction = (0, 1);
        elif pressed[pg.K_UP] and self.direction != (0, 1): self.direction = (0, -1);
        #Snake movement update
        if pg.time.get_ticks() - self.waitT > 100:
            self.move();
        self.updateLocVars();
        #Draw updated snake   
        self.draw();

    def move(self):
        self.waitT = pg.time.get_ticks();
        for body in self.bodies:
            if self.bodies.index(body) == 0:
                body.x += self.direction[0] * 20;
                body.y += self.direction[1] * 20;
            else:
                body.x = globals().get("PrevX" + str(self.bodies.index(body) - 1));
                body.y = globals().get("PrevY" + str(self.bodies.index(body) - 1));
            
    def draw(self):
        for body in self.bodies:
            pg.draw.rect(screen, (255, 0, 0), Rect(body.x, body.y, 20, 20));
       # pg.draw.rect(screen, (255, 0, 0), Rect(self.bodies[-1].x, self.bodies[-1].y, 20, 20));

def drawGrid():
    cellWidth = 20;
    cellHeight = 20;
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
snake = Snake();
snake.updateLocVars();

while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False;
    
    screen.fill(BLACK);
    snake.update();
    drawGrid();
    pg.display.update();

pg.quit();