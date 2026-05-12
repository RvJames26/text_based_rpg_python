
from character.pick_character import CharacterSelection
from main_menu.menu import Start

my_game = Start("start")
my_game.run_menu()

character_selection = CharacterSelection()
my_character = character_selection.pick_class()