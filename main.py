
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
        self.items = {}
        self.monsters = {}
        
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
        
        while new_char.character.hp > 0:
            new_map = Map()
            new_map.mapDriver("rooms.json")
            # mapDriver holds logic for stating whether a room has items and/or monsters
            if new_map.randomMap[int(new_map.current)]["monsters"] is not None:
                if new_map.randomMap[int(new_map.current)]["items"] is not None:
                    turn = "character"
                    print("Player must defeat all monsters before collecting items. Combat Start!")
                    for type, monster in self.monsters.items():
                        while monster.hp > 0:
                            if turn == "character":
                                new_char.character.attack(monster)
                                turn = "monster"
                            else:
                                monster.attack(new_char.character)
                        print("You defeated it!")
                else:
                    print("Defeat all monsters to progress to next room!")
            else:
                if new_map.randomMap[int(new_map.current)]["items"] is not None:
                    print("Collect all items to progress to next room!")
                else:
                    print("Progress to next room!")

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