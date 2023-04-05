import pygame
import sys
from setting import SCREEN_WIDTH, SCREEN_HEIGHT, MAIN_DIR, SCREEN, CLOCK

class instruction:
    def __init__(self):
        font1 = pygame.font.SysFont("SimHei Bold", 40)
        font2 = pygame.font.SysFont("SimHei", 28)
        SCREEN.fill((255, 255, 255))
        self.text1 = font1.render("Dinosaur Running:", True, (0, 0, 0))
        self.text2 = font2.render("Press SPACE or UP to Jump", True, (0, 0, 0))
        self.text3 = font2.render("Press DOWN to Crawl", True, (0, 0, 0))

        self.text4 = font1.render("Dinosaur Shooting", True, (0, 0, 0))
        self.text5 = font2.render("Use UP, DOWN, LEFT, RIGHT to Move Character", True, (0, 0, 0))
        self.text6 = font2.render("Press SPACE to Shoot", True, (0, 0, 0))
        self.text7 = font2.render("Pickup GUN Item to Upgrade Weapon", True, (0, 0, 0))
        self.text8 = font2.render("Pickup Helmet Item to Upgrade EQUIPMENT", True, (0, 0, 0))

        self.text9 = font1.render("Press ESC to Return", True, (0, 0, 0))

        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 - 100)
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 - 60)
        self.text_rect3 = self.text3.get_rect()
        self.text_rect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 - 20)

        self.text_rect4 = self.text4.get_rect()
        self.text_rect4.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 80)
        self.text_rect5 = self.text5.get_rect()
        self.text_rect5.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 120)
        self.text_rect6 = self.text6.get_rect()
        self.text_rect6.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 160)
        self.text_rect7 = self.text7.get_rect()
        self.text_rect7.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 200)
        self.text_rect8 = self.text8.get_rect()
        self.text_rect8.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 240)

        self.text_rect9 = self.text9.get_rect()
        self.text_rect9.bottomleft = (50, SCREEN_HEIGHT - 50)

    def draw(self):
        SCREEN.blit(self.text1, self.text_rect1)
        SCREEN.blit(self.text2, self.text_rect2)
        SCREEN.blit(self.text3, self.text_rect3)
        SCREEN.blit(self.text4, self.text_rect4)
        SCREEN.blit(self.text5, self.text_rect5)
        SCREEN.blit(self.text6, self.text_rect6)
        SCREEN.blit(self.text7, self.text_rect7)
        SCREEN.blit(self.text8, self.text_rect8)
        SCREEN.blit(self.text9, self.text_rect9)

    def main_loop(self):
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        return

            CLOCK.tick(30)
            pygame.display.update()
