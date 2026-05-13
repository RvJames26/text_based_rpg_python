from calculations.math import Calculations

class FightMenu:
    def __init__(self, player, enemy):
        self.my_character = player
        self.current_enemy = enemy

    def display_menu(self):
        while True:
            print(f"""
            {self.my_character.__class__.__name__}              VS          {self.current_enemy.__class__.__name__}
            hp={self.my_character.hp}                                        hp={self.current_enemy.hp}""")
            players_choice = input(f"""
            1. Attack""")
            if players_choice == "1":
                calc = Calculations()
                if calc.accuracy(self.current_enemy.evasion):
                    dmg_dealt = calc.damage(self.my_character.attack_power, self.current_enemy.defense)
                    self.current_enemy.hp -= dmg_dealt
                    print(f"Attack Hit, {dmg_dealt} dmg")

                else:
                    print(f"Miss")

                if self.current_enemy.hp <= 0:
                    print(f"The {self.current_enemy.__class__.__name__} is dead")
                    return True

                print(f" The {self.current_enemy.__class__.__name__} attacks")
                if calc.accuracy(self.my_character.evasion):
                    enemy_dmg = calc.damage(self.current_enemy.attack, self.my_character.defense)
                    self.my_character.hp -= enemy_dmg
                    print(f"You took {enemy_dmg} damage")
                else:
                    print("You dodged")

                if self.my_character.hp <= 0:
                    print(f"Game Over")
                    return False
