import pygame


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
Yellow = (255, 255, 0)

width = 60
hight = 30
x = 400
y = 400

class Game:
    screen = None
    Emu = []
    rokets = []
    lost = None

    def __int__(self, width, hight):
        pygame.init()
        self.width = width
        self.hight = hight
        self.screen = pygame.display.set_mode((hight,width))
        self.clock = pygame.time.Clock()
        end = False

        while not end :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True

        pygame.display.flip()
        self.clock.tick(60)
        self.screen.fill(Yellow)

class Alien:
    def __init__(self,game, x, y):
            self.game = game
            self.x = x
            self.y = y

    def draw(self):
            pygame.draw.rect(self.game.screen,
                            green,
                            pygame.Rect(self.x, self.y, width, hight))
            self.y += 0.05

alien = Alien(30, 30)
alien.draw()


