import random
import pygame
from pygame.locals import *

def bonkColorChange(lcurr_color):
    logo_pxarr = pygame.PixelArray(logo);
    nxt_color = lcurr_color;
    while (nxt_color == lcurr_color):
        nxt_color = random.choice(colors_list);
    logo_pxarr.replace(lcurr_color,nxt_color);
    del logo_pxarr;
    return nxt_color;

RED =       (255,0,0,255);
BLUE =      (0,0,255,255);
GREEN =     (0,255,0,255);
YELLOW =    (255,255,0,255);
CYAN =      (0,255,255,255);
MAGENTA =   (255,0,255,255);
BLACK =     (0,0,0,255);
GRAY =      (127,127,127,255);
WHITE =     (255,255,255,255);
colors_list = [RED,BLUE,GREEN,YELLOW,CYAN,MAGENTA,GRAY,WHITE];
size = 1000, 620;
width, height = size;

pygame.init();
screen = pygame.display.set_mode(size);
running = True;

logo = pygame.image.load("PythonCode/dvdmeme/dvd.png");
curr_color = WHITE;
rect = logo.get_rect();
speed = [2,2];

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False;

    rect = rect.move(speed);
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0];
        curr_color = bonkColorChange(curr_color);       

    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1];
        curr_color = bonkColorChange(curr_color);

    screen.fill(pygame.Color(0,0,0,0));
    pygame.draw.rect(screen, BLACK, rect, 1);
    screen.blit(logo,rect);
    pygame.display.update();

pygame.quit();
