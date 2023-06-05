import pygame ,sys
from setting import *






#colour code
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

"""defidne radius birds"""
#y x axis on screen
x = 100
y = 100
#size of Emu
width_Emu = 20
hight_Emu = 50
#set mouvement speed
veloci_Emu = 0.03

class Emu(object):
    def __init__(self,x,y,width,height,health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.health = health


pygame.init()
screen = pygame.display.set_mode((width_screen, hight_screen))
clock = pygame.time.Clock()


""" project class"""
class project (object):
    def __int__(self, x_p, y_p, colour_p, radious, direction_p):
        self.x = x_p
        self.y = y_p
        self.radious = radious
        self.colour_p = colour_p
        self.direction_p = direction_p
        self.vel_p = 0.05 * direction_p
    def draw(screen):
        pygame.draw.rect(screen, red, (150, 300, 100, 50))





lazers = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for lazer in lazers :
        if lazer.x < 700 and lazer.x > 0:
            lazer.x += lazer.vel_p
        else:
            lazers.pop(lazers.index(lazer))

    screen.fill("black")
    #Emu
    pygame.draw.rect(screen, blue, (x, y, width_Emu, hight_Emu))
    #speed Emu go down
    y += veloci_Emu


    pygame.display.update()
    clock.tick()

