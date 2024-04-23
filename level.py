import sys
import json
import math
import os

from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path
from assignments.level_schema import Level

console = Console()
os.system('clear' if os.name == 'posix' else 'cls')


def load_level_data(level: int) -> Level:
    game_data_path = Path(__file__).parent / "assignments" / "gamedata.json"
    game_data_raw = json.loads(game_data_path.read_text())
    levels = [Level(**level) for level in game_data_raw['levels']]
    return levels[level]


def render_difficulty(level_difficulty: int):
    number_of_full = math.ceil(level_difficulty / 2)
    number_of_empty = 5 - number_of_full
    empty = "○"
    full = "●"
    difficulty = ""
    for i in range(0, number_of_full):
        difficulty += full
    for i in range(0, number_of_empty):
        difficulty += empty
    return difficulty


def display_assignment(level_id: int):
    level: Level = load_level_data(level_id)
    source: Path = Path(__file__).parent / "assignments" / "levels" / level.description

    level_path = \
        ("\n\nContract's code: contracts/" + level.instance_contract + \
        "\n- HINT: You can try (ctrl + click) on the file path. That should open the file in your editor (if your IDE supports it).") \
        if (level_id > 0) else ""

    markdown_output =                                                    \
        "# " + level.name + "\n" +                                       \
        "Difficulty: " + render_difficulty(level.difficulty)  + "\n\n" + \
        source.read_text() +                                             \
        level_path
    
    console.print(Markdown(markdown_output))
    sys.exit(0)


def display_finished(level_id: int):
    level: Level = load_level_data(level_id)
    source = Path(__file__).parent / "assignments" / "levels" / str(level.completed_description)

    markdown_output = \
        "# " + level.name + " finished!" + "\n" +\
        source.read_text()
    
    console.print(Markdown(markdown_output))
    sys.exit(0)


def display_help():
    game_data_path = Path(__file__).parent / "assignments" / "README.md"
    console.print(Markdown(game_data_path.read_text()))


if len(sys.argv) >= 2:
    try: level_index = int(sys.argv[1])
    except:
        display_help()
        exit()
if len(sys.argv) >= 3 and sys.argv[2] == "done":
    display_finished(level_index)
else:
    display_assignment(level_index)
