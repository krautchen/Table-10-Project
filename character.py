from random import randrange
from items import *

def d6(number):
    """Roll a six sided die

    Args:
        number (int): how many dice to roll

    Returns:
        int: sum of dice rolls
    """
    if number>1:
        return sum([randrange(1, 7) for _ in range(number)])
    else:
        return randrange(1,7)

class CharacterCreator:
    def __init__(self):
        self.character = None
        self.points=d6(1)

  
    def create_character(self):
        name = input("Enter your character's name: ")
        strength = self.get_attribute("strength")
        defense = self.get_attribute("defense")
        dexterity = self.get_attribute("dexterity")

        self.character = Character(name=name, strength=strength, defense=defense, dexterity=dexterity)
        print(f"\nCharacter '{self.character.name}' created with the following attributes:")
        self.character.status()

    def assign_stat(self, attribute_name):
        while True:
            try:
                value = int(input(f"How many points do you want in {attribute_name}? "))
                if 1 <= value <= 10:
                    return value
                else:
                    print(f"Invalid input. {attribute_name.capitalize()} must be between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
class Character:
    """A basic character tempalte
    """
    def __init__(self,
                character_type='Player',
                name='Gandalf',
                level=1,         
                hp=10,
                strength=2,
                defense=2,
                dexterity=2,
                hits=1,
                weapon={},
                armor={},
                bag=[]
                ):
        """Initialize a character(Char)

        Args:
            character_type (str, optional): Char type. Defaults to 'Player'.
            name (str, optional): Char name. Defaults to 'Gandalf'.
            level (int, optional): Char level. Defaults to 1.
            hp (int, optional): Char health. Defaults to 10.
            strength (int, optional): Char strength. Defaults to 2.
            defense (int, optional): Char defense. Defaults to 2.
            dexterity (int, optional): Char dexterity. Defaults to 2.
            hits (int, optional): Char number of attacks. Defaults to 1.
            weapon (dict, optional): Char weapon object. Defaults to {}.
            armor (dict, optional): Char armor object. Defaults to {}.
            bag (list, optional): Char bag object. Defaults to [].
        """
        self.type=character_type
        self.name=name
        self.level=level
        self.hp=hp
        self.strength=strength
        self.defense=defense
        self.dexterity=dexterity
        self.hits=hits
        self.weapon= Weapon(name,type,damage=1)
        self.armor=Armor(name,armor_value=1)
        self.bag=Bag(name='Sack',size=1,contents=[])
                        
    def attack(self,target):
        """Generic attack

        Returns:
            str: Total damage
        Side effects:
            Possibly modifies the target's hp
        """
        if d6(self.dexterity)+self.dexterity > d6(target.defense):
            damage = (d6(self.strength)) * self.weapon.damage
            total_damage = damage - (self.armor.armor_value+self.defense)
            
            if total_damage > 0:
                target.take_damage(total_damage)
                return print(f"{self.name} attacks {target.name} for {total_damage} damage.")
            
            else:
                print(f"{self.name} fails to damage {target.name}. "+
                      f"{target.name}'s armor is too tough")
        else:
            return print(f"{target.name} deftly dodges.")
        
    def take_damage(self,total_damage):
        self.hp-=total_damage
        
    def heal(self,healing_value):
        self.hp+=healing_value
        
    def status(self):
        print(f"""{self.name} has {self.hp} HP""")
        
    def level_up(self,stat):
        raise NotImplemented
    
    def equip_weapon(self,weapon):
        self.weapon=weapon
        
    def equip_armor(self,armor):
        self.armor=armor