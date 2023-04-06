import pygame
import random
import sys
from setting import SCREEN_WIDTH, SCREEN_HEIGHT, MAIN_DIR, SCREEN, CLOCK
import os
from tools import transform_image_constant, obj_is_mask
import time

DINO_RUN_IMG = [
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Dinosaur/run1.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Dinosaur/run2.png"))
]
GUN_IMG = [
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/Gun/Gun1.png")), width=50),
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/Gun/Gun2.png")), width=50),
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/Gun/Gun3.png")), width=80),
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/Gun/Gun4.png")), width=80),
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/Gun/Gun5.png")), width=80)
]
BULLET_IMG = [
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Bullet/bullet1.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Bullet/bullet2.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Bullet/bullet3.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Bullet/bullet4.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Bullet/bullet5.png"))
]
HELMET_IMG = [
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/head/Helmet1.png")), width=55),
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/head/Helmet2.png")), width=55),
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/head/Helmet3.png")), width=55)
]
CACTUS_IMG = [
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Cactus/LargeCactus3.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Cactus/SmallCactus3.png"))
]
WYVERN_IMG = [
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Wyvern/wyvern1.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Wyvern/wyvern2.png"))
]
BOSS_IMG = [
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Boss/boss1.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Boss/boss1.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Boss/boss.png")),
    pygame.image.load(os.path.join(MAIN_DIR, "Image/Boss/boss.png"))
]
BOOM_IMG = [
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/explosion/ex1.png")), width=100),
    transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/explosion/ex2.png")), width=100)
]

GUN_ITEM_IMG = transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/Gun/Gun_item.png")), width=50)
HELMET_ITEM_IMG = transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/head/Helmet_item.png")), width=50)
HEALTH_ITEM_IMG = transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/Other/Health_item.png")), width=50)
GAME_OVER_IMG = pygame.image.load(os.path.join(MAIN_DIR, "Image/Other/wasted.png"))
GAME_OVER_WIN_IMG = transform_image_constant(pygame.image.load(os.path.join(MAIN_DIR, "Image/Other/Win.png")), width=400)
RESET_IMG = pygame.image.load(os.path.join(MAIN_DIR, "Image/Other/Reset.png"))
RESET_WIN_IMG = pygame.image.load(os.path.join(MAIN_DIR, "Image/Other/Reset_win.png"))
GROUND_IMG = pygame.image.load(os.path.join(MAIN_DIR, "Image/Other/Ground.png"))

SHOOT_MUSIC = pygame.mixer.Sound(os.path.join(MAIN_DIR, "Music/gun.wav"))
MAIN_THEME_MUSIC = os.path.join(MAIN_DIR, "Music/backgroudMusic.wav")
GAME_OVER_MUSIC = os.path.join(MAIN_DIR, "Music/title.wav")

class Ground:
    def __init__(self):
        self.speed = 5
        self.ground_list = []
        for i in range(SCREEN_WIDTH):
            if random.random() > 0.95:
                img_rect = GROUND_IMG.get_rect()
                img_rect.x = random.randint(0, GROUND_IMG.get_width())
                img_rect.w = random.randint(120, min(300, max(120, GROUND_IMG.get_width() - img_rect.x)))
                draw_pos = [i, random.randint(0, SCREEN_HEIGHT)]
                self.ground_list.append([img_rect, draw_pos])

    def draw(self):
        if random.random() > 0.8:
            img_rect = GROUND_IMG.get_rect()
            img_rect.x = random.randint(0, GROUND_IMG.get_width())
            img_rect.w = random.randint(120, min(300, max(120, GROUND_IMG.get_width()-img_rect.x)))
            draw_pos = [SCREEN_WIDTH, random.randint(0, SCREEN_HEIGHT)]
            self.ground_list.append([img_rect, draw_pos])

        new_ground_list = []
        for g in self.ground_list:
            if g[1][0] < -g[0].w:
                del g
            else:
                g[1][0] -= self.speed
                new_ground_list.append(g)
        self.ground_list = new_ground_list
        for g in self.ground_list:
            SCREEN.blit(GROUND_IMG, (g[1][0], g[1][1]), g[0])

class Item:
    def __init__(self, item_type=0):
        self.x_speed = 3
        self.y_speed = 3
        self.item_type = item_type
        if item_type==0:
            self.img = GUN_ITEM_IMG
        elif item_type==1:
            self.img = HELMET_ITEM_IMG
        else:
            self.img = HEALTH_ITEM_IMG

        self.rect = self.img.get_rect()
        self.mask = pygame.mask.from_surface(self.img.convert_alpha())
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT-self.img.get_height())
        self.direct = random.randint(0, 1)

    def draw(self):
        if random.random() > 0.9:
            self.direct = 1 - self.direct
        if self.direct:
            self.rect.y -= self.y_speed
        else:
            self.rect.y += self.y_speed
        self.rect.y = max(min(self.rect.y, SCREEN_HEIGHT-self.img.get_height()), 0)
        self.rect.x -= self.x_speed
        SCREEN.blit(self.img, self.rect)

class Bullet:
    def __init__(self, bullet_idx, centerx, centery, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.bullet_idx = bullet_idx
        self.img = BULLET_IMG[bullet_idx]
        self.mask = pygame.mask.from_surface(self.img.convert_alpha())
        self.rect = self.img.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

    def draw(self):
        SCREEN.blit(self.img, self.rect)
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

class Explosion:
    def __init__(self, obj):
        self.obj = obj
        self.step = 0
        self.max_step = 20

    def draw(self):
        img = BOOM_IMG[min(self.max_step - 1, self.step)//(self.max_step//2)]
        rect = img.get_rect()
        rect.centerx = self.obj.rect.centerx
        rect.centery = self.obj.rect.centery
        SCREEN.blit(img, rect)
        self.step += 1

class Dinosaur:
    def __init__(self):
        self.move_speed = 8
        self.health = 100
        self.rect = DINO_RUN_IMG[0].get_rect()
        self.rect.x = 88
        self.rect.y = 425 - self.rect.height
        self.mask = pygame.mask.from_surface(DINO_RUN_IMG[0].convert_alpha())
        self.gun_idx = 0
        self.helmet_idx = -1
        self.gun_img = GUN_IMG[self.gun_idx]
        self.gun_rect = self.gun_img.get_rect()
        self.helmet_img = None
        self.helmet_rect = None
        self.update_gun()
        self.step = 0

    def draw(self):
        img = DINO_RUN_IMG[self.step // 10]
        rect = img.get_rect()
        self.rect.w = rect.w
        self.rect.h = rect.h
        self.mask = pygame.mask.from_surface(img.convert_alpha())
        self.update_gun()
        self.update_helmet()

        SCREEN.blit(img, self.rect)
        if self.helmet_idx >= 0:
            SCREEN.blit(self.helmet_img, self.helmet_rect)
        SCREEN.blit(self.gun_img, self.gun_rect)

        # draw health bar
        pygame.draw.rect(SCREEN, (0, 0, 0), (49, 19, 102, 22), 1)
        pygame.draw.rect(SCREEN, (0, 255, 0), (50, 20, self.health, 20), 0)

    def update_health(self, state):
        # state: heal = 0, shot = 1, hit = 2
        if state==0:
            self.health += 20
        elif state==1:
            if self.helmet_idx >= 0:
                self.helmet_idx -= 1
            else:
                self.health -= 1
        else:
            self.health -= 5
        self.health = min(max(0, self.health), 100)

    def update_gun(self):
        self.gun_idx = min(max(0, self.gun_idx), 4)
        self.gun_img = GUN_IMG[self.gun_idx]
        self.gun_rect = self.gun_img.get_rect()
        if self.gun_idx==0 or self.gun_idx==1:
            self.gun_rect = self.gun_img.get_rect()
            self.gun_rect.x = self.rect.x + 50
            self.gun_rect.y = self.rect.y + 15
        else:
            self.gun_rect = self.gun_img.get_rect()
            self.gun_rect.x = self.rect.x + 40
            self.gun_rect.y = self.rect.y + 20

    def update_helmet(self):
        self.helmet_idx = min(max(-1, self.helmet_idx), 2)
        if self.helmet_idx < 0:
            self.helmet_img = None
            self.helmet_rect = None
        else:
            self.helmet_img = HELMET_IMG[self.helmet_idx]
            self.helmet_rect = self.helmet_img.get_rect()
            self.helmet_rect.x = self.rect.x + 35
            self.helmet_rect.y = self.rect.y - 10

    def update(self, keys):
        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.rect.y -= self.move_speed
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.rect.y += self.move_speed
        self.rect.y = min(max(0, self.rect.y), SCREEN_HEIGHT-self.rect.h)

        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.rect.x -= self.move_speed
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.rect.x += self.move_speed
        self.rect.x = min(max(0, self.rect.x), SCREEN_WIDTH-self.rect.w)
        self.step = (self.step + 1) % 20

    def shoot(self):
        SHOOT_MUSIC.play()
        self.update_gun()
        begin_x = self.gun_rect.x + self.gun_rect.w
        begin_y = self.gun_rect.y + self.gun_rect.h // 2 - 5
        bullet_list = []

        if self.gun_idx == 0:
            bullet_list.append(Bullet(0, begin_x, begin_y, speed_x=15, speed_y=0))
            return bullet_list

        bullet_list.append(Bullet(0, begin_x, begin_y-5, speed_x=15, speed_y=0))
        bullet_list.append(Bullet(0, begin_x, begin_y+5, speed_x=15, speed_y=0))
        if self.gun_idx == 1:
            return bullet_list

        delta = 10
        speed_y = 2
        for i in range(2, self.gun_idx+1):
            bullet_list.append(Bullet(1, begin_x, begin_y - delta, speed_x=15, speed_y=-speed_y))
            bullet_list.append(Bullet(1, begin_x, begin_y + delta, speed_x=15, speed_y=speed_y))
            delta += 5
            speed_y += 2
        return bullet_list

class Boss:
    def __init__(self):
        self.health = 200
        self.speed = 2
        self.bullet_speed = 10
        self.direct_x = 1
        self.direct_y = 1
        self.last_shoot_time = 0
        self.img = BOSS_IMG[0]
        self.rect = self.img.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT-self.rect.h)
        self.mask = pygame.mask.from_surface(self.img.convert_alpha())
        self.step = 0

    def update_health(self, state):
        self.health -= 2

    def draw(self):
        if self.health > 100:
            self.img = BOSS_IMG[self.step // 10]
        else:
            self.img = BOSS_IMG[self.step // 10 + 2]
        rect = self.img.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.mask = pygame.mask.from_surface(self.img.convert_alpha())
        self.rect = rect

        # x direction move
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.direct_x = -1
        elif self.rect.x < SCREEN_WIDTH * 2 / 3:
            self.direct_x = 1
        elif random.random() > 0.9:
            self.direct_x = -1 * self.direct_x
        self.rect.x = self.rect.x + self.direct_x * self.speed

        # y direction move
        if self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.direct_y = -1
        elif self.rect.y < self.rect.height // 2:
            self.direct_y = 1
        elif random.random() > 0.95:
            self.direct_y = -1 * self.direct_y
        self.rect.y = self.rect.y + self.direct_y * self.speed

        SCREEN.blit(self.img, self.rect)
        self.step = (self.step + 1) % 20

        # draw health
        pygame.draw.rect(SCREEN, (0, 0, 0), (1299, 19, 102, 22), 1)
        if self.health > 100:
            pygame.draw.rect(SCREEN, (255, 0, 0), (1300, 20, self.health-100, 20), 0)
        else:
            pygame.draw.rect(SCREEN, (255, 0, 0), (1300, 20, self.health, 20), 0)

    def get_bullet(self):
        if self.health > 100:
            bullet_list = [Bullet(3, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=0),
                           Bullet(3, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=-3),
                           Bullet(3, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=3),
                           Bullet(3, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=-6),
                           Bullet(3, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=6)]
        else:
            bullet_list = [Bullet(4, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=0),
                           Bullet(4, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=-3),
                           Bullet(4, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=3),
                           Bullet(4, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=-6),
                           Bullet(4, self.rect.centerx, self.rect.centery, speed_x=-self.bullet_speed, speed_y=6)]

        return bullet_list

    def shoot(self, dino):
        if (time.time() - self.last_shoot_time) > 0.2:
            self.last_shoot_time = time.time()
            return self.get_bullet()
        return []

class Cactus:
    def __init__(self):
        self.speed = 1
        self.health = 100
        self.bullet_speed = 8
        self.last_shoot_time = time.time()
        self.img = random.choice(CACTUS_IMG)
        self.rect = self.img.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(0, 200)
        self.rect.y = random.randint (0, SCREEN_HEIGHT-self.rect.h)
        self.mask = pygame.mask.from_surface(self.img.convert_alpha())

    def update_health(self, state):
        # state: shot = 0, hit = 1
        if state==0:
            self.health -= 10
        else:
            self.health = 0

    def draw(self):
        self.rect.x -= self.speed
        SCREEN.blit(self.img, self.rect)

    def get_bullet(self, dinosaur):
        min_x = dinosaur.rect.x - 50
        max_x = dinosaur.rect.x + dinosaur.rect.w + 50
        dinosaur_target_x = random.random() * (max_x-min_x) + min_x

        min_y = dinosaur.rect.y - 50
        max_y = dinosaur.rect.y + dinosaur.rect.h + 50
        dinosaur_target_y = random.random() * (max_y-min_y) + min_y

        distance_x = abs(dinosaur_target_x-self.rect.centerx)
        distance_y = abs(dinosaur_target_y-self.rect.centery)
        distance = (distance_x**2 + distance_y**2)**0.5
        speed_x = self.bullet_speed * distance_x / distance
        speed_y = self.bullet_speed * distance_y / distance
        if dinosaur_target_x < self.rect.centerx:
            speed_x = -speed_x
        if dinosaur_target_y < self.rect.centery:
            speed_y = -speed_y
        return [Bullet(bullet_idx=3, centerx=self.rect.centerx, centery=self.rect.centery, speed_x=speed_x, speed_y=speed_y)]

    def shoot(self, dinosaur):
        if (time.time() - self.last_shoot_time) > (random.random()+0.1):
            self.last_shoot_time = time.time()
            return self.get_bullet(dinosaur)
        return []

class Wyvern:
    def __init__(self):
        self.health = 60
        self.speed = 2
        self.bullet_speed = 8
        self.direct_x = 1
        self.direct_y = 1
        self.last_shoot_time = 0
        self.shoot_times = 0
        self.img = WYVERN_IMG[0]
        self.rect = self.img.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT-self.rect.h)
        self.mask = pygame.mask.from_surface(self.img.convert_alpha())
        self.step = 0

    def update_health(self, state):
        # state: shot = 0 (health - 10), hit = 1 (die);
        if state == 0:
            self.health -= 20
        else:
            self.health = 0

    def draw(self):
        self.img = WYVERN_IMG[self.step // 10]
        rect = self.img.get_rect()
        rect.x = self.rect.x
        rect.y = self.rect.y
        self.mask = pygame.mask.from_surface(self.img.convert_alpha())
        self.rect = rect

        # x direction move
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.direct_x = -1
        elif self.rect.x < self.rect.width:
            self.direct_x = 1
        elif random.random() > 0.9:
            self.direct_x = -1 * self.direct_x
        self.rect.x = self.rect.x + self.direct_x * self.speed

        # y direction move
        if self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.direct_y = -1
        elif self.rect.y < self.rect.height // 2:
            self.direct_y = 1
        elif random.random() > 0.95:
            self.direct_y = -1 * self.direct_y
        self.rect.y = self.rect.y + self.direct_y * self.speed

        SCREEN.blit(self.img, self.rect)
        self.step = (self.step + 1) % 20

    def get_bullet(self, dinosaur):
        min_x = dinosaur.rect.x - 20
        max_x = dinosaur.rect.x + dinosaur.rect.w + 20
        dinosaur_target_x = random.random() * (max_x-min_x) + min_x

        min_y = dinosaur.rect.y - 20
        max_y = dinosaur.rect.y + dinosaur.rect.h + 20
        dinosaur_target_y = random.random() * (max_y-min_y) + min_y

        distance_x = abs(dinosaur_target_x-self.rect.centerx)
        distance_y = abs(dinosaur_target_y-self.rect.centery)
        distance = (distance_x**2 + distance_y**2)**0.5
        speed_x = self.bullet_speed * distance_x / distance
        speed_y = self.bullet_speed * distance_y / distance
        if dinosaur_target_x < self.rect.centerx:
            speed_x = -speed_x
        if dinosaur_target_y < self.rect.centery:
            speed_y = -speed_y
        return [Bullet(bullet_idx=2, centerx=self.rect.centerx, centery=self.rect.centery, speed_x=speed_x, speed_y=speed_y)]

    def shoot(self, dinosaur):
        if self.shoot_times == 3:
            if (time.time() - self.last_shoot_time) > (0.8 + random.random()):
                self.shoot_times = 1
                self.last_shoot_time = time.time()
                return self.get_bullet(dinosaur)
        else:
            if (time.time() - self.last_shoot_time) > 0.6:
                self.shoot_times += 1
                self.last_shoot_time = time.time()
                return self.get_bullet(dinosaur)
        return []

class Restart:
    def __init__(self):
        self.game_over_img = GAME_OVER_IMG
        self.game_over_win_img = GAME_OVER_WIN_IMG
        self.reset_img = RESET_IMG
        self.reset_win_img = RESET_WIN_IMG
        self.game_over_pos = (
            SCREEN_WIDTH//2-self.game_over_img.get_width()//2,
            SCREEN_HEIGHT//4 - 100
        )
        self.game_win_pos = (
            SCREEN_WIDTH//2-self.game_over_win_img.get_width()//2,
            SCREEN_HEIGHT//4 - 100
        )
        self.reset_pos = (
            SCREEN_WIDTH//2-self.reset_img.get_width()//2,
            SCREEN_HEIGHT//2 + 50
        )
        self.reset_win_pos = (
            SCREEN_WIDTH//2-self.reset_img.get_width()//2,
            SCREEN_HEIGHT//2 + 200
        )
        self.font = pygame.font.SysFont("SimHei", 30)

    def draw(self, cost_time, is_win):
        text1 = self.font.render("Game Duration: %.2f s" % cost_time, True, (0, 0, 0))
        text_rect1 = text1.get_rect()
        text2 = self.font.render("Press Enter to Restart Game", True, (0, 0, 0))
        text_rect2 = text2.get_rect()
        if is_win:
            SCREEN.blit(self.game_over_win_img, self.game_win_pos)
            SCREEN.blit(self.reset_win_img, self.reset_win_pos)
            text_rect1.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
            text_rect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)
        else:
            SCREEN.blit(self.game_over_img, self.game_over_pos)
            SCREEN.blit(self.reset_img, self.reset_pos)
            text_rect1.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 70)
            text_rect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 120)

        SCREEN.blit(text1, text_rect1)
        SCREEN.blit(text2, text_rect2)


class ShootingMain:
    def __init__(self):
        self.item_time = None
        self.ground = None
        self.dinosaur = None
        self.item_list = None
        self.boom_list = None
        self.enemy_list = None
        self.enemy_config = None
        self.last_kill_all_enemy_time = None
        self.bullet_list = None
        self.restart = None
        self.back_ground_music =None
        self.game_over = None
        self.start_time = None
        self.game_over_time = None
        self.start()

    def start(self):
        self.item_time = 0  # time.time()
        self.ground = Ground()
        self.dinosaur = Dinosaur()
        self.item_list = []
        self.boom_list = []
        self.enemy_list = []
        self.enemy_config = [
            {"wyvern": 3, "cactus": 0, "boss": 1},
            {"wyvern": 6, "cactus": 4, "boss": 0},
            {"wyvern": 5, "cactus": 3, "boss": 0},
            {"wyvern": 4, "cactus": 2, "boss": 0},
            {"wyvern": 3, "cactus": 1, "boss": 0}
        ]
        self.last_kill_all_enemy_time = None
        self.bullet_list = []
        self.restart = Restart()
        self.back_ground_music = 0  # no music = 0，in-game music = 1，game_over music = 2
        self.game_over = 0 # in-game = 0, loss = 1, win = 2
        self.start_time = time.time()
        self.game_over_time = None

    def draw(self):
        SCREEN.fill((255, 255, 255))
        if self.game_over:
            self.restart.draw(cost_time=self.game_over_time-self.start_time, is_win=self.game_over==2)
        else:
            self.ground.draw()
            self.dinosaur.draw()
            for item in self.item_list:
                item.draw()
            for bullet in self.bullet_list:
                bullet.draw()
            for e in self.enemy_list:
                e.draw()
            for b in self.boom_list:
                b.draw()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        return
                if event.type == pygame.KEYDOWN:
                    if self.game_over and event.key==pygame.K_RETURN:
                        self.start()
                    elif event.key == pygame.K_SPACE:
                        bullet_list = self.dinosaur.shoot()
                        self.bullet_list.extend(bullet_list)

            if time.time()-self.item_time > 3:
                self.item_time = time.time()
                self.item_list.append(Item(item_type=random.randint(0, 2)))

            # dinosaur moving
            keys = pygame.key.get_pressed()
            self.dinosaur.update(keys)

            # check if got the first aid bag
            new_item_list = []
            for item in self.item_list:
                if item.rect.x > -item.rect.w:
                    if obj_is_mask(self.dinosaur, item):
                        if item.item_type==0:
                            self.dinosaur.gun_idx += 1
                        elif item.item_type==1:
                            self.dinosaur.helmet_idx += 1
                        else:
                            self.dinosaur.update_health(state=0)
                        del item
                    else:
                        new_item_list.append(item)
                else:
                    del item
            self.item_list = new_item_list

            # Spawn Enemy
            if len(self.enemy_list) == 0 and len(self.enemy_config):
                if self.last_kill_all_enemy_time is None:
                    self.last_kill_all_enemy_time = time.time()
                elif self.last_kill_all_enemy_time is not None and (time.time()-self.last_kill_all_enemy_time) > 5:
                    enemy_config = self.enemy_config.pop()
                    for _ in range(enemy_config["wyvern"]):
                        self.enemy_list.append(Wyvern())
                    for _ in range(enemy_config["cactus"]):
                        self.enemy_list.append(Cactus())
                    for _ in range(enemy_config["boss"]):
                        self.enemy_list.append(Boss())
                    self.last_kill_all_enemy_time = None

            # Check enemy alive and hit check
            for e in self.enemy_list:
                if obj_is_mask(self.dinosaur, e):
                    self.dinosaur.update_health(state=2)
                    e.update_health(state=1)
            new_enemy_list = []
            for e in self.enemy_list:
                if e.health > 0:
                    new_enemy_list.append(e)
                else:
                    self.boom_list.append(Explosion(e))
            self.enemy_list = new_enemy_list

            # Enemy shoot
            for e in self.enemy_list:
                b = e.shoot(self.dinosaur)
                self.bullet_list.extend(b)

            # bullet hit check
            new_bullet_list = []
            for bullet in self.bullet_list:
                if bullet.rect.x > SCREEN_WIDTH or bullet.rect.x < -bullet.rect.width:
                    del bullet
                elif bullet.rect.y > SCREEN_HEIGHT or bullet.rect.y < -bullet.rect.height:
                    del bullet
                else:
                    is_del = False
                    if bullet.bullet_idx <= 1:
                        for e in self.enemy_list:
                            if obj_is_mask(bullet, e):
                                e.update_health(state=0)
                                del bullet
                                is_del = True
                                break
                    elif obj_is_mask(bullet, self.dinosaur):
                        self.dinosaur.update_health(state=1)
                        del bullet
                        is_del = True
                    if not is_del:
                        new_bullet_list.append(bullet)
            self.bullet_list = new_bullet_list

            # check if enemy die
            new_enemy_list = []
            for e in self.enemy_list:
                if e.health > 0:
                    new_enemy_list.append(e)
                else:
                    self.boom_list.append(Explosion(e))
            self.enemy_list = new_enemy_list

            # check explode effect
            self.boom_list = [b for b in self.boom_list if b.step <= b.max_step]

            # check if game over
            if len(self.enemy_list) == 0 and len(self.enemy_config) == 0 and self.game_over == 0:
                self.game_over = 2
                self.game_over_time = time.time()
            elif self.dinosaur.health <= 0 and not self.game_over:
                self.game_over = 1
                self.game_over_time = time.time()

            self.draw()
            CLOCK.tick(60)
            pygame.display.update()

            if self.game_over and self.back_ground_music != 2:
                pygame.mixer.music.load(GAME_OVER_MUSIC)
                pygame.mixer.music.play(loops=-1)
                self.back_ground_music = 2
            elif self.back_ground_music == 0:
                self.back_ground_music = 1
                pygame.mixer.music.load(MAIN_THEME_MUSIC)
                pygame.mixer.music.play(loops=-1)

