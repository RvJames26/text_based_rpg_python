from character.swordmaster import SwordMaster
from character.shadow import Shadow

class CharacterSelection:

    def __init__(self):
        self.player_choice = None

    def pick_class(self):
        while True:
            player_choice = input("""
            1. SwordMaster
            Max HP: 150
            Attack Power: 14
            Defense: 8 
            Evasion Chance: 5% 
            Critical Hit Chance: 10%
            Special Ability:Bulwark Stance

            2. Shadow
            Max HP: 80
            Attack Power: 18
            Defense: 3
            Evasion Chance: 35%
            Critical Hit Chance: 25%
            Special Ability:Shadow Strike

            Pick a character: """)

            if player_choice == '1':
                self.player_choice = SwordMaster()
                break
            if player_choice == '2':
                self.player_choice = Shadow()
                break
            else:
                print('Please enter a valid option')
                continue

        return self.player_choice
