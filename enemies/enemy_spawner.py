import  random
from enemies.cave_slime import CaveSlime
from enemies.goblin_scavenger import GoblinScavenger
from enemies.armored_sentinel import ArmoredSentinel
from enemies.void_knight import VoidKnight

class EnemySpawner:
    def spawn_random_enemies(self):
        enemy_chance = random.randint(1, 10)

        if enemy_chance <= 4:
            return CaveSlime()
        if enemy_chance <= 7:
            return GoblinScavenger()
        if enemy_chance <=9:
            return ArmoredSentinel()
        else:
            return VoidKnight()