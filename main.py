
from character.pick_character import CharacterSelection
from main_menu.menu import Start
from enemies.enemy_spawner import EnemySpawner
from fight_menu.menu import FightMenu

my_game = Start()
if not my_game.run_menu():
    raise SystemExit

character_selection = CharacterSelection()

while True:
    my_character = character_selection.pick_class()

    while True:
        spawner = EnemySpawner()
        current_enemy = spawner.spawn_random_enemies()

        print(f"A {current_enemy.__class__.__name__} appeared")

        battle_screen = FightMenu(my_character, current_enemy)
        player_survived = battle_screen.display_menu()

        if not player_survived:
            break

