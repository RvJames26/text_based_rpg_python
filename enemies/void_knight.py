
from enemies.enemy import Enemy


class VoidKnight(Enemy):
    def __init__(self):
        super().__init__(hp=250,attack=20, defense=5, evasion=0)