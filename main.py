import pygame
import sys
import os
from setting import SCREEN_HEIGHT, SCREEN_WIDTH, MAIN_DIR, SCREEN, CLOCK
from DinosaurRunning.RunningMain import RunningMain
from DinosaurShooting.ShootingMain import ShootingMain
from instruction import instruction

pygame.display.set_caption("Dinosaur Adventure")
DINOSAUR_JUMP_IMG = pygame.image.load(os.path.join(MAIN_DIR, "Image/Dinosaur/jump.png"))
DINOSAUR_JUMP_SMALL_IMG = pygame.transform.scale(DINOSAUR_JUMP_IMG, (DINOSAUR_JUMP_IMG.get_width()//3, DINOSAUR_JUMP_IMG.get_height()//3))
GROUND_IMG= pygame.image.load(os.path.join(MAIN_DIR, "Image/Other/Track.png"))

GAME_ITEMS = ["Dinosaur Running", "Dinosaur Shooting", "Instructions"]

class Menu:
    def __init__(self):
        self.start = 0
        self.start_finish = 0

        self.font = pygame.font.SysFont("SimHei", 30)
        self.text = self.font.render("Press ENTER to Start", True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)

        self.dinosaur_rect = DINOSAUR_JUMP_IMG.get_rect()
        self.dinosaur_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)
        self.jump_speed = 8.5

        self.font_item = pygame.font.SysFont("microsoftyahei", 25)
        self.game_texts = [self.font_item.render(t, True, (0, 0, 0)) for t in GAME_ITEMS]
        self.game_text_rects = [t.get_rect() for t in self.game_texts]
        for i in range(len(self.game_text_rects)):
            self.game_text_rects[i].x = SCREEN_WIDTH // 2.3
            self.game_text_rects[i].y = SCREEN_HEIGHT // 2 + i * 50 - 15

        self.selected = 1
        self.dinosaur_item_rect = DINOSAUR_JUMP_SMALL_IMG.get_rect()
        self.update_dinosaur_item_rect()




    def draw(self):
        SCREEN.fill((255, 255, 255))
        SCREEN.blit(self.text, self.text_rect)
        for i in range(len(self.game_texts)):
            SCREEN.blit(self.game_texts[i], self.game_text_rects[i])
        SCREEN.blit(GROUND_IMG, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 - 180), (0, 0, 120, 70))
        SCREEN.blit(DINOSAUR_JUMP_SMALL_IMG, self.dinosaur_item_rect)

        if self.start != 0:
            self.dinosaur_rect.centery -= self.jump_speed * 2
            self.jump_speed -= 0.8
            if self.jump_speed < -8.5:
                self.jump_speed = 8.5
                self.start = 0
                self.start_finish = 1
                self.dinosaur_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)
        SCREEN.blit(DINOSAUR_JUMP_IMG, self.dinosaur_rect)

    def menu_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.start = 1
                    elif event.key == pygame.K_DOWN and not self.start:
                        self.selected = 1 if self.selected == 3 else self.selected + 1
                        self.update_dinosaur_item_rect()
                    elif event.key == pygame.K_UP and not self.start:
                        self.selected = 3 if self.selected == 1 else self.selected - 1
                        self.update_dinosaur_item_rect()

            if self.start_finish:
                self.start = 0
                self.start_finish = 0
                if self.selected == 1:
                    main = RunningMain()
                elif self.selected == 2:
                    main = ShootingMain()
                elif self.selected == 3:
                    main = instruction()
                main.main_loop()

            self.draw()
            CLOCK.tick(30)
            pygame.display.update()

    def update_dinosaur_item_rect(self):
        self.dinosaur_item_rect.center = (SCREEN_WIDTH // 2.45, SCREEN_HEIGHT // 2 + 50 * (self.selected-1))

if __name__ == "__main__":
    menu = Menu()
    menu.menu_loop()
