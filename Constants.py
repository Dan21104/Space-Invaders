import pygame as pg
import os

import pygame.image

GAME_ICON = pygame.image.load('Images/spaceShips_007.png')
WIDTH, HEIGHT = 800, 1000
SCREEN_OFFSET = 75
SPACE = (0, 0, 0)
BULLET_COLOR = (255, 255, 255)
FPS = 144
VEL = 4
BULLET_VEL = 4
BULLET_WIDTH = 5
BULLET_HEIGHT = 12
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 80, 60
SPACESHIP_IMAGE = pg.image.load(os.path.join('Images', 'spaceShips_007.png'))
SPACESHIP = pg.transform.rotate(pg.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)
