import random
from enemies.cave_slime import CaveSlime
from enemies.goblin_scavenger import GoblinScavenger
from enemies.armored_sentinel import ArmoredSentinel
from enemies.void_knight import VoidKnight

ENEMY_TYPES = (
    CaveSlime, CaveSlime, CaveSlime, CaveSlime,
    GoblinScavenger, GoblinScavenger, GoblinScavenger,
    ArmoredSentinel, ArmoredSentinel, VoidKnight,
)

class EnemySpawner:
    def spawn_random_enemies(self):
        roll = random.randint(1, 10)
        return ENEMY_TYPES[roll - 1]()
