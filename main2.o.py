import pygame, sys

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
Yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    class Game:
        screen = None
        emu = []
        lazers = []
        lost = False

        def __init__(self, width, height):
            pygame.init()
            self.width = width
            self.height = height
            self.screen = pygame.display.set_mode((width, height))
            self.clock = pygame.time.Clock()
            done = False

            tank = Tank(self, width / 2, height - 20)
            generator = E_placement(self)
            rocket = None

            while not done:
                if len(self.emu) == 0:
                    self.displayText("WINNER")

                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:
                    tank.x -= 2 if tank.x > 20 else 0
                elif pressed[pygame.K_UP]:
                    tank.y -= 2 if tank.y > 20 else 0
                elif pressed[pygame.K_RIGHT]:
                    tank.x += 2 if tank.x < width - 20 else 0
                elif pressed[pygame.K_d]:
                    tank.y += 2 if tank.y < width - 20 else 0

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                        self.lazers.append(Lazer(self, tank.x-2.5, tank.y-20))

                pygame.display.flip()
                self.clock.tick(60)
                self.screen.fill(Yellow)

                for emu in self.emu:
                    emu.draw()
                    emu.Collision(self)
                    if (emu.y > height):
                        self.lost = True
                        self.displayText("Villigers killed.YOU LOSE")

                for lazer in self.lazers:
                    lazer.draw()

                if not self.lost: tank.draw()

        def displayText(self, text):
            pygame.font.init()
            font = pygame.font.SysFont('Arial', 50)
            textsurface = font.render(text, False, (44, 0, 62))
            self.screen.blit(textsurface, (110, 160))


    class Emu:
        def __init__(self, game, x, y, hp,emu_c):
            self.x = x
            self.game = game
            self.y = y
            self.size = 30
            self.Size = 20
            self.HP = hp
            self.Emu_c = emu_c

        def draw(self):
            #pygame.draw.rect(self.game.screen,self.Emu_c,pygame.Rect(self.x, self.y, self.Size, self.size))
            emu_image = pygame.image.load("images/birdy.png")
            self.game.screen.blit(emu_image, (self.x, self.y))
            self.y += 0.13

        def Collision(self, game):
            for lazer in game.lazers:
                if (lazer.x < self.x + self.Size and lazer.x > self.x - self.Size and
                        lazer.y < self.y + self.size and lazer.y > self.y - self.size):
                    game.lazers.remove(lazer)
                    self.HP -= 1

                    if self.HP < 3 and self.HP >1:
                        self.Emu_c = green

                    elif self.HP < 2 and self.HP > 0:
                        self.Emu_c = red

                    elif self.HP == 0:
                        game.emu.remove(self)



    class Tank:
        def __init__(self, game, x, y):
            self.x = x
            self.game = game
            self.y = y

        def draw(self):
            #pygame.draw.rect(self.game.screen, green, pygame.Rect(self.x-25, self.y-20, 50, 20))
            tank_image = pygame.image.load("images/tank.2")
            self.game.screen.blit(tank_image, (self.x-10, self.y-30))

    class E_placement:
        def __init__(self, game):
            side_dist = 10
            width = 70
            for x in range(side_dist, game.width - side_dist, width):
                for y in range(side_dist, int(game.height / 2), width):
                    game.emu.append(Emu(game, x, y, 3,blue))



    class Lazer:
        def __init__(self, game, x, y):
            self.x = x
            self.y = y
            self.game = game

        def draw(self):
            pygame.draw.rect(self.game.screen,red,pygame.Rect(self.x+14, self.y-7, 3, 7))
            self.y -= 2

    print()



    if __name__ == '__main__':
        game = Game(600, 400)

    pygame.display.update()
    clock.tick()
    pygame.quit()

