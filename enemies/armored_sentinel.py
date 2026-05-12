
from enemies.enemy import Enemy


class ArmoredSentinel(Enemy):
    def __init__(self):
        super().__init__(hp=100, attack=12, defense=10, evasion=0)