import random
import time
from datetime import datetime
from datetime import timedelta
import pygame
from pygame.locals import *

WHITE = (255,255,255,255);
BLACK = (0,0,0,255);
size = 1280, 757;
width, height = size;

pygame.init();
screen = pygame.display.set_mode(size);
pygame.display.set_caption("Go to horny jail");
running = True;
debug = False;
clock = pygame.time.Clock();
lastCollide = None;
mode = random.randint(0, 1);
jpcPoints = 0;
npcPoints = 0;


ball = pygame.image.load("PythonCode/ponk/ball.png");
jpcPaddle = pygame.image.load("PythonCode/ponk/paddle.png");
npcPaddle = pygame.image.load("PythonCode/ponk/paddle.png");
pongEffect = pygame.mixer.Sound("PythonCode/ponk/pong.ogg");
bonkEffect = pygame.mixer.Sound("PythonCode/ponk/bonk.ogg");
font = pygame.font.Font("PythonCode/ponk/dot.ttf", 50);
fontDebug = pygame.font.Font("PythonCode/ponk/dot.ttf", 15)
jpcRect = jpcPaddle.get_rect();
jpcRect = jpcRect.move(50, 375);
npcRect = npcPaddle.get_rect();
npcRect = npcRect.move(width - 70, 375);
ballRect = ball.get_rect();
ballRect = ballRect.move(random.choice(range(600, 700)), random.choice(range(500, 600)));
speed = [random.choice(range(8, 11)),random.choice(range(8, 11))];
if mode == 1: speed = [random.choice((-8, 8)), random.choice((-8, 8))]

def restartBall(ballRect, lastCollide):
    ballRect.x = random.choice(range(600, 700));
    ballRect.y = random.choice(range(500, 600));
    lastCollide = datetime.now();


while running:

    clock.tick(60);
    for event in pygame.event.get(): 
        if event.type == KEYDOWN:    
            if event.key == K_SPACE and not debug: debug = True;
            elif event.key == K_SPACE and debug: debug = False;
        if event.type == QUIT: running = False;

    if ((ballRect.colliderect(jpcRect) and ballRect.top != jpcRect.bottom and ballRect.bottom != jpcRect.top) or (ballRect.colliderect(npcRect) and ballRect.top != npcRect.bottom and ballRect.bottom != npcRect.top)):
        if lastCollide is None or (datetime.now() - lastCollide).seconds > 0.4:
            lastCollide = datetime.now();
            pongEffect.play();
            speed[0] = -speed[0];
            if mode == 1: speed[1] = -speed[1];          
    if (ballRect.top < 150 or ballRect.bottom > height or (ballRect.colliderect(jpcRect) and (ballRect.top == jpcRect.bottom or ballRect.bottom == jpcRect.top)) or (ballRect.colliderect(npcRect) and (ballRect.top == npcRect.bottom or ballRect.bottom == npcRect.top))):
        pongEffect.play();
        speed[1] = -speed[1];
    if ballRect.left < 0:
        bonkEffect.play();
        restartBall(ballRect, lastCollide);
        npcPoints += 1;
        time.sleep(2);
    if ballRect.right > width:
        bonkEffect.play();
        restartBall(ballRect, lastCollide);
        jpcPoints += 1; 
        time.sleep(2);

    pressed = pygame.key.get_pressed();
    if pressed[pygame.K_w] and jpcRect.top > 150: jpcRect.move_ip([0, -5]);
    if pressed[pygame.K_s] and jpcRect.bottom < height: jpcRect.move_ip([0, 5]);
    if pressed[pygame.K_UP] and npcRect.top > 150: npcRect.move_ip([0, -5]);
    if pressed[pygame.K_DOWN] and npcRect.bottom < height: npcRect.move_ip([0, 5]);

    ballRect = ballRect.move(speed);
    screen.fill(BLACK);
    pointsTxt = font.render(str(jpcPoints) + "   |   " + str(npcPoints), True, WHITE);
    pointsTxtRect = pointsTxt.get_rect();
    pointsTxtRect.center = (width//2, 60);
    pygame.draw.rect(screen, BLACK, pointsTxtRect, 1);
    pygame.draw.rect(screen, BLACK, ballRect, 1);
    pygame.draw.rect(screen, WHITE, ((0, 145), (width, 5)), 0);
    pygame.draw.rect(screen, BLACK, jpcRect, 1);
    pygame.draw.rect(screen, BLACK, npcRect, 1);
    screen.blit(pointsTxt, pointsTxtRect);
    screen.blit(ball, ballRect);
    screen.blit(jpcPaddle, jpcRect);
    screen.blit(npcPaddle, npcRect);
    
    #DEBUG PURPOSE:
    if debug:
        ballSpeedTxt = fontDebug.render("B_Speed: (" + str(speed[0]) + ", " + str(speed[1]) + ")", True, WHITE);
        ballSpeedTxtRect = ballSpeedTxt.get_rect();
        ballSpeedTxtRect = ballSpeedTxtRect.move(10, 10);
        pygame.draw.rect(screen, BLACK, ballSpeedTxtRect, 1);
        screen.blit(ballSpeedTxt, ballSpeedTxtRect);
        modeTxt = fontDebug.render("Mode: " + str(mode), True, WHITE);
        modeTxtRect = modeTxt.get_rect();
        modeTxtRect = modeTxtRect.move(10, 50);
        pygame.draw.rect(screen, BLACK, modeTxtRect, 1);
        screen.blit(modeTxt, modeTxtRect);
        lastCollideTxt = fontDebug.render("L_Collide: " + str(lastCollide), True, WHITE);
        lastCollideTxtRect = lastCollideTxt.get_rect();
        lastCollideTxtRect = lastCollideTxtRect.move(10, 90);
        pygame.draw.rect(screen, BLACK, lastCollideTxtRect, 1);
        screen.blit(lastCollideTxt, lastCollideTxtRect);

    pygame.display.update();


pygame.quit();