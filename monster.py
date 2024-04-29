from character import *
import json

def load_monsters(file_path):
    with open(file_path, 'r') as file:
        monster_data = json.load(file)
        print(file)
        monsters = []
        for monster in monster_data:
            monster_obj = Monster(
                character_type=monster.get('character type'),
                name=monster.get('name'),
                hp=monster.get('hp'),
                strength=monster['strength'],
                defense=monster['defense'],
                dexterity=monster['dexterity'],
                hits=monster['hits'],
                weapon=monster['weapon'],
                armor={},
                bag=monster['bag']
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
        self.type=character_type
        
        
    def __repr__(self):
        # Create a detailed representation of the Monster
        return (
            f"Monster(name={self.name}, "
            f"type={self.type}, "
            f"level={self.level}, "
            f"hp={self.hp}, "
            f"strength={self.strength}, "
            f"defense={self.defense}, "
            f"dexterity={self.dexterity}, "
            f"hits={self.hits}, "
            f"weapon={self.weapon}, "
            f"armor={self.armor}, "
            f"bag={self.bag})"
        )