import pygame as pg
from pygame.locals import *
from math import sqrt


SIZE = 750
G = 6.67 * 10**-11

class Particle():
    
    def __init__(self, pos, m):
        self.x = pos[0]
        self.y = pos[1]
        self.v = 0                                #Particle's velocity, starts at 0
        self.d = SIZE-pos[1]/30                   #30px == 1m.    Distance from gravitational center
        self.h = self.d                           #Same as d but only from where the object started falling
        self.m = m                                #Object's mass
        self.isFalling = True
        self.hasStopped = False
        self.historic = [0, 0]
        self.historicIndex = 0
    
    #Checks if velocity remains constant, which means that the object has stopped. 
    #Used to prevent the object from going through the floor
    def checkHistoric(self):
        if self.historicIndex > 1: self.historicIndex = 0
        self.historic[self.historicIndex] = self.v
        self.historicIndex += 1
        flag = True
        for i in range(0, 2): 
            if abs(self.v - self.historic[i]) > 0.0001:         #Error margin of 0.0001
                flag = False
                break
        if flag: self.hasStopped = True

    def update(self, g):
        if not self.hasStopped:
            self.d = SIZE-self.y/10
            self.v += g/60                              #60 fps
            self.y += self.v/2                          #60 fps but it's 2 because 30px=1m so 60/30 = 2
            if self.y+20 >= SIZE and self.isFalling: 
                self.v = -self.v/(1.0 + self.m/10)     #Calculates bounce negative velocity, the more massive the object is, the less it will bounce
                self.isFalling = False
            if not self.isFalling and self.v < 5 and self.v > -5:
                self.h = self.d
                self.isFalling = True
            self.checkHistoric()
        else:
            self.y = SIZE-20
            self.v = 0




if __name__ == "__main__":
    try:
        M = float(input("Introduce la masa (M) del planeta en kg (Ejm, Tierra = ->5.97<- * 10**24): "))
    except ValueError:
        M = 5.97                #Defaults to Earth's value

    try:
        expM = int(input("Introduce el exponente: (M *10^?): "))
    except ValueError:
        expM = 24               #Defaults to Earth's value
    M *= 10**expM               #Applies scientific notation

    try:
        R = float(input("Introduce el radio del planeta en km (Ejm, Tierra = 6501): "))
    except ValueError:
        R = 6501                #Defaults to Earth's value
    R *= 1000                   #Converts radius from km to m

    m = 1           #Next particle's mass starts at 1 by default
    g = (G*M)/R**2  #Calculates the gravitational acceleration using Newton's law of universal gravitation

    pg.init()
    displayFont = pg.font.SysFont('Arial', 20)
    clock = pg.time.Clock()
    screen = pg.display.set_mode((SIZE, SIZE))
    pg.display.set_caption("Gravity Simulator")
    running = True
    started = False       #Indicates if the first particle has been created in order to start the simulation 
    particles = []

    #SIMULATION MAIN LOOP
    while running:

        for event in pg.event.get():
            if event.type == QUIT: running = False
            if event.type == MOUSEBUTTONDOWN:
                started = True
                particles.append(Particle(pg.mouse.get_pos(), m))
            if event.type == KEYDOWN:
                if event.key == K_UP: m += 1               #Increments next particle's mass
                if event.key == K_DOWN and m>1: m -= 1     #Decrements next particle's mass
                if event.key == K_LEFT: m = 1              #Resets next particle's mass (Defaults it to 1)
        
        screen.fill((255, 255, 255))
        if started:
            for particle in particles:
                particle.update(g)                                                  #Updates particle
                pg.draw.circle(screen, (255, 0, 0), (particle.x, particle.y), 20)   #Draws particle
        
        #TEXT DISPLAYING
        massDisplaySurface = displayFont.render(f"Prox. masa: {m}", False, (0, 0, 0))
        screen.blit(massDisplaySurface, (0, 0))

        #FOR DEBUGGING PURPOSE:
        #print(m)
        #print(f"v: {particle.v} | g: {g} | isFalling: {particle.isFalling} | hasStopped: {particle.hasStopped}")
        
        pg.display.update()
                