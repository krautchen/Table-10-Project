from character import *
import json

def load_monsters(file_path):
    monsters = {"trash":[],"boss":[]}
    with open(file_path, 'r') as file:
        monster_data = json.load(file)
        for category,monster_list in monster_data.items():
            for monster in monster_list:
                monster_obj = Monster(
                    character_type=monster['character type'],
                    name=monster["name"],
                    hp=monster['hp'],
                    strength=monster['strength'],
                    defense=monster['defense'],
                    dexterity=monster['dexterity'],
                    hits=monster['hits'],
                    weapon=monster['weapon'],
                    armor=monster['armor'],
                    bag=monster['bag'],
                    exp_val=monster['exp_val']
                )
                monsters[category].append(monster_obj)
    return monsters

class Monster(Character):
    def __init__(self,
                character_type='Monster',
                name='Groht',
                level=1,         
                hp=1,
                strength=1,
                defense=1,
                dexterity=1,
                hits=1,
                weapon={},
                armor={},
                bag=[],
                exp_val=1):
        super().__init__(character_type,name,level,hp,strength,defense,dexterity,
                         hits,weapon,armor,bag)
        self.exp_val=exp_val

        
        
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
            f"bag={self.bag}),"
            f"exp_val={self.exp_val})"
        )