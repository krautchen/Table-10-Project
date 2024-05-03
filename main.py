
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
        new_char = CharacterCreator()
        new_char.create_character()
        new_map = Map()
        
        while new_char.character.hp > 0:
            choice = new_map.room_description(new_char.character.name)
            if choice == "fight monsters":
                new_map.has_monsters(new_char.character)
            elif choice == "collect items":
                new_map.has_items(new_char.character)
            else:
                new_map.room_transition()

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