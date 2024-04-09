from random import randrange

def d6(number):
    """Roll a six sided die

    Args:
        number (_type_): _description_

    Returns:
        _type_: _description_
    """
    result=number*randrange(1,6)
    return result

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
    
class Character():
    """A basic character tempalte
    """
    def __init__(self,
                character_type=None,
                name='Player',
                level=1,         
                hp=1,
                strength=1,
                defense=1,
                dexterity=1,
                hits=1,
                weapon={},
                armor={},
                bag=[]
                ):
        """Generic character attributes

        Args:
            name (string): Character name
            type (string): The type of weapon
            hits (int): Number of hits
            weapon_damage (int): How much damage the type type of item does
            size (int, optional): How big the bag is. Defaults to 5.
            contents (list, optional): Stuff in the bag. Defaults to [].
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
        self.bag=Bag(name='Sack',size=1,contents=['rope'])
                        
    def attack(self,target):
        """Generic attack

        Returns:
            str: Total damage
        Side effects:
            Possibly modifies the target's hp
        """
        if d6(self.dexterity)+self.dexterity > d6(target.defense):
            damage = (d6(self.strength)) * self.weapon.damage
            total_damage = damage - self.armor.armor_value
            if total_damage > 0:
                target.take_damage(total_damage)
                return print(f"{self.name} attacks {target.name} for {total_damage} damage.")
            else:
                print(f"{self.name} fails to damage {target.name}. "+
                      f"{target.name}'s armor is too tough")
        
    def take_damage(self,total_damage):
        self.hp-=total_damage
        
    def heal(self,healing_value):
        self.hp+=healing_value
        
    def status(self):
        print(f"""{self.name} has {self.hp} HP""")
        
    def level_up(self,stat):
        raise NotImplemented    

class Item:
    def __init__(self, name):
        self.name = name

class Weapon(Item):
    def __init__(self, name, type, damage):
        super().__init__(name)
        self.type = type
        self.damage = damage

class Armor(Item):
    def __init__(self, name, armor_value):
        super().__init__(name)
        self.armor_value = armor_value

class Consumable(Item):
    def __init__(self, name, healing_value):
        super().__init__(name)
        self.healing_value = healing_value
        
    def heal(self,target):
        target.heal(self.healing_value)

class Bag(Item):
    def __init__(self, name, size, contents=None):
        super().__init__(name)
        self.size = size
        self.contents = contents or []
        
    def store(self,item):
        self.contents.append(item)
    
    def remove(self,item):
        self.contents.remove(item)

    def organize(self):
        sorted(self.contents,key=lambda bag: bag[1])