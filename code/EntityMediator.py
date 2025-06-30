from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    # Verifies if the entities are colliding with the windows limits, if so they are eliminated
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    # Verifies if the entities are colling between themselves, if so, sets the variable valid_interaction as true
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
           valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
           valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        # Sets the damage to the entities that collided and the name of the one that done the damage to the variable last damage to be used for the score
        if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    # Adds the score for the Player if it dealt the last damage to the enemies
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score


    @staticmethod
    # Establishes the ent1 and ent2 in the entities present in the level for the collisions configuration
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    # Verifies the entities health and uses the give_score method when the health is lower than zero
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)