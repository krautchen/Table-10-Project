from character import *
import json

def load_monsters(file_path):
    """Loads monsters from a file.
    PA:  Noah Hibbler

    Args:
        file_path (str): Path to monster data file

    Returns:
        dict: a dictionary containing monsters
    """
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
    """Defines a monster from a Character class.
    PA: Noah Hibbler
    Attributes:
        exp_val (int): moster experience value

    Args:
        Character (class): Character class for base attributes
    """
    
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
        """Initializes monster object.
        PA: Noah Hibbler
        Args:
            character_type (str, optional): Type. Defaults to 'Monster'.
            name (str, optional): Monster name. Defaults to 'Groht'.
            level (int, optional): Monster level. Defaults to 1.
            hp (int, optional): Monster health. Defaults to 1.
            strength (int, optional): Monster strength. Defaults to 1.
            defense (int, optional): Monster defense. Defaults to 1.
            dexterity (int, optional): Monster dexterity. Defaults to 1.
            hits (int, optional): Monster number of attacks. Defaults to 1.
            weapon (dict, optional): Monster weapon object. Defaults to {}.
            armor (dict, optional): Monster armor object. Defaults to {}.
            bag (list, optional): Monster bag. Defaults to [].
            exp_val (int, optional): Monster experience value. Defaults to 1.
            
        Side effects:
            Sets monster attributes
        """
        super().__init__(character_type,name,level,hp,strength,defense,dexterity,
                         hits,weapon,armor,bag)
        self.exp_val=exp_val

        
        
    def __repr__(self):
        """Formal representation of the monster.
        PA: Noah Hibbler
        
        Returns:
            str: Monster attributes
        """
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