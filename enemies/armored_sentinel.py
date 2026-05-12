from enemies import enemy


class ArmoredSentinel(enemy):
    def __init__(self):
        super().__init__(hp=100, attack=12, defense=10, evasion=0)