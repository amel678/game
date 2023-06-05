import pygame ,sys
from setting import *
import random

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

    """
    pygame.draw.rect(screen, A_Emu_c, (A_x_E, A_y_E, A_width_Emu, A_hight_Emu))
    pygame.draw.rect(screen, B_Emu_c, (B_x_E, B_y_E, B_width_Emu, B_hight_Emu))
    pygame.draw.rect(screen, C_Emu_c, (310 - 100, 100, C_width_Emu, C_hight_Emu))
    pygame.draw.rect(screen, D_Emu_c, (310 - 200, 100, D_width_Emu, D_hight_Emu))
    #speed Emu go down
    """

"""defidne radius birds"""
#y x axis on screen
x_E = 310
y_E = 100

x = 300
y = 400

L_x = x + 25
L_y = y

#size of Emu


A_width_Emu = 20
A_hight_Emu = 50
A_Emu_c = blue
A_Emu_HP = 2
A_x_E = 410
A_y_E = 100


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
for i in range(5):
    e = Emu(20, 50, blue, ex, ey)
    ex += 100
    enemies.add(e)


Lazer_Emu = pygame.sprite.Group()
fire = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key_move = pygame.key.get_pressed()
    if key_move[pygame.K_LEFT] and x > veloci:
        x -= veloci
        L_x -= veloci
    if key_move[pygame.K_RIGHT] and x < 800 - veloci - width:
        x += veloci
        L_x += veloci
    if key_move[pygame.K_UP] and y > veloci:
        y -= veloci
        L_y -= veloci
    if key_move[pygame.K_DOWN] and y < 500 - hight - veloci:
        y += veloci
        L_y += veloci
    if key_move[pygame.K_a] and x > veloci:
        L_x -= veloci
    if key_move[pygame.K_d] and x < 800 - veloci - width:
        L_x += veloci
    if key_move[pygame.K_SPACE]:
        shoot = 1
        L_colour = red
    if shoot == 1 and L_y > 0:
        L_y -= veloci_lazer
    else :
        shoot = 0
        L_colour = black
        L_y = y

    screen.fill(Yellow)
    enemies.draw(screen)
    pygame.draw.rect(screen, L_colour, (L_x, L_y, 10, 10))
    pygame.draw.rect(screen, green, (x, y, width, hight))

    if L_x < ex and L_x < (ex + 20) and L_y < (ey + 50 ):


    fire += 1
    if fire == 60:
        enemy_list = list(enemies)
        e = random.choice(enemy_list)


        print(e)
        fire = 0







    pygame.display.update()
    clock.tick()
