import pygame, sys
from pygame.examples.grid import WINDOW_WIDTH
from pygame.locals import *
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
setGround = pygame.Rect((0,300, WINDOW_WIDTH, 100))

class Block():
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def  current_pos(self):
        return self.rect.y
    def fall(self):
        block = pygame.draw.rect(screen, RED, self.rect)
        if block.bottom <= 260:
            self.rect.y +=1
        if block.bottom >260:
            self.rect.y = 0





### FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Test game')

x,y = (0,0)
block = pygame.Rect(0,0,40,40)

rand = 0

Block_List = []


Block1 = Block(0,0,40,40)
Block2 = Block(40,0,40,40)
Block3 = Block(80,0,40,40)
Block4 = Block(120,20,40,40)

Block_List.append(Block1)
Block_List.append(Block2)
Block_List.append(Block3)
Block_List.append(Block4)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(WHITE)
    # block2 = pygame.Surface((40,40))
    # block2.fill(RED)
    #
    # screen.blit(block2,(0,0))
    # block1 = pygame.draw.rect(screen,RED,block)
    GROUND = pygame.draw.rect(screen,'#571e15',setGround)
    current_time = pygame.time.get_ticks()
    if Block_List[rand].current_pos() <= 150:
        Block_List[rand].fall()
    else:
        rand = random.randint(0, 3)

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()