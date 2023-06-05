import pygame, sys
from setting import *

pygame.init()
screen = pygame.display.set_mode((width_screen, hight_screen))
pygame.display.set_caption("Emu wars")
clock = pygame.time.Clock()

# backwrond of the game

bg = pygame.image.load("img/bg.png")

def backround ():
    screen.blit(bg, (0, 0))


while True:
    backround()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")

    pygame.display.update()
    clock.tick()


