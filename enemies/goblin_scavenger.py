from enemies import enemy


class GoblinScavenger(enemy):
    def __init__(self):
        super().__init__(hp=60,attack=15, defense=2, evasion=20)