from enemies import enemy


class VoidKnight(enemy):
    def __init__(self):
        super().__init__(hp=250,attack=20, defense=5, evasion=0)