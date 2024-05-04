
from items import *
from character import *
from monster import load_monsters
from driver import *
from argparse import ArgumentParser
import sys
import re

class Game:
    """Defines the game interface and playing.
    
    Attributes:
        genre (str): the genre of the game
    """
    def __init__(self, genre):
        self.genre = genre
        self.equip_prompt = """Would you like to equip any items from your bag?\n
        > Yes\n
        > No
        """
        self.equip_type_prompt = """Would you like to equip any items from your bag?\n
        > Weapons\n
        > Armor\n
        > Bags\n
        > Back\n
        Type the item type, a forward slash, then the item to equip.\n
        For example, "Weapons/Sword" to equip the sword weapon.
        """
        self.load_genre()
        
    def load_genre(self):
        fantasy = r"""^fantasy$"""
        scifi = r"""(?x)^sci[enc\s-]*?fi[ction]*?$"""

        fantasy_regex = re.compile(fantasy, re.IGNORECASE)
        scifi_regex = re.compile(scifi, re.IGNORECASE)

        if fantasy_regex.match(self.genre) == True:
            self.items = load_items('fantasy_items.json')
            self.monsters = load_monsters('fantasy_monsters.json')

        elif scifi_regex.match(self.genre):
            raise NotImplementedError("This genre isn't ready yet!")
    
    def play(self):
        print("----------------------------------------------------------------")
        print(f"Welcome to the Basic World of {self.genre.capitalize()}!")
        print("----------------------------------------------------------------")
        new_char = CharacterCreator()
        new_char.create_character()
        new_map = Map()
        while new_map.gameEnd != True:
            self.status(new_char.character)
            choice = new_map.room_description(new_char.character.name)
            if choice == "fight monsters":
                new_map.has_monsters(new_char.character)
            elif choice == "collect items":
                new_map.has_items(new_char.character)
            elif choice == "move to next room":
                new_map.has_puzzle()
                new_map.room_transition()
                self.equip(new_char.character)
            else:
                print("Game over.")
                new_map.gameEnd = True
    def equip(self, char):
        user_input = self.invalid_input(self.equip_prompt)
        if user_input == "yes":
            print(char.bag.contents)
            equip_input = input(self.equip_type_prompt).lower()
            if "/" in equip_input:
                type, item = equip_input.split("/")
                if type == "weapon":
                    char.equip_weapon(self.items[type][0]) if item == "fist" else \
                    char.equip_weapon(self.items[type][1]) if item == "sword" else \
                    char.equip_weapon(self.items[type][2])
                elif type == "armor":
                    char.equip_armor(self.items[type][0]) if item == "shield" else \
                    char.equip_armor(self.items[type][1]) if item == "helmet" else \
                    char.equip_armor(self.items[type][2]) if item == "studded leather" else \
                    char.equip_armor(self.items[type][3])
                elif type == "bag":
                    char.equip_bag(self.items[type][0]) if item == "sack" else \
                    char.equip_bag(self.items[type][1]) if item == "rucksack" else \
                    char.equip_bag(self.items[type][2])
            else:
                input(self.equip_prompt)
        else:
            pass
    def status(self, char):
        print("------------------------------------------------------------------------------------------------")
        print(f"""{char.name}, you currently have {char.hp} HP and the following items equipped:\n
              {char.weapon.name}\n
              {char.armor.name}\n
              {char.bag.name}""")
        print("------------------------------------------------------------------------------------------------")
    def invalid_input(self, prompt):
        while True:
            try:
                user_input = input(prompt).lower()
                if user_input in ["yes", "no"]:
                    return user_input
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            except ValueError:
                print("Invalid input. Please enter 'yes' or 'no'.")
def main(genre):
    game = Game(genre)
    game.play()


def parse_args(arglist):

    parser = ArgumentParser()
    parser.add_argument("genre", help="path to word list text file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.genre)