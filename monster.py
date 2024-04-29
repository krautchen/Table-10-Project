from character import *

def load_monsters(file_path):
    with open(file_path, 'r') as file:
        monster_data = json.load(file)

    monsters = []
    for monster in monster_data:
        monster_obj = Monster(
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

class Monster(Character):
    def __init__(self,
                character_type='Monster',
                name='Player',
                level=1,         
                hp=1,
                strength=1,
                defense=1,
                dexterity=1,
                hits=1,
                weapon={},
                armor={},
                bag=[]):
        super().__init__(name,level,hp,strength,defense,dexterity,
                         hits,weapon,armor,bag)
        self.type='Monster'