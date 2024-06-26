import json
import re
from random import randint
# -- Notes
# either populated from a dice roll or called when you move in certain directions

# dice roll should be after direction selection because then you can populate 
# the status of enemies, items, whether there's a puzzle in the new currentRoom
# based on the result

# if the roll is an odd number then the puzzle function is called and a random 
# puzzle is loaded from the json along with any necessary items, enemies, etc.
# character should have a current_room attribute to reference and update within 
# function

def puzzle():
    """Generates a random puzzle if the dice roll requires it. Updates 
    character's current_room attribute conditionally based on puzzle
    completion.
    PA: Michelle Akem
    Techniques: regex expressions
    Returns:
        str: status of the puzzle
    
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
        hint = current_puzzle["hint"]
    while guess_count < 5:
        guess = input("Please enter your guess: ")
        if len(guess) == 0:
            guess_count += 1
            print("Guess must contain at least one character.")
        elif guess == "exit":
            break
        else:
            if re.search(code, guess):
                print(f"{guess} is correct!")
                return "complete"
            else:
                print(f"{guess} is incorrect! Please try again.")
                if input("Would you like a hint? (y/n): ") == "y":
                    print(f"Hint: {hint}")
                else:
                    pass
                guess_count += 1
        if guess_count == 5:
            print("Sorry, you have run out of guesses.")
            return "failed"
if __name__ == "__main__":
    puzzle()