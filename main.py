import sys
import pygame

pygame.init()

class Character:
    def __init__(self) -> None:
        self.movement = [False, False]

class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Platformer")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.player = Character()

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

Game().run()