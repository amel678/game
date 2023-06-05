import pygame
from pygame.locals import *

clock = pygame.time.Clock()
fps = 60

green = (0, 255, 0)


hight_screen = 500
width_screen = 800
width = 60
hight = 30
x = 400
y = 400

class tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen,
                         green,
                         pygame.rect(self.x, self.y, width, hight))
        self.y += 1






Tank = tank(400, 400)


pygame.init()
screen = pygame.display.set_mode((width_screen, hight_screen))



run = True
while run:

    Tank.draw()


    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



pygame.quit()

