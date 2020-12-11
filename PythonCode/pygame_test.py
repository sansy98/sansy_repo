import pygame
from pygame.locals import *

RED =       (255,0,0);
BLUE =      (0,0,255);
GREEN =     (0,255,0);
YELLOW =    (255,255,0);
CYAN =      (0,255,255);
MAGENTA =   (255,0,255);
BLACK =     (0,0,0);
GRAY =      (127,127,127);
WHITE =     (255,255,255);

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, K_y:YELLOW, K_m:MAGENTA, K_c:CYAN, K_w:WHITE}

pygame.init();

running = True;
background = GRAY;
screen = pygame.display.set_mode((1280,800));   #DISPLAYS SCREEN 

while running:                                  #PROGRAM LOOP
    for event in pygame.event.get():            #EVENT LOOP
        print(event);                           #DISPLAY ONGOING EVENTS IN CONSOLE

        #======DRAW SECTION====== 
        screen.fill(background);
        pygame.display.update();
        #========================

        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key];
        caption = "background color = " + str(background);
        pygame.display.set_caption(caption);

        '''
        if event.type == KEYDOWN:               #If any key is pressed
            if event.key == pygame.K_r:         #If that key is R turn screen red
                background = RED;
            elif event.key == pygame.K_g:       #If that key is G turn screen green
                background = GREEN;
            elif event.key == pygame.K_b:       #If that key is B turn screen blue
                background = BLUE;
        '''

        if event.type == 256:                   #WHEN CLOSING WINDOW THE GAME STOPS (QUIT == 256)
            running = False;

pygame.quit();                                  #This ends the application properly