
"""defidne radius birds"""
#y x axis on screen
x_E = 310
y_E = 100

x = 300
y = 400

L_x = x + 25
L_y = y



#lazer
L_colour = (0,0,0)
shoot = 0
L_DMG = 1
veloci_lazer = 0.07

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
Yellow = (255, 255, 0)

hight_screen = 500
width_screen = 800

A_width_Emu = 20
A_hight_Emu = 50
A_Emu_c = blue
A_Emu_HP = 2



B_width_Emu = 20
B_hight_Emu = 50
B_Emu_c = blue
B_Emu_HP = 2
B_x_E = 510
B_y_E = 100

C_width_Emu = 20
C_hight_Emu = 50
C_Emu_c = blue
C_Emu_HP = 2

D_width_Emu = 20
D_hight_Emu = 50
D_Emu_c = blue
D_Emu_HP = 2


EL_x = x_E
EL_y = y_E
EL_v = 0.02




    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False


