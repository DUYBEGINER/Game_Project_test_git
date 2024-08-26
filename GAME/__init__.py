from random import random

import pygame
import random


pygame.init()
#Set up the screen
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Set up time
clock = pygame.time.Clock()
running = True
rect = pygame.Rect(50, 50, 20, 20)
#Title and icon game
pygame.display.set_caption("New game")
icon=pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    python = pygame.image.load('background.jpg')
    background = pygame.transform.scale(python,(1280,720))
    pygame.draw.rect(screen, (255, 255, 255), rect)
    rect.x+=1
    if rect.x == 800:
        rect.x = random.randint(0,720)
        rect.y = random.randint(0,720)
    screen.blit(background,(0, 0))
    pygame.display.update()
    # flip() the display to put your work on screen
    clock.tick(120)  # limits FPS to 60
    time = clock.get_time()
pygame.quit()