from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):

    def __init__(self, name: str, position: tuple):
        # Inherits the Entity parameters for making the configuration less complex when setting movement
        super().__init__(name, position)

    def move(self, ):
        # Movement configured as in parallax
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass