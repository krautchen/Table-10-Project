import json

def load_items(items_file):
    """_summary_

    Args:
        items_file (file): a file with items

    Returns:
        dict: a dictionary of items
    """
    items = {"weapons": [], "armor": [], "consumables": [], "bags": []}
    with open(items_file, 'r') as file:
        data = json.load(file)
        for category, item_list in data.items():
            for item in item_list:
                if category == "weapons":
                    item = Weapon(item['name'],
                                  item['type'],
                                  item['damage'])
                elif category == "armor":
                    item = Armor(item['name'],
                                 item['armor_value'])
                elif category == "consumables":
                    item = Consumable(item['name'],
                                      item['healing_value'])
                elif category == "bags":
                    item = Bag(item['name'],
                               item['size'])
                items[category].append(item)
    return items

class Item:
    """A class for items
    """
    def __init__(self, name):
        self.name = name
        
class Weapon(Item):
    """A class for weapons

    Args:
        Item (class): Item class for names
    """
    def __init__(self, name, type, damage):
        """Initialize weapons

        Args:
            name (str): name of weapon
            type (list): weapon types
            damage (int): weapon damage
        """
        super().__init__(name)
        self.type = type
        self.damage = damage
        
    def __str__(self):
        """User-friendly string representation of the Weapon."""
        return f"Weapon: {self.name}, Types: {self.type}, Damage: {self.damage}"
        
    def __repr__(self):
        return f"Weapon(name={self.name}, type={self.type}, damage={self.damage})"

class Armor(Item):
    """A class for armor

    Args:
        Item (class): Item class for names
    """
    def __init__(self, name, armor_value):
        """Initialize armor

        Args:
            name (str): name of weapon
            armor_value (int): armor value
        """
        super().__init__(name)
        self.armor_value = armor_value
        
    def __str__(self):
        """print the object, but user-friendly"""
        return f"Armor: {self.name}, Armor Value: {self.armor_value}"
        
    def __repr__(self):
        """print the object

        Returns:
            str: formal representation of the object
        """
        return f"Armor(name={self.name}, armor_value={self.armor_value})"

class Consumable(Item):
    """A class for consumables

    Args:
        Item (class): Item class for names
    """
    def __init__(self, name, healing_value):
        """Initialize consumable objects

        Args:
            name (str): name of the consumable
            healing_value (int): How many 
        """
        super().__init__(name)
        self.healing_value = healing_value
        
    def __str__(self):
        """print the object, but user-friendly"""
        return f"Consumable: {self.name}, Healing Value: {self.healing_value}"
        
    def __repr__(self):
        """print the object

        Returns:
            str: formal representation of the object
        """
        return f"Consumable(name={self.name}, healing_value={self.healing_value})"

        
    def heal(self,target):
        target.heal(self.healing_value)

class Bag(Item):
    """Stores items in a list

    Args:
        Item (class): Item class for names
    """
    def __init__(self, name, size, contents=[]):
        """Initialize bag objects

        Args:
            name (str): Type of bag
            size (int): Size of bag
            contents (list, optional): stores item data. Defaults to [].
        """
        super().__init__(name)
        self.size = size
        self.contents = contents
        
    def __str__(self):
        """print the object, but user-friendly"""
        return f"""Bag: {self.name}
                    Size: {self.size}
                    Contents: {self.contents}"""
                        
    def __repr__(self):
        """print the object

        Returns:
            str: formal representation of the object
        """
        return f"Bag(name={self.name}, size={self.size})"
        
    def store(self,item):
        """Put a thing in the bag

        Args:
            item (object): Item to store
            
        Side effects:
            modifies contents of bag object
        """
        self.contents.append(item)
    
    def remove(self,item):
        """Remove a thing from the bag

        Args:
            item (object): Item to store
            
        Side effects:
            modifies contents of bag object
        """
        self.contents.remove(item)

    def organize(self):
        """Organize things in the bag

        Args:
            item (object): Item to store
            
        Side effects:
            modifies contents of bag object
        """
        self.contents=sorted(self.contents,key=lambda item: item.name)