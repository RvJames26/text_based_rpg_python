from character import Character

class SwordMaster(Character):
    def __init__(self):
        super().__init__(hp=150, attack_power=14, defense=8, evasion=5)

        self.critical_hit = 10
        self.special_ability = "Bulwark Stance"