import pygame ,sys
from setting import *

#colour code
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
    def draw():
    pygame.draw.rect(screen, green, (300, 400, 60, 30))



pygame.init()
screen = pygame.display.set_mode((width_screen, hight_screen))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #tank movemnet
    tank = player(300, 400, 60, 30)
    key_move = pygame.key.get_pressed()
    if key_move[pygame.K_LEFT] and tank.x > tank.vel:
        tank.x -= tank.vel
    if key_move[pygame.K_RIGHT] and tank.y < 800 - tank.vel - tank.width:
        tank.x += tank.vel
    if key_move[pygame.K_UP] and tank.x > tank.vel:
        tank.y -= tank.vel
    if key_move[pygame.K_DOWN] and tank.y < 500 - tank.height - tank.vel:
        tank.y += tank.vel
    player.draw()




    pygame.display.update()
    screen.fill("black")
    clock.tick()

