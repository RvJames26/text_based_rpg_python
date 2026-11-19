# Text Based RPG

A small turn-based RPG played in the terminal. Choose a character, fight randomly selected enemies, and see how long you can survive.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Run the game

Clone the repository, open a terminal in the project folder, and run:

```bash
python main.py
```

On some systems, use `python3 main.py` instead.

## How to play

1. Select **1** to start from the main menu.
2. Choose a character: **SwordMaster** or **Shadow**.
3. During each fight, enter **1** to attack.
4. Attacks can miss based on the target's evasion. Damage is calculated from attack power minus defense, with a minimum of zero.
5. Defeat enemies to continue. The game ends when your character's HP reaches zero.

## Characters

| Character | HP | Attack | Defense | Evasion | Critical chance | Special ability |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| SwordMaster | 150 | 14 | 8 | 5% | 10% | Bulwark Stance |
| Shadow | 80 | 18 | 3 | 35% | 25% | Shadow Strike |

Critical hit chances and special abilities are listed as character stats, but are not implemented in combat yet.

## Enemies

Enemies are selected randomly for each encounter:

| Enemy | HP | Attack | Defense | Evasion |
| --- | ---: | ---: | ---: | ---: |
| Cave Slime | 40 | 8 | 0 | 0% |
| Goblin Scavenger | 60 | 15 | 2 | 20% |
| Armored Sentinel | 100 | 12 | 10 | 0% |
| Void Knight | 250 | 20 | 5 | 0% |

## Project structure

```text
character/      Player character classes and selection
enemies/        Enemy classes and random enemy selection
fight_menu/     Turn-based combat
main_menu/      Start menu
calculations/   Hit chance and damage calculations
main.py         Game entry point
```

## License

No license has been added yet. Add a `LICENSE` file before allowing others to reuse or distribute this project.
