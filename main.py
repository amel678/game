import pygame ,sys
from setting import *



"""defidne radius birds"""
#y x axis on screen
x_E = 310
y_E = 100

x = 300
y = 400

L_x = x + 25
L_y = y

#size of Emu
width_Emu = 20
hight_Emu = 50
veloci_Emu = 0.01
Emu_c = blue
Emu_HP = 2

A_width_Emu = 20
A_hight_Emu = 50
A_Emu_c = blue
A_Emu_HP = 2
A_x_E = x_E + 100
A_y_E = y_E


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



pygame.init()
screen = pygame.display.set_mode((width_screen, hight_screen))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(Yellow)




    class Lazer:
        pygame.draw.rect(screen, L_colour, (L_x, L_y, 10, 10))

    class Emu_L:
        pygame.draw.rect(screen, red, (EL_x, EL_y, 10, 10))

    if  x < 800 - EL_v - width:
        EL_y += EL_v


    class Emu:
    #Emu
        pygame.draw.rect(screen, Emu_c, (x_E, y_E, width_Emu, hight_Emu))
        pygame.draw.rect(screen, A_Emu_c, (x_E + 100, y_E, A_width_Emu, A_hight_Emu))
        pygame.draw.rect(screen, B_Emu_c, (x_E + 200, y_E, B_width_Emu, B_hight_Emu))
        pygame.draw.rect(screen, C_Emu_c, (x_E - 100, y_E, C_width_Emu, C_hight_Emu))
        pygame.draw.rect(screen, D_Emu_c, (x_E - 200, y_E, D_width_Emu, D_hight_Emu))
        #speed Emu go down

    key_shoot = pygame.key.get_pressed()
    if key_shoot[pygame.K_SPACE]:
        shoot = 1
        L_colour = red
    if shoot == 1 and L_y > 0:
        L_y -= veloci_lazer
    else :
        shoot = 0
        L_colour = black
        L_y = y


    if Emu_HP == 0:
        width_Emu = 0
        hight_Emu = 0
        """Kills = Kills 
        print(screen,"Kills :"+ str(Kills)"""



    """A Emu"""
    if L_x > A_x_E and L_x < (A_x_E + width_Emu)and L_y > y_E  and  L_y < (y_E + A_width_Emu):
        A_Emu_c = red
        L_y = y
        shoot = 0
        A_Emu_HP = (A_Emu_HP - L_DMG)
    else:
        A_Emu_HP = A_Emu_HP
        A_Emu_c = A_Emu_c

    if A_Emu_HP == 0:
        A_width_Emu = 0
        A_hight_Emu = 0

    class Tank:
        pygame.draw.rect(screen, green, (x, y, width, hight))
         #tank movemnet
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

    key_move = pygame.key.get_pressed()
    if key_move[pygame.K_a] and x > veloci:
        L_x -= veloci
    if key_move[pygame.K_d] and x < 800 - veloci - width:
        L_x += veloci



    pygame.display.update()
    clock.tick()
