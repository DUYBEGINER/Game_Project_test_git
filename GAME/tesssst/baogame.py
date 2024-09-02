import pygame, random
from pygame.sprite import Group, Sprite

pygame.init()

# Định nghĩa màn hình game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Miner Game')
clock = pygame.time.Clock()
FPS = 60


def draw_screen():
    screen.fill(bg)
    pygame.draw.line(screen, RED, (0, 300), (400, 300), 1)


# Định nghĩa màu sắc
bg = (144, 201, 120)
RED = (255, 0, 0)
img_ground = pygame.Rect((0, SCREEN_HEIGHT - SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT))

# Định nghĩa các biến của trò chơi
GRAVITY = 0.75
COOLDOWN_SPAWN = 120
count = 0


# Định nghĩa class Đá
class Stone(Sprite):
    def __init__(self, scale):
        Sprite.__init__(self)
        self.vel_y = 0
        self.scale = scale
        self.in_air = True
        self.collision_ground = False
        self.list_check = []
        img = pygame.image.load('block.jpg').convert_alpha()
        self.image = pygame.transform.scale(img, (self.scale * img.get_width(), self.scale * img.get_height()))
        self.rect = self.image.get_rect()
        y = random.randrange(1, 11, 1)
        self.rect.center = ((int)(y * self.rect.width), -10)

    def update(self):
        dy = 0
        self.check_collision_stone()
        self.check_collision_group()
        if self.in_air:
            self.vel_y += GRAVITY
            if self.vel_y > 5:
                self.vel_y = 5
            dy = self.vel_y
        self.rect.y += dy
        self.tmp_function()

    def check_collision_stone(self):
        for i in stones:
            if self != i:
                if (self.rect.colliderect(i.rect) and
                        self.rect.bottom <= i.rect.top + 5 and
                        self.rect.bottom >= i.rect.top):
                    self.in_air = False
                    self.vel_y = 0
                    self.rect.bottom = i.rect.top + 1
                    break
                else:
                    self.in_air = True

    def check_collision_group(self):
        for i in grounds:
            if (self.rect.colliderect(i.rect) and
                    self.rect.bottom <= i.rect.top + 5 and
                    self.rect.bottom >= i.rect.top):
                self.collision_ground = True
                self.in_air = False
                self.vel_y = 0
                self.rect.bottom = i.rect.top + 1
                break
            else:
                self.in_air = True

    def tmp_function(self):
        for i in stones:
            if i.collision_ground:
                self.list_check.append(i)
        if len(self.list_check) == 10:
            for i in self.list_check:
                i.kill()
            self.list_check = []
        self.list_check = []


# Tạo nhóm các đối tượng
stones = Group()
update_time = pygame.time.get_ticks()


# Tự động sinh ra các đá
def re_spawn_stone():
    stone = Stone(2)
    stones.add(stone)


# Class Ground
class Ground(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.scale = 2
        self.image = pygame.transform.scale(img_ground,
                                            (self.scale * img_ground.get_width(), self.scale * img_ground.get_height()))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    # def draw(self)


# respawn ground
grounds = Group()
for i in range(0, 8):
    ground = Ground(i * img_ground.width() * 2, 300)
    grounds.add(ground)
# MAIN LOOP
running = True
while running:
    clock.tick(FPS)

    draw_screen()
    if pygame.time.get_ticks() - update_time > COOLDOWN_SPAWN:
        count += 1
        update_time = pygame.time.get_ticks()
        re_spawn_stone()

    stones.update()
    stones.draw(screen)

    grounds.update()
    grounds.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
