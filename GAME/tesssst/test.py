from turtledemo.forest import doit1
import pygame, sys
from pygame.locals import *
import random


# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
GROUND_HEIGHT = 50
BACKGROUND_IMAGE1 = pygame.image.load("background3.png")
BACKGROUND_IMAGE2 = pygame.image.load("background1.png")
pygame.init()

# Screen setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Stacking Blocks')


### FPS ###
FPS = 120
fpsClock = pygame.time.Clock()
last_time = pygame.time.get_ticks()


# Load block image
block_image = pygame.image.load('blocknew.png')
block_image = pygame.transform.scale(block_image, (BLOCK_SIZE, BLOCK_SIZE))

# Load background image
Ground_image = pygame.image.load('ground.png')
Ground_image = pygame.transform.scale(Ground_image, (WINDOW_WIDTH, GROUND_HEIGHT))
# Ground setup
class Ground(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = Ground_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# limit max col
max_col = [0]*(WINDOW_WIDTH // BLOCK_SIZE)

# Block class
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # Call the parent class (Sprite) constructor
        self.image = block_image  # Assign the image to the sprite
        self.rect = self.image.get_rect()  # Get the rect for positioning
        self.rect.topleft = (x, y)  # Set the initial position
        self.fall_speed = 2  # Fall speed

    def update(self, blocklist):
        if self.rect.bottom < WINDOW_HEIGHT - GROUND_HEIGHT:
            self.rect.y += self.fall_speed
        for other_block in blocklist:
            if other_block != self and self.rect.colliderect(other_block.rect):
                self.rect.y = other_block.rect.top - self.rect.height
                break


# Function to check and clear full rows
def check_and_clear_rows(block_group):
    rows = []
    # Tạo dictionary để đếm số lượng block trên mỗi hàng
    for block in block_group:
        last_row = WINDOW_HEIGHT - GROUND_HEIGHT - BLOCK_SIZE
        row = block.rect.y
        if row == last_row:
            rows.append(block)

    # Kiểm tra xem hàng nào đã được lấp đầy
    if len(rows) >= WINDOW_WIDTH // BLOCK_SIZE:
            # Xóa các block trên hàng này
            for block in rows:
                block_group.remove(block)
            # Cập nhật lại số cột tối đa
            for i in range(len(max_col)):
                max_col[i] -= 1

# Sprite group
block_group = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
ground_group.add(Ground(0, 350))


# Main game loop
while True:
    screen.blit(BACKGROUND_IMAGE2, (0, 0))
    screen.blit(BACKGROUND_IMAGE1, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Fill screen with white
    # screen.fill(WHITE)

    current_time = pygame.time.get_ticks()
    if current_time - last_time > 1000:
        while True:
            rand = random.randint(0, WINDOW_WIDTH // BLOCK_SIZE - 1)
            if max_col[rand] <= 2:
                max_col[rand] += 1
                break


        block = Block(rand * BLOCK_SIZE, -10)
        block_group.add(block)
        last_time = current_time

    # Update all sprites in the group
    block_group.update(block_group)

    # Kiểm tra và xóa hàng đã được lấp đầy
    check_and_clear_rows(block_group)

    # Draw all sprites in the group
    block_group.draw(screen)
    ground_group.draw(screen)
    # Draw the ground
    # GROUND = pygame.draw.rect(screen, '#571e15', setGround)


    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
