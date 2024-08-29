import pygame
# import spritesheet
# from GAME.spritesheet import SpriteSheet


#####################################################---INIT GAME---#########################################################
pygame.init()

#Set up the screen
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
BLACK = (0,0,0)


# class Player(pygame.sprite.Sprite):
#     def __init__(self,image,x,y):
#         pygame.sprite.Sprite.__init__(self)
#
#         self.sprite = []
#         self.is_animating = False
#         self.sprite.append(pygame.image.load(r"C:\Users\Admin\PycharmProjects\firstGame\GAME\item\Fire+Sparks-export1.jpg"))
#         self.sprite.append(pygame.image.load(r"C:\Users\Admin\PycharmProjects\firstGame\GAME\item\Fire+Sparks-export2.jpg"))
#         self.sprite.append(pygame.image.load(r"C:\Users\Admin\PycharmProjects\firstGame\GAME\item\Fire+Sparks-export3.jpg"))
#         self.sprite.append(pygame.image.load(r"C:\Users\Admin\PycharmProjects\firstGame\GAME\item\Fire+Sparks-export4.jpg"))
#         self.sprite.append(pygame.image.load(r"C:\Users\Admin\PycharmProjects\firstGame\GAME\item\Fire+Sparks-export5.jpg"))
#         self.sprite.append(pygame.image.load(r"C:\Users\Admin\PycharmProjects\firstGame\GAME\item\Fire+Sparks-export6.jpg"))
#         self.sprite.append(pygame.image.load(r"C:\Users\Admin\PycharmProjects\firstGame\GAME\item\Fire+Sparks-export7.jpg"))
#         self.current_sprite = 0
#         self.image = self.sprite[self.current_sprite]
#         self.image.set_colorkey('Black')
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)




# sprite_sheet_image = pygame.image.load('Idle-Sheet.png').convert_alpha()  #Conver alpha làm cho ảnh mịn hơn
# sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

#create animation
# animation_list = []
# animation_step = 4
# last_update = pygame.time.get_ticks()
# animation_cooldown = 150
# frame = 0
#
# for x in range(animation_step):
#     animation_list.append(Player1.get_img(x,64,80,3,BLACK))

#define player action variables
moving_left = False
moving_right = False


#Create character
class Sodier(pygame.sprite.Sprite):
    def __init__(self,image,width,height,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = image
        self.speed = speed
        self.width = width
        self.height = height
        self.direction = 1
        self.flip = False
        self.img_ani = pygame.Surface((width, height))
        self.rect = self.img_ani.get_rect()
        self.rect.center = (x,y)
        # self.image = pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))



    def animation_idle(self,frame,scale,color):
        self.img_ani.blit(self.sheet, (0,0), (frame * self.width,0,self.width,self.height))
        self.img_ani = pygame.transform.scale(self.img_ani,(self.width*scale,self.height*scale),)
        self.img_ani.set_colorkey(color)
        return self.img_ani

    def draw(self):
        screen.blit(pygame.transform.flip(self.sheet,self.flip,False),self.rect)

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

sprite_sheet_image = pygame.image.load('Idle-Sheet.png').convert_alpha()
Player1 = Sodier(sprite_sheet_image, 64,80,500,500, 10)

animation_list = []
animation_step = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0

for x in range(animation_step):
     animation_list.append(Player1.animation_idle(x,10,BLACK))

# Player1 = Sodier(200,500,3,20)
# Player2 = Sodier(400,500,3,5)


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

f = 0
# moving_sprite = pygame.sprite.Group()
# Fire = fire(100,100)
# moving_sprite.add(Fire)
########################################################## RUN GAME ################################################################
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    #Show game
    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.QUIT:
            running = False
        #keyboard press
        if event.type == pygame.KEYDOWN:
            # Fire.animate()
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
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame+=1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0
    for x in range(animation_step):
        screen.blit(animation_list[frame],Player1.rect)
    Player1.draw()
    Player1.move(moving_left, moving_right)
    pygame.display.update()
    # rect.x+=1
    # if rect.x == 800:
    #     rect.x = random.randint(0,720)
    #     rect.y = random.randint(0,720)

    # flip() the display to put your work on screen
    # moving_sprite.draw(screen)
    # moving_sprite.update()
    # pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()
#commit test