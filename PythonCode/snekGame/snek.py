import pygame as pg
from pygame.locals import *
import math
import random
import time


class bodyPart():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        

class Snake():
    def __init__(self, bodies = [bodyPart(620, 60), bodyPart(600, 60)], direction = (1, 0), waitT = pg.time.get_ticks(), lastDrift = pg.time.get_ticks()):
        self.bodies = bodies;
        self.direction = direction;
        self.waitT = waitT;
        self.lastDrift = lastDrift;

    def updateLocVars(self):
        for body in self.bodies:
            #Adding key with assigned value to globals() creating in result a new global variable :D
            globals()["PrevX" + str(self.bodies.index(body))] = body.x;       #Previous X value: PrevXi   i = obj index
            globals()["PrevY" + str(self.bodies.index(body))] = body.y;       #Previous Y value: PrevYi   i = obj index

    def update(self):
        #Snake direction update
        pressed = pg.key.get_pressed();
        if pressed[pg.K_RIGHT] and self.direction != (-1, 0) and pg.time.get_ticks() - self.lastDrift > 120: 
            self.direction = (1, 0);
            self.lastDrift = pg.time.get_ticks();
        elif pressed[pg.K_LEFT] and self.direction != (1, 0) and pg.time.get_ticks() - self.lastDrift > 120: 
            self.direction = (-1, 0);
            self.lastDrift = pg.time.get_ticks();
        elif pressed[pg.K_DOWN] and self.direction != (0, -1) and pg.time.get_ticks() - self.lastDrift > 120: 
            self.direction = (0, 1);
            self.lastDrift = pg.time.get_ticks();
        elif pressed[pg.K_UP] and self.direction != (0, 1) and pg.time.get_ticks() - self.lastDrift > 120: 
            self.direction = (0, -1);
            self.lastDrift = pg.time.get_ticks();
        #Snake movement update
        if pg.time.get_ticks() - self.waitT > 70:
            self.move();
        #Snake check not collided update
        if len(self.bodies) > 2:
            for body in self.bodies:
                for i in self.bodies:
                    if body.x == i.x and body.y == i.y and body != i and body != self.bodies[-1] and i != self.bodies[-1]:
                        screen.fill((0, 0, 0));
                        self.drawSnake();
                        drawGrid();
                        pg.draw.rect(screen, (255, 0, 0), Rect(body.x, body.y, 20, 20));
                        self.die();
        if self.bodies[0].x >= 1260 or self.bodies[0].y >= 750 or self.bodies[0].x < 0 or self.bodies[0].y < 0:
            screen.fill((0, 0, 0));
            self.drawSnake();
            drawGrid();
            pg.draw.rect(screen, (255, 0, 0), Rect(self.bodies[1].x, self.bodies[1].y, 20, 20));
            self.die();

        self.updateLocVars();
        #Draw updated snake   
        self.drawSnake();

    def die(self):
        pg.display.update();
        time.sleep(3);
        globals()["running"] = False;        

    def move(self):
        self.waitT = pg.time.get_ticks();
        for body in self.bodies:
            if self.bodies.index(body) == 0:
                body.x += self.direction[0] * 20;
                body.y += self.direction[1] * 20;
            else:
                body.x = globals().get("PrevX" + str(self.bodies.index(body) - 1));
                body.y = globals().get("PrevY" + str(self.bodies.index(body) - 1));
            
    def drawSnake(self):
        for body in self.bodies:
            pg.draw.rect(screen, (0, 255, 0), Rect(body.x, body.y, 20, 20));
    
    def grow(self):
        self.bodies.append(bodyPart(globals().get("PrevX" + str(self.bodies.index(self.bodies[-1]))), globals().get("PrevY" + str(self.bodies.index(self.bodies[-1])))));


class Food():
    def __init__(self, x = random.choice(range(10, 1251, 20)), y = random.choice(range(10, 741, 20)), rect = Rect(0, 0, 0, 0)):
        self.x = x;
        self.y = y;
        self.rect = Rect(x+10 , y+10, 20, 20);
    
    def update(self):
        self.drawFood();

    def respawn(self):
            self.x = random.choice(range(10, 1251, 20));
            self.y = random.choice(range(10, 741, 20));
            self.drawFood();
    
    def drawFood(self):
        pg.draw.circle(screen, (255, 0 ,0), (self.x, self.y), 10);
        pg.display.update();

def drawGrid():
    cellWidth = 20;
    cellHeight = 20;
    rows = round(width / cellWidth);
    columns = math.floor(height / cellHeight);

    for column in range(0, columns):
        for row in range(0, rows):
            pg.draw.rect(screen, (0, 0, 0), Rect(cellWidth * row, cellHeight * column, cellWidth, cellHeight), 1);


BLACK = (0, 0, 0);
WHITE = (255, 255, 255);
width = 1260;
height = 750;

pg.init();
clock = pg.time.Clock();
screen = pg.display.set_mode((width, height));
pg.display.set_caption("Snek gaem");
running = True;
lastEat = pg.time.get_ticks();
snake = Snake();
prevSnekLen = len(snake.bodies);
snake.updateLocVars();
food = Food();

while running:
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                snake.grow();
        if event.type == QUIT:
            running = False;

    screen.fill(BLACK);
    if len(snake.bodies) > 0 and food.x - 10 == snake.bodies[0].x and food.y - 10 == snake.bodies[0].y and pg.time.get_ticks() - lastEat > 100:
        lastEat = pg.time.get_ticks();
        food.respawn();
        snake.grow();

    #drawGrid();
    snake.update();
    #if snake.die() and len(snake.bodies) > 2: running = False;
    drawGrid();
    food.drawFood();
    pg.display.update();
    clock.tick(60);
    #print(str(snake.bodies[0].x) + " " +str(snake.bodies[0].y) + " || " + str(food.x) + " " + str(food.y));

pg.quit();