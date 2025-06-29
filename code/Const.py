# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'Player1': 300,
    'Player1Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Enemy1': 100,
    'Enemy2': 200
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 4,
    'Player1Shot': 1,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}


# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_SHOT = {
    'Player1': pygame.K_SPACE,
}


# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324