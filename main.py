
from items import *
from character import *
from monster import load_monsters
from argparse import ArgumentParser
import sys

class Game:
    def __init__(self):
    
    def load_genre(self,genre):
        fantasy = r"""^(f[a-z]*n[a-z]*t[a-z]*s[a-z]*y)$"""
        scifi = r"""(?x)^(s[a-z]*c[a-z]*i[a-z]*
                        e?n?c?e?f?
                        [a-z]*i[a-z]*c?t?[a-z]*i[a-z]*o?n?)$"""

        fantasy_regex = re.compile(fantasy, re.IGNORECASE)
        scifi_regex = re.compile(scifi, re.IGNORECASE)

        if fantasy_regex.match(genre) == True:
            load_items('fantasy_items.json')
            load_monsters('fantasy_monsters.json')

        elif scifi_regex.match(genre):
            raise NotImplementedError("This genre isn't ready yet!")
    

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