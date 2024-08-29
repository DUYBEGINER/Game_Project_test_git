import pygame, sys
from pygame.locals import *
import random

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GROUND_HEIGHT = 100

pygame.init()

# Ground setup
setGround = pygame.Rect((0, WINDOW_HEIGHT - GROUND_HEIGHT, WINDOW_WIDTH, GROUND_HEIGHT))

# Block class
class Block():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.fall_speed = random.randint(1, 3)  # Random fall speed

    def fall(self):
        if self.rect.bottom < WINDOW_HEIGHT - GROUND_HEIGHT:
            self.rect.y += self.fall_speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

### FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

# Screen setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Test Game')

# Create blocks with independent properties
Block_List = [
    Block(0, 0, 40, 40, RED),
    Block(50, 0, 40, 40, RED),
    Block(100, 0, 40, 40, RED),
    Block(150, 20, 40, 40, RED)
]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Fill screen with white
    screen.fill(WHITE)

    # Draw the ground
    GROUND = pygame.draw.rect(screen, '#571e15', setGround)

    # Update and draw each block independently
    for block in Block_List:
        block.fall()
        block.draw(screen)

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()