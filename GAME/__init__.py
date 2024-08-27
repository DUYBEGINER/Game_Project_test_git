
import pygame

import spritesheet
from GAME.spritesheet import SpriteSheet
#####################################################---INIT GAME---#########################################################
pygame.init()



#Set up the screen
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BLACK = (0,0,0)

sprite_sheet_image = pygame.image.load('Idle-Sheet.png').convert_alpha()  #Conver alpha làm cho ảnh mịn hơn
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

frame_0 = sprite_sheet.get_img(0,64,80,3, BLACK)
frame_1 = sprite_sheet.get_img(1,64,80,3, BLACK)
frame_2 = sprite_sheet.get_img(2,64,80,3, BLACK)
frame_3 = sprite_sheet.get_img(3,64,80,3, BLACK)

#define player action variables
moving_left = False
moving_right = False


#Create character
class Sodier(pygame.sprite.Sprite):
    def __init__(self,x,y,scale,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load(r"C:\Users\Admin\PycharmProjects\firstGame\GAME\Asset\Idle\Idle.gif")
        self.image = pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)

    def move(self, moveing_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0

        if moving_left:
            dx -= self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx += self.speed
            self.flip = False
            self.direction = 1

        #update position
        self.rect.x += dx
        self.rect.y += dy


Player1 = Sodier(200,500,3,5)
Player2 = Sodier(400,500,3,5)


#Set up time
clock = pygame.time.Clock()
running = True
# rect = pygame.Rect(50, 50, 20, 20)


#Title and icon game
pygame.display.set_caption("New game")
icon=pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)


#Set background
bgr = pygame.image.load('background2.jpg')
background = pygame.transform.scale(bgr,(1280,720))

########################################################## RUN GAME ################################################################
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # Player1.draw()
    # Player1.move(moving_left, moving_right)

    #Show game
    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.QUIT:
            running = False
        #keyboard press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                running = False
        #keyboard button release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("black")

    # RENDER YOUR GAME HERE
    screen.blit(background, (0, 0))


    screen.blit(frame_0, (0, 0))
    screen.blit(frame_1, (100, 0))
    screen.blit(frame_2, (200, 0))
    screen.blit(frame_3, (300, 0))
    pygame.display.update()
    # rect.x+=1
    # if rect.x == 800:
    #     rect.x = random.randint(0,720)
    #     rect.y = random.randint(0,720)

    # flip() the display to put your work on screen


    clock.tick(60)  # limits FPS to 60
    time = clock.get_time()
pygame.quit()
#commit test