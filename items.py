import json
def load_items(items_file):
    items = {"weapons": [], "armor": [], "consumables": [], "bags": []}
    with open(items_file, 'r') as file:
        data = json.load(file)
        for category, item_list in data.items():
            for item_data in item_list:
                if category == "weapons":
                    item = Weapon(item_data['name'],
                                  item_data['type'],
                                  item_data['damage'])
                elif category == "armor":
                    item = Armor(item_data['name'],
                                 item_data['armor_value'])
                elif category == "consumables":
                    item = Consumable(item_data['name'],
                                      item_data['healing_value'])
                elif category == "bags":
                    item = Bag(item_data['name'],
                               item_data['size'])
                items[category].append(item)
    return items

class Item:
    def __init__(self, name):
        self.name = name
        
class Weapon(Item):
    def __init__(self, name, type, damage):
        super().__init__(name)
        self.type = type
        self.damage = damage
        
    def __repr__(self):
        return f"Weapon(name={self.name}, type={self.type}, damage={self.damage})"

class Armor(Item):
    def __init__(self, name, armor_value):
        super().__init__(name)
        self.armor_value = armor_value
    def __repr__(self):
        return f"Armor(name={self.name}, armor_value={self.armor_value})"

class Consumable(Item):
    def __init__(self, name, healing_value):
        super().__init__(name)
        self.healing_value = healing_value
        
    def __repr__(self):
        return f"Consumable(name={self.name}, healing_value={self.healing_value})"

        
    def heal(self,target):
        target.heal(self.healing_value)

class Bag(Item):
    def __init__(self, name, size, contents=[]):
        super().__init__(name)
        self.size = size
        self.contents = contents
        
    def __repr__(self):
        return f"Bag(name={self.name}, size={self.size})"
        
    def store(self,item):
        self.contents.append(item)
    
    def remove(self,item):
        self.contents.remove(item)

    def organize(self):
        self.contents=sorted(self.contents,key=lambda bag: bag['name'])