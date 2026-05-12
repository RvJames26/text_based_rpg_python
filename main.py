from calculations.math import Calculations
from character.pick_character import CharacterSelection
from main_menu.menu import Start
from enemies.enemy_spawner import EnemySpawner

my_game = Start("start")
my_game.run_menu()

character_selection = CharacterSelection()
my_character = character_selection.pick_class()

spawner = EnemySpawner()
current_enemy = spawner.spawn_random_enemies()

print(f"A {current_enemy.__class__.__name__} appeared")

# calc = Calculations()
# if calc.accuracy(current_enemy.evasion):
#     dmg_dealt = calc.damage(my_character.attack_power, current_enemy.defense)
#     current_enemy.hp -= dmg_dealt
#     print (f"Attack Hit, {dmg_dealt} dmg")
# else:
#     print (f"Miss")
#

