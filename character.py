from random import randrange
from items import *

def d6(number):
    """Roll a six sided die
    PA: Noah Hibbler
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
    """Creates a Character object.
    PA: Noah Hibbler
    
    Attributes:
        character (Character): a Character object
        points (int): the number of points a character has
    """
    def __init__(self):
        """Creates attributes for CharacterCreator object.
        PA: Noah Hibbler
        
        Side effects:
            Sets character and points attributes.
        """
        self.character = None
        self.points=d6(1)

    def create_character(self):
        """Creates a character for the game.
        PA: Noah Hibbler
        
        Side effects:
            Sets character name and stats attributes.
        """
        name = input("Enter your character's name: ")
        strength = self.assign_stat("strength")
        defense = self.assign_stat("defense")
        dexterity = self.assign_stat("dexterity")

        self.character = Character(name=name, strength=strength, defense=defense, dexterity=dexterity)
        print(f"\nCharacter '{self.character.name}' created with the following attributes: \n{self.character.strength} strength \n{self.character.defense} defense \n{self.character.dexterity} dexterity")

    def assign_stat(self, attribute_name):
        """Assigns a stat to a character.
        PA: Noah Hibbler
        
        Args:
            attribute_name (str): the name of the stat to assign
        
        Returns:
            int: the value of the stat
        Side effects:
            Prints error messages for invalid user input
        """
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
    """A basic character template.
    PA: Noah Hibbler
    
    Attributes:
        type (str): type of the character
        name (str): name of the character
        level (int): level of the character
        hp (int): health of the character
        strength (int): strength of the character
        defense (int): defense of the character
        dexterity (int): dexterity of the character
        hits (int): number of attacks the character can make
        weapon (Weapon): weapon of the character
        armor (Armor): armor of the character
        bag (Bag): bag of the character
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
        PA: Noah Hibbler
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
        self.weapon= Weapon(name='Fist',type="Blunt",damage=1)
        self.armor=Armor(name='Shield',armor_value=1)
        self.bag=Bag(name='Sack',size=1,contents=[])
                        
    def attack(self,target):
        """Generic attack.
        PA: Noah Hibbler
        
        Args:
            target (Character): target to attack
        Returns:
            str: Total damage
        Side effects:
            Possibly modifies the target's hp and prints combat sequence
        """
        if d6(self.dexterity)+self.dexterity > d6(target.defense):
            damage = (d6(self.strength)) * self.weapon.damage
            total_damage = damage - (self.armor.armor_value+self.defense)
            
            if total_damage > 0:
                target.take_damage(total_damage)
                # should print target hp after this print statement
                return print(f"{self.name} attacks {target.name} for {total_damage} damage.\n")
            
            else:
                print(f"{self.name} fails to damage {target.name}.\n"+
                      f"{target.name}'s armor is too tough.\n")
        else:
            return print(f"{target.name} deftly dodges.\n")
        
    def take_damage(self,total_damage):
        """Sets the damage to the target and resulting hp.
        PA: Noah Hibbler
        Args:
            total_damage (int): amount of damage
        Side effects:
            Sets hp attribute
        """
        self.hp-=total_damage
        
    def heal(self,healing_value):
        """Sets the restoration for target and resulting hp.
        PA: Noah Hibbler
        Args:
            healing_value (int): amount of restoration
        Side effects:
            Sets hp attribute
        """
        self.hp+=healing_value
    
    def equip_weapon(self,weapon):
        """Equips a Character with a weapon.
        PA: Noah Hibbler
        Args:
            weapon (Weapon): weapon of choice
            
        Side effects:
            Sets weapon attribute
        """
        self.weapon=weapon
        
    def equip_armor(self,armor):
        """Equips a Character with armor.
        PA: Noah Hibbler
        Args:
            armor (Armor): armor of choice
            
        Side effects:
            Sets armor attribute
        """
        self.armor=armor
    
    def equip_bag(self,bag):
        """Equips a Character with a bag.
        PA: Noah Hibbler
        Args:
            bag (Bag): bag of choice
        
        Side effects:
            Sets bag attribute
        """
        # should set new bag contents equal to what was in the old bag
        old_bag_items = self.bag.contents
        self.bag=bag
        self.bag.contents=old_bag_items