from character import *

def load_monsters(file_path):
    with open(file_path, 'r') as file:
        monster_data = json.load(file)

    monsters = []
    for monster in monster_data:
        monster_obj = Character(
            character_type=monster['character_type'],
            name=monster['name'],
            hp=monster['hp'],
            strength=monster['strength'],
            defense=monster['defense'],
            dexterity=monster['dexterity'],
            hits=monster['hits'],
            weapon=monster['weapon'],
            armor={},
            bag=monster['contents']
        )
        monsters.append(monster_obj)

    return monsters

class Monster:
    def __init__(self):
        self.name