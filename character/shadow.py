from character.character import Character

class Shadow(Character):
    def __init__(self):
        super().__init__(hp=80, attack_power=18, defense=3, evasion=35)

        self.critical_hit = 25
        self.special_ability = "Shadow Strike"