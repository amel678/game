import pygame ,sys
from setting import *


pygame.init()
screen = pygame.display.set_mode((width_screen,hight_screen))
clock = pygame.time.Clock()

class Emu(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")

    pygame.display.update()
    clock.tick()

