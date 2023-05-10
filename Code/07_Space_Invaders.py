import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

BACKGROUND_COLOR = (0, 0, 0)
BULLET_COLOR = (255, 255, 255)
BULLET_SIZE = 5
SHIP_WIDTH = 15

shipA_x = SCREEN_WIDTH / 2
shipA_y = SCREEN_HEIGHT - 70
bullet_x = shipA_x
bullet1_x = shipA_x
bullet2_x = shipA_x
bullet3_x = shipA_x
bullet4_x = shipA_x
bullet5_x = shipA_x
bullet6_x = shipA_x
bullet7_x = shipA_x
bullet8_x = shipA_x
bullet9_x = shipA_x
bullet10_x = shipA_x
bullet_y = shipA_y + 15
bullet1_y = shipA_y + 15
bullet2_y = shipA_y + 15
bullet3_y = shipA_y + 15
bullet4_y = shipA_y + 15
bullet5_y = shipA_y + 15
bullet6_y = shipA_y + 15
bullet7_y = shipA_y + 15
bullet8_y = shipA_y + 15
bullet9_y = shipA_y + 15
bullet10_y = shipA_y + 15
bullet_vy = 2.5
bullet_dy = -1
speed_indicator = 2
gap = 50
step = 3.5

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()

ship_A = pygame.image.load('Default/ship_A.png')


def game_input():
    global shipA_x, shipA_y, step
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_ESCAPE]:
        exit()
    elif key_input[pygame.K_LEFT]:
        shipA_x -= step
    elif key_input[pygame.K_RIGHT]:
        shipA_x += step
    pygame.display.update()


def game_update():
    global shipA_x, bullet_y, bullet1_y, bullet2_y, bullet3_y, bullet4_y, bullet5_y, bullet6_y, bullet7_y, bullet8_y,\
        bullet9_y, bullet10_y
    if shipA_x < SHIP_WIDTH:
        shipA_x = SHIP_WIDTH
    if shipA_x > SCREEN_WIDTH - SHIP_WIDTH:
        shipA_x = SCREEN_WIDTH - SHIP_WIDTH
    if bullet_y < 0:
        bullet_y = shipA_y + 15
    if bullet1_y < 0:
        bullet1_y = shipA_y + 15
    if bullet2_y < 0:
        bullet2_y = shipA_y + 15
    if bullet3_y < 0:
        bullet3_y = shipA_y + 15
    if bullet4_y < 0:
        bullet4_y = shipA_y + 15
    if bullet5_y < 0:
        bullet5_y = shipA_y + 15
    if bullet6_y < 0:
        bullet6_y = shipA_y + 15
    if bullet7_y < 0:
        bullet7_y = shipA_y + 15
    if bullet8_y < 0:
        bullet8_y = shipA_y + 15
    if bullet9_y < 0:
        bullet9_y = shipA_y + 15
    if bullet10_y < 0:
        bullet10_y = shipA_y + 15
    bullet_y += speed_indicator * bullet_vy * bullet_dy


def game_output():
    global bullet_y, bullet1_y, bullet2_y, bullet3_y, bullet4_y, bullet5_y, bullet6_y, bullet7_y,\
        bullet8_y, bullet9_y, bullet10_y
    window.fill(BACKGROUND_COLOR)
    pygame.draw.circle(window, BULLET_COLOR, (bullet_x, bullet_y), BULLET_SIZE)
    if bullet_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet1_x, bullet1_y), BULLET_SIZE)
        bullet1_y += speed_indicator * bullet_vy * bullet_dy
    if bullet1_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet2_x, bullet2_y), BULLET_SIZE)
        bullet2_y += speed_indicator * bullet_vy * bullet_dy
    if bullet2_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet3_x, bullet3_y), BULLET_SIZE)
        bullet3_y += speed_indicator * bullet_vy * bullet_dy
    if bullet3_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet4_x, bullet4_y), BULLET_SIZE)
        bullet4_y += speed_indicator * bullet_vy * bullet_dy
    if bullet4_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet5_x, bullet5_y), BULLET_SIZE)
        bullet5_y += speed_indicator * bullet_vy * bullet_dy
    if bullet5_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet6_x, bullet6_y), BULLET_SIZE)
        bullet6_y += speed_indicator * bullet_vy * bullet_dy
    if bullet6_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet7_x, bullet7_y), BULLET_SIZE)
        bullet7_y += speed_indicator * bullet_vy * bullet_dy
    if bullet7_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet8_x, bullet8_y), BULLET_SIZE)
        bullet8_y += speed_indicator * bullet_vy * bullet_dy
    if bullet8_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet9_x, bullet9_y), BULLET_SIZE)
        bullet9_y += speed_indicator * bullet_vy * bullet_dy
    if bullet9_y < shipA_y - gap:
        pygame.draw.circle(window, BULLET_COLOR, (bullet10_x, bullet10_y), BULLET_SIZE)
        bullet10_y += speed_indicator * bullet_vy * bullet_dy
    window.blit(ship_A, (shipA_x - 32, shipA_y))
    pygame.display.flip()


while True:
    game_input()
    game_update()
    game_output()
    clock.tick(144)
