from enemies.enemy import Enemy


class CaveSlime(Enemy):
    def __init__(self):
        super().__init__(hp=40, attack=8, defense=0, evasion=0)