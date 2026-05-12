import random

class Calculations:
    def __init__(self):
        pass

    def accuracy(self, evasion_stat):
        roll = random.randint(1, 100)

        if roll > evasion_stat:
            return True
        else:
            return False

    def damage(self, attack_power, defense_def):
        total_dmg = max(0, attack_power - defense_def)
        return total_dmg