import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, C_GREEN
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window, name, game_mode):
        # Configuration for the first level, background image and player as an entity, enemy spawn time and list of entities
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)


    def run(self):
        # Sets soundtrack and volume
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            # Loop for the enemy event, quitting and shooting
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                # Shows player health and score
                if ent.name == 'Player1':
                    self.level_text(14, f'Player - Health:{ent.health} | Score:{ent.score}', C_GREEN, (10, 25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice (('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # Printed messages
            self.level_text(14, f'{self.name}', C_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    #Specific text characteristics
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)