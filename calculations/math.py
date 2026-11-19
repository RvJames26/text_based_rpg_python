import random

class Calculations:
    @staticmethod
    def accuracy(evasion_stat):
        return random.randint(1, 100) > evasion_stat

    @staticmethod
    def damage(attack_power, defense):
        return max(0, attack_power - defense)
