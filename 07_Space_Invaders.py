import pygame
import pygame as pg
import random
pygame.init()

WIDTH, HEIGHT = 800, 1000
SCREEN_OFFSET = 75
SPACE = (0, 0, 0)
BULLET_COLOR = (255, 255, 255)
FPS = 144
VEL = 3
ENEMY_VEL = 0.5
UPGRADE_VEL = 0.5
BULLET_VEL = 4
BULLET_WIDTH = 5
BULLET_HEIGHT = 12
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 64, 64

ship_A = pg.image.load("Images/00/ship_A.png")
ship_B = pg.image.load("Images/00/ship_B.png")
ship_C = pg.image.load("Images/00/ship_C.png")
ship_D = pg.image.load("Images/00/ship_D.png")
ship_E = pg.image.load("Images/00/ship_E.png")
ship_F = pg.image.load("Images/00/ship_F.png")
ship_G = pg.image.load("Images/00/ship_G.png")
ship_H = pg.image.load("Images/00/ship_H.png")
ship_I = pg.image.load("Images/00/ship_I.png")
ship_J = pg.image.load("Images/00/ship_J.png")
ship_K = pg.image.load("Images/00/ship_K.png")
ship_L = pg.image.load("Images/00/ship_L.png")

enemy_A = pg.transform.rotate(pg.image.load("Images/00/enemy_A.png"), 180)
enemy_B = pg.transform.rotate(pg.image.load("Images/00/enemy_B.png"), 180)
enemy_C = pg.transform.rotate(pg.image.load("Images/00/enemy_C.png"), 180)
enemy_D = pg.transform.rotate(pg.image.load("Images/00/enemy_D.png"), 180)
enemy_E = pg.transform.rotate(pg.image.load("Images/00/enemy_E.png"), 180)

SPACESHIP = ship_A
ENEMY = enemy_A
UPGRADE = pg.image.load("Images/00/icon_plusSmall.png")

score = 0
score_increment = 1
score_a = 300
ally_upgrade = 0
enemy_upgrade = 0
clock = pg.time.Clock()
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Space Invaders')
game_running = True
shooting_delay = 1000
spawning_delay = 3000
spawning_upgrade_delay = 25000
ally_shot_dmg = 1
space_ship_hp = 3
enemy_dmg = 1
enemy_hp = 2
ally_shot_event = pg.USEREVENT + 1
spawn_enemy = pg.USEREVENT + 2
spawn_upgrade = pg.USEREVENT + 3
pg.time.set_timer(ally_shot_event, shooting_delay)
pg.time.set_timer(spawn_enemy, spawning_delay)
pg.time.set_timer(spawn_upgrade, spawning_upgrade_delay)

font_obj = pygame.font.Font(None, 32)
score_Surface = font_obj.render(str(score), True, (97, 222, 42), None)
score_Rect = score_Surface.get_rect()
score_Rect.center = (400, 30)

hp_Surface = font_obj.render(str(space_ship_hp), True, (136, 8, 8), None)
hp_Rect = score_Surface.get_rect()
hp_Rect.center = (750, 30)

dmg_Surface = font_obj.render("Ally damage: " + str(ally_shot_dmg), True, (0, 0, 128), None)
dmg_Rect = score_Surface.get_rect()
dmg_Rect.center = (610, 30)

enemy_hp_Surface = font_obj.render(str(enemy_hp), True, (136, 8, 8), None)
enemy_hp_Rect = score_Surface.get_rect()
enemy_hp_Rect.center = (100, 30)

enemy_dmg_Surface = font_obj.render("Enemy damage: " + str(enemy_dmg), True, (0, 0, 128), None)
enemy_dmg_Rect = score_Surface.get_rect()
enemy_dmg_Rect.center = (50, 30)

bullets = []
enemies = []
upgrades = []
dangers = []


def on_key_down(event):
    global space_ship_vel, bullets
    if event.key == pg.K_d or event.key == pg.K_RIGHT and space_ship.x < WIDTH - SPACESHIP_WIDTH - SCREEN_OFFSET:
        space_ship_vel = 1
    elif event.key == pg.K_a or event.key == pg.K_LEFT and space_ship.x > SCREEN_OFFSET:
        space_ship_vel = -1


def on_key_up(event):
    global space_ship_vel
    if event.key == pg.K_d or event.key == pg.K_RIGHT and space_ship_vel == 1:
        space_ship_vel = 0
    elif event.key == pg.K_a or event.key == pg.K_LEFT and space_ship_vel == -1:
        space_ship_vel = 0


def game_input():
    global game_running
    key_input = pygame.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or key_input[pygame.K_ESCAPE]:
            game_running = False
        elif event.type == pg.KEYDOWN:
            on_key_down(event)
        elif event.type == pg.KEYUP:
            on_key_up(event)
        if event.type == ally_shot_event:
            bullet = pygame.Rect(space_ship.x + SPACESHIP_WIDTH // 2 - BULLET_WIDTH // 2,
                                 space_ship.y + SPACESHIP_HEIGHT // 3, BULLET_WIDTH, BULLET_HEIGHT)
            bullets.append(bullet)
        if event.type == spawn_enemy:
            enemy = pg.Rect(random.randint(SCREEN_OFFSET, WIDTH - SPACESHIP_WIDTH - SCREEN_OFFSET), 0,
                            SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
            enemies.append(enemy)
        if event.type == spawn_upgrade:
            upgrade = pg.Rect(random.randint(SCREEN_OFFSET, WIDTH - SPACESHIP_WIDTH - SCREEN_OFFSET), 0,
                              SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
            upgrades.append(upgrade)


def game_update():
    global space_ship_vel, space_ship_hp, score, score_Surface, score_Rect, score_a, ally_upgrade, SPACESHIP,\
        enemy_upgrade, ENEMY, hp_Rect, hp_Surface, dmg_Rect, dmg_Surface, ally_shot_dmg, spawning_upgrade_delay,\
        enemy_hp, enemy_dmg, enemy_dmg_Rect, enemy_dmg_Surface, enemy_hp_Surface, enemy_hp_Rect, shooting_delay, \
        spawning_delay

    space_ship.x = space_ship.x + space_ship_vel * VEL
    if score == 2500:
        enemy_upgrade = 1
    if score == 7000:
        enemy_upgrade = 2
    if score == 15000:
        enemy_upgrade = 3
    if score == 30000:
        enemy_upgrade = 4
    if space_ship.x > (WIDTH - SPACESHIP_WIDTH + 10) or space_ship.x + 10 < 0:
        space_ship_vel = 0
    for bullet in bullets:
        bullet.y -= BULLET_VEL
        if bullet.collidelist(enemies) >= 0:
            enemy_hp -= ally_shot_dmg
            bullets.remove(bullet)
            if enemy_hp <= 0:
                if enemy_upgrade == 0:
                    enemy_hp = 2
                    enemy_dmg = 1
                elif enemy_upgrade == 1:
                    enemy_hp = 6
                    enemy_dmg = 3
                elif enemy_upgrade == 2:
                    enemy_hp = 10
                    enemy_dmg = 6
                elif enemy_upgrade == 3:
                    enemy_hp = 25
                    enemy_dmg = 15
                elif enemy_upgrade == 4:
                    enemy_hp = 40
                    enemy_dmg = 25
                enemies.pop(bullet.collidelist(enemies))
    for enemy in enemies:
        enemy.y += ENEMY_VEL
        if enemy.colliderect(space_ship):
            space_ship_hp -= enemy_dmg
            enemies.remove(enemy)
    for upgrade in upgrades:
        if upgrade.colliderect(space_ship):
            ally_upgrade += 1
            upgrades.remove(upgrade)
    for upgrade in upgrades:
        upgrade.y += UPGRADE_VEL
    score_Surface = font_obj.render(str(score // score_a), True, (97, 222, 42), None)
    score_Rect = score_Surface.get_rect()
    score_Rect.center = (400, 30)
    hp_Surface = font_obj.render("Ally hp: " + str(space_ship_hp), True, (136, 8, 8), None)
    hp_Rect = score_Surface.get_rect()
    hp_Rect.center = (610, 60)
    dmg_Surface = font_obj.render("Ally damage: " + str(ally_shot_dmg), True, (0, 0, 128), None)
    dmg_Rect = score_Surface.get_rect()
    dmg_Rect.center = (610, 30)
    enemy_hp_Surface = font_obj.render("Enemy hp: " + str(enemy_hp), True, (136, 8, 8), None)
    enemy_hp_Rect = score_Surface.get_rect()
    enemy_hp_Rect.center = (50, 60)
    enemy_dmg_Surface = font_obj.render("Enemy damage: " + str(enemy_dmg), True, (0, 0, 128), None)
    enemy_dmg_Rect = score_Surface.get_rect()
    enemy_dmg_Rect.center = (50, 30)
    if ally_upgrade == 1:
        SPACESHIP = ship_B
        space_ship_hp = 6
        ally_shot_dmg = 2
    if ally_upgrade == 2:
        SPACESHIP = ship_C
        space_ship_hp = 10
        ally_shot_dmg = 5
    if ally_upgrade == 3:
        SPACESHIP = ship_D
        space_ship_hp = 15
        ally_shot_dmg = 8
    if ally_upgrade == 4:
        SPACESHIP = ship_E
        space_ship_hp = 20
        ally_shot_dmg = 10
    if ally_upgrade == 5:
        SPACESHIP = ship_F
        space_ship_hp = 25
        ally_shot_dmg = 12
    if ally_upgrade == 6:
        SPACESHIP = ship_G
        space_ship_hp = 26
        ally_shot_dmg = 13
    if ally_upgrade == 7:
        SPACESHIP = ship_H
        space_ship_hp = 27
        ally_shot_dmg = 14
    if ally_upgrade == 8:
        SPACESHIP = ship_I
        space_ship_hp = 28
        ally_shot_dmg = 15
    if ally_upgrade == 9:
        SPACESHIP = ship_J
        space_ship_hp = 29
        ally_shot_dmg = 16
    if ally_upgrade == 10:
        SPACESHIP = ship_K
        space_ship_hp = 30
        ally_shot_dmg = 17
    if ally_upgrade == 11:
        SPACESHIP = ship_L
        space_ship_hp = 50
        ally_shot_dmg = 25
    if enemy_upgrade == 1:
        ENEMY = enemy_B
    if enemy_upgrade == 2:
        ENEMY = enemy_C
    if enemy_upgrade == 3:
        ENEMY = enemy_D
    if enemy_upgrade == 4:
        ENEMY = enemy_E
    if space_ship_hp == 0:
        exit()
    score += score_increment


def game_output():
    window.fill(SPACE)
    window.blit(SPACESHIP, (space_ship.x, space_ship.y))
    window.blit(score_Surface, score_Rect)
    window.blit(hp_Surface, hp_Rect)
    window.blit(dmg_Surface, dmg_Rect)
    window.blit(enemy_hp_Surface, enemy_hp_Rect)
    window.blit(enemy_dmg_Surface, enemy_dmg_Rect)
    for bullet in bullets:
        pygame.draw.rect(window, BULLET_COLOR, bullet)
    for enemy in enemies:
        window.blit(ENEMY, enemy)
    if ally_upgrade < 11:
        for upgrade in upgrades:
            window.blit(UPGRADE, upgrade)
    pg.display.flip()


space_ship = pygame.Rect((WIDTH - SPACESHIP_WIDTH) // 2, HEIGHT - HEIGHT // 8,
                         SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

space_ship_vel = 0
while game_running:
    clock.tick(FPS)
    game_input()
    game_update()
    game_output()
