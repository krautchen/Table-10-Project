
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
        """Initialize a Game object.
        
        Args:
            genre (str): the genre of the game
        """
        self.genre = genre
        self.equip_prompt = """Would you like to equip any items from your bag?\n
        > Yes\n
        > No
        """
        self.equip_type_prompt = """What items would you like to equip?\n
        > Weapons\n
        > Armor\n
        > Bags\n
        > Back\n
        Type the item type, a forward slash, then the item to equip.\n
        For example, "Weapons/Sword" to equip the sword weapon.
        """
        
    def load_genre(self):
        """Loads the items and monsters for a genre.
        
        Side effects:
            Sets self.items and self.monsters attributes
        
        Raises:
            NotImplementedError: if genre is sci-fi
        """
        fantasy = r"""^fantasy$"""
        scifi = r"""(?x)^sci[enc\s-]*?fi[ction]*?$"""

        fantasy_regex = re.compile(fantasy, re.IGNORECASE)
        scifi_regex = re.compile(scifi, re.IGNORECASE)

        if fantasy_regex.match(self.genre) != None:
            self.items = load_items('fantasy_items.json')
            self.monsters = load_monsters('fantasy_monsters.json')

        elif scifi_regex.match(self.genre):
            raise NotImplementedError("This genre isn't ready yet!")
    
    def play(self):
        """Handles play sequence for the Game object.
        
        Side effects:
            Prints to stdout and sets gameEnd attribute
        """
        print("----------------------------------------------------------------")
        print(f"Welcome to the Basic World of {self.genre.capitalize()}!")
        print("----------------------------------------------------------------")
        new_char = CharacterCreator()
        new_char.create_character()
        new_map = Map()
        self.load_genre()
        while new_map.gameEnd != True:
            print(new_map)
            choice = new_map.room_description(new_char.character.name)
            if choice == "fight monsters":
                new_map.has_monsters(new_char.character)
            elif choice == "collect items":
                new_map.has_items(new_char.character)
            elif choice == "move to next room":
                new_map.room_transition()
                new_map.has_puzzle()
                self.equip(new_char.character)
                self.status(new_char.character)
            else:
                print("Game over.")
                new_map.gameEnd = True
    def equip(self, char):
        """Handles equip sequence after player is finished in a room.

        Args:
            char (Character): current character of user
        
        Side effects:
            Prints to stdout
        """
        user_input = input(self.equip_prompt).lower()
        if user_input == "yes":
            print(f"You have {len(char.bag.contents)} items in your bag.\n")
            contents = [print(item) for item in char.bag.contents]
            equip_input = self.input_check(self.equip_type_prompt)
            if equip_input:
                type, name = equip_input.split("/")
                for item in self.items[type]:
                    if item.name.lower() == name:
                        if type == "weapons":
                            char.equip_weapon(item)
                            print(f"{item.name.capitalize()} equipped.")
                        elif type == "armor":
                            char.equip_armor(item)
                            print(f"{item.name.capitalize()} equipped.")
                        elif type == "bags":
                            char.equip_bag(item)
                            print(f"{item.name.capitalize()} equipped.")
                        else:
                            pass
        else:
            pass

    def status(self, char):
        """Handles status sequence after player is finished in a room.

        Args:
            char (Character): current character of user
        
        Side effects:
            Prints to stdout
        """
        print("------------------------------------------------------------------------------------------------")
        print(f"""{char.name}, you currently have {char.hp} HP and the following items equipped:\n
              {char.weapon.name}\n
              {char.armor.name}\n
              {char.bag.name}""")
        print("------------------------------------------------------------------------------------------------")
    def input_check(self, prompt):
        """Checks user input for equip prompt to ensure it is valid.

        Args:
            prompt (str): prompt to print to user
        
        Returns:
            str: The validated user input.
        """
        while True:
            try:
                user_input = input(prompt).lower()
                if "/" in user_input:
                    type, name = user_input.split("/")
                    if type in ["weapons", "armor", "bags"]:
                        return user_input
                    else:
                        print("Invalid item type. Please enter a valid type (weapons, armor, bags).")
            except ValueError:
                print("Invalid input format. Please enter the type and name separated by '/'.")

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