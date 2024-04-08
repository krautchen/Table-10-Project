import json
import re
# puzzle function is called when a user interacts with a room that has the
# has_puzzle attribute (or something like that)

# first, the user has to know that they encountered a room like that (user
# should have a current_room attribute assigned to a Room object)

def puzzle():
    guess_count = 0
    with open("puzzles.json", "r", encoding="utf-8") as file:
        puzzle1 = json.load(file)
    #if player.current_room.has_puzzle:
        code = puzzle1["1"]["code"]
        print(puzzle1["1"]["prompt"])
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
print(puzzle())
