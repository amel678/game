import pygame ,sys
from setting import *


pygame.init()
screen = pygame.display.set_mode((width_screen, hight_screen))
clock = pygame.time.Clock()

class Emu(pygame.sprite.Sprite):
    #Emu
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.veloci_Emu = 0.01
        self.Emu_HP = 2
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))

class E_Lazer(pygame.sprite.Sprite):
    def __int__(self, width, height, color, el_x, el_y):
        super().__init__()
        self. VEL_L = 0.02
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(el_x, el_y))

class tank(pygame.sprite.Sprite):
    #Emu
    def __init__(self, width, height, color, x, y, health):
        super().__init__()
        self.veloci_Emu = 0.01
        self.Emu_HP = 2
        self.image = pygame.Surface(60, 30,x, y)
        self.image.fill(green)
        self.HP = health
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self):
        veloci = 0.2

        key_move = pygame.key.get_pressed()
        if key_move[pygame.K_LEFT] and self.rect.x > veloci:
            self.rect.x -= veloci
        if key_move[pygame.K_RIGHT] and self.rect.x < 800 - veloci - width:
            self.rect.x += veloci
        if key_move[pygame.K_UP] and self.rect.y > veloci:
            self.rect.y -= veloci
        if key_move[pygame.K_DOWN] and self.rect.y < 500 - hight - veloci:
            self.rect.y += veloci



class Lazer(pygame.sprite.Sprite):
    #Emu
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.veloci_Emu = 0.01
        self.Emu_HP = 2
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))

#Positions of elements y x axis on screen
x_E = 310
y_E = 100

x = 300
y = 400

L_x = x + 25
L_y = y

#lazer
L_colour = black
shoot = 0
L_DMG = 1
veloci_lazer = 0.07

#size of tank
width = 60
hight = 30
#set mouvement speed
veloci = 0.2

Kills = 0


enemies = pygame.sprite.Group()
ex = 100
ey = 100
emu_c = blue
emu_w = 20
emu_y = 50

for i in range(7):
    e = Emu(emu_w, emu_y, emu_c, ex, ey)
    ex += 100
    enemies.add(e)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    screen.fill(Yellow)
    enemies.draw(screen)
    pygame.draw.rect(screen, L_colour, (L_x, L_y, 10, 10))
    tank_group.draw(screen)


    pygame.display.update()
    clock.tick()


