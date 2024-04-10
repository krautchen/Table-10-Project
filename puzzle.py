import json
import re
from random import choice, randint
# dice roll should be after direction selection because then you can populate 
# the status of enemies, items, whether there's a puzzle in the new currentRoom
# based on the result
# puzzle function is called based on a dice roll
# if the roll is an odd number then the puzzle function is called and a random 
# puzzle is loaded from the json along with any necessary items, enemies, etc.

# first, the user has to know that they encountered a room like that (user
# should have a current_room attribute assigned to a Room object)

def puzzle():
    """Generates a random puzzle if the dice roll requires it.
    
    Side effects:
        Prints a puzzle prompt and results of the guesses to stdout.
    """
    guess_count = 0
    with open("puzzles.json", "r", encoding="utf-8") as file:
        puzzles = json.load(file)
        current_puzzle = puzzles[f"{randint(1, len(puzzles))}"]
    #if player.current_room.has_puzzle:
        code = current_puzzle["code"]
        print(current_puzzle["prompt"])
    while guess_count < 5:
        guess = input("Please enter your guess: ")
        if len(guess) == 0:
            guess_count += 1
            print("Guess must contain at least one character.")
        else:
            if re.search(code, guess):
                print(f"{guess} is correct!")
                break
                # move character into room by setting current_room attribute to next room
            else:
                print(f"{guess} is incorrect!")
                guess_count += 1
        if guess_count == 5:
            print("Sorry, you have run out of guesses.")
                # keep character in current_room, do nothing
puzzle()
