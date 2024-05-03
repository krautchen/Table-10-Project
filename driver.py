import json
import random
import sys
from argparse import ArgumentParser
from puzzle import puzzle as p
from items import *
from monster import load_monsters
#answer is L3ST TR10S4R1
"""Functionality check-list for map
-add non square/rectangle rooms
-add the items to each of the rooms after functionality for such has been 
created
"""

class Map:
    """
    The map that is being used.

    Attributes:
        prompt: string
            a prompt asking which direction to travel
        invalidDirection: string
            a prompt explaining the direction choice is not valid
        neswError: string
            a prompt explaining to choose a valid cardinal direction
        neswCheck: list
            the list of valid cardinal directiosn
        playInput: string
            a prompt asking the user if they want to continue
        gameEnd: boolean
            signals if the game is over
        puzzleEnd: string
            signals if the puzzle has been run and completed
        current: string
            the current room that the player is in
    
    """
    def __init__(self):
        """
        Initalizes a map object
        side effects:
            Initalizes all the values
        """
        self.directionPrompt = "Which direction would you like to go? "
        self.roomPrompt = "What do you want to do? Type (fight monsters), (collect items), or (move to next room). Or type quit to quit "
        self.invalidDirection = "invalid choice, please choose another directon"
        self.neswError = "please choose a movement of nesw" 
        self.neswCheck = ["n", "s", "e", "w"]
        self.playInput = "would you like to continue? "
        self.gameEnd = False 
        self.puzzleEnd = "not complete"
        self.itemCheck = False
        self.monsterCheck = False
        self.name = ""
        self.first = False
        self.items = load_items('fantasy_items.json')
        self.monsters = load_monsters('fantasy_monsters.json')
        
        with open ("rooms.json", "r", encoding= "utf-8") as f:
            map = json.load(f)
        
        #picks a random map
        randomMap = random.choice(list(map))
        self.playRoom = map[randomMap]
        #picks random room in map
        randomRoom= str(random.randint(1, len(map[randomMap])))
        #random chance for the puzzle to appear
        #game start
        self.currentRoom = self.playRoom[randomRoom]
        print(self.currentRoom)

    def room_description(self, name):
        """Describes current room in the game, including what's in it and prompts the user on what to do.
        
        Side effects:
            prints the description of the current room
        """
        self.name = name
        if "monsters" in self.currentRoom or "items" in self.currentRoom:
            if "items" not in self.currentRoom:
                print(f"""Room description:\n
                {name} is currently in room {self.currentRoom["current"]}.
                This room has {len(self.currentRoom["monsters"])} monsters and 0 items.
                """)
            elif "monsters" not in self.currentRoom:
                print(f"""Room description:\n
                {name} is currently in room {self.currentRoom["current"]}.
                This room has 0 monsters and {len(self.currentRoom["items"])} items.
                """)
            else:
                print(f"""Room description:\n
                    {name} is currently in room {self.currentRoom["current"]}.
                    This room has {len(self.currentRoom["monsters"])} monsters and {len(self.currentRoom["items"])} items.
                    """)
        else:
            print(f"""Room description:\n
                {name} is currently in room {self.currentRoom["current"]}.
                This room has no monsters or items.
                """)
        
        choice = input(self.roomPrompt).lower()
        if choice == "quit":
                self.gameEnd = True
                return "goodbye!"
        while choice not in ["fight monsters", "collect items", "move to next room", "quit"]:
            print("Choose between the three prompts provided. Or type quit to quit")
            choice = input(self.roomPrompt)
            if choice == "quit":
                self.gameEnd = True
                return "goodbye!"
        return choice
    
    def room_transition(self):
        """Handles player movement between rooms.
        
        Args:
            userInput (str): the direction the player wants to move in
        """
        while(self.gameEnd != True):
            if self.first == False:
                r = self.room_description(self.name)
                if self.gameEnd == True:
                    return print("game over.")
                self.first = True
            try:
                userInput = input(self.directionPrompt).lower()
                if userInput in self.neswCheck and userInput in self.currentRoom:
                    while self.currentRoom[userInput] == "invalid movement":
                        print(self.invalidDirection)
                        userInput = input(self.directionPrompt).lower()
                else:
                    r = self.room_description(self.name)
                    if self.gameEnd == True:
                        return print("game over.")
                    self.current = self.playRoom[self.currentRoom[userInput]]
                    self.currentRoom = self.current
            finally:
                self.currentRoom = self.playRoom[self.currentRoom[userInput]]
            r = self.room_description(self.name)
            if self.gameEnd == True:
                return print("game over.")
        return r

    
    def has_puzzle(self):
        """Checks if the incoming room has a puzzle associated with it and if it does, executes the imported puzzle function.
        """
        puzzleChance = random.randint(1, 10)
        willGetPuzzle = random.randint(1,3) 
        
        if self.puzzleEnd != "complete":
            if willGetPuzzle == puzzleChance:
                self.puzzleEnd = p() 
    def has_items(self, char):
        """Checks if the current room has items, and if it does, asks the player if they want to equip after storing every item automatically.
        """
        if "items" in self.currentRoom:
            self.itemCheck = True
        # category is the type of item and objects is the list of item objects
        # this loop should return the dictionary of self.items only if the category is in self.currentRoom["items"]
        room_objects = {category: objects for category, objects in self.items.items() if category in self.currentRoom["items"]}
        for category in room_objects:
            for item in self.items[category]:
                char.bag.store(item)
                char.bag.organize()
                print(f"{item.name} has been added to your inventory.")
                # after this, it should remove the item from self.currentRoom["items"]
            
    def has_monsters(self, char):
        """Checks if the current room has monsters, and if it does, engage combat sequence.
        """
        if "monsters" in self.currentRoom:
            self.monsterCheck = True
            if "trash" in self.currentRoom["monsters"]:
                monster = self.monsters["trash"][0]
                print(monster)
                while monster.hp > 0:
                    char.attack(monster)
                    print("Monster attacked.") 
                print("monster defeated.")       
            if "boss" in self.currentRoom["monsters"]:
                monster = self.monsters["boss"][0]
                print(monster)
                while monster.hp > 0:
                    char.attack(monster)
                    print("Monster attacked.")
                print("monster defeated")
                self.currentRoom["monsters"].remove(monster)
                    
    # def mapDriver(self): 
    #     """
    #     The main driver for the users movement in the map

    #     Side effects:
    #         assigns the map and room at random read from a json file, 
    #         and then handles movement for the duration of the game. 
    #     """
    #     with open ("rooms.json", "r", encoding= "utf-8") as f:
    #         map = json.load(f)
        
    #     #picks a random map
    #     randomMap = random.choice(list(map))
    #     playRoom = map[randomMap]
    #     #picks random room in map
    #     randomRoom= str(random.randint(1, len(map[randomMap])))
    #     #random chance for the puzzle to appear
    #     #game start
    #     self.currentRoom = playRoom[randomRoom]
    #     print(self.currentRoom)

    #     current = self.currentRoom["current"]
    #     print(self.status(current))
    #     userInput = input(self.prompt).lower()
        
    #     if userInput not in self.currentRoom:
    #         userInput = self.playPrompt("nesw")

    #     if userInput not in self.neswCheck and self.gameEnd == False:
    #         userInput = self.playPrompt("nesw")
    #     elif self.gameEnd != True and userInput in self.currentRoom:
    #         movement = self.currentRoom[userInput]

    #     while(self.gameEnd != True):
    #         previous = self.currentRoom["current"]

    #         if userInput not in self.neswCheck:
    #              userInput = self.playPrompt("nesw").lower()
    #         elif self.gameEnd != True:
    #             self.currentRoom = playRoom[previous]
    #             current = self.currentRoom["current"]
                
    #         prevInput = userInput
            
    #         if movement == "invalid movement" and self.gameEnd == False:
    #             userInput = self.playPrompt("invalid")
    #             while(userInput not in self.currentRoom and self.gameEnd != True or 
    #                   prevInput == userInput):
    #                 prevInput = userInput
    #                 userInput = self.playPrompt("invalid").lower()
    #             if self.gameEnd != True and prevInput != userInput:
    #                 movement = self.currentRoom[userInput]
    #             if self.gameEnd:
    #                 break
    #         else:
    #             if "monsters" in self.currentRoom:
    #                 print(self.currentRoom)
    #                 self.monsterCheck = True
    #                 if "items" in self.currentRoom:
    #                     print(self.currentRoom)
    #                     self.itemCheck = True
    #                     print("You must defeat all monsters before collecting items!")
    #                 else:
    #                     print("You must defeat all monsters before progressing to the next room!")
    #             else:
    #                 if "items" in self.currentRoom:
    #                     print(self.currentRoom)
    #                     self.itemCheck = True
    #                     print("Collect items, then move to next room!")
    #                 else:
    #                     print(self.currentRoom)
    #                     print("Move to next room!")
    #             self.currentRoom = playRoom[movement]
    #             current = self.currentRoom["current"]

    #         puzzleChance = random.randint(1, 10)
    #         willGetPuzzle = random.randint(1,3) 
            
    #         if self.puzzleEnd != "complete":
    #             if willGetPuzzle == puzzleChance:
    #                 self.puzzleEnd = p()  
                    
    #         print(self.status(current))
    #         userInput = input(self.prompt).lower()
        
    #         if userInput not in self.currentRoom:
    #              userInput = self.playPrompt("nesw")
    #         if self.gameEnd != True:
    #             movement = self.currentRoom[userInput]
    # def status(self, cr):
    #     """
    #     Displays what room the user is currently in

    #     Args:
    #     cr: string
    #         The current room the user is

    #     Returns:
    #         returns the in a string explaining current positioning of the user    
    #     """
    #     return f"you are currently in room {cr}. {cr} has "
    # def playPrompt(self, errorChoice):
    #     """
    #     Handles errors for movement and invalid inputs.
    #     Args:
    #     errorChoice: string
    #         the type of error to be displayed to the user
        
    #     Returns:
    #         Either if the game is over or a valid movement for the user to 
    #         traverse
    #     """
    #     ansFlag = True
    #     once = False
    #     if errorChoice == "nesw":
    #         if once == False:
    #             print(self.neswError)
    #             once = True
    #         answer = input(self.playInput).lower()
    #     else:
    #         if once == False:
    #             print(self.invalidDirection)
    #             once = True
    #         answer = input(self.playInput).lower()
        
    #     while(ansFlag == True):
    #         if answer == "no":
    #             self.play = False 
    #             ansFlag = False
    #             print("goodbye!")
    #             self.gameEnd = True
    #             break
    #         elif answer == "yes":
    #             na = input(self.prompt).lower()
    #             if na in self.neswCheck:
    #                 ansFlag = False
    #                 return na
    #             else:
    #                 print("invalid answer, please try again.")
    #                 answer = input(self.playInput).lower()
    #         else: 
    #                 print("invalid answer, please try again.")
    #                 answer = input(self.playInput).lower()
