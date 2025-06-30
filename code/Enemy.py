from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        # Entity parameters and shot delay for the enemies
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        # Enemy movement configuration
        self.rect.centerx -= ENTITY_SPEED[self.name]


    def shoot(self):
        # Enemy shooting configuration
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))