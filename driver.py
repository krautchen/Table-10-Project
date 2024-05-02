import json
import random
import sys
from argparse import ArgumentParser
from puzzle import puzzle as p
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
        self.prompt = "Which direction would you like to go? "
        self.invalidDirection = "invalid choice, please choose another directon"
        self.neswError = "please choose a movement of nesw" 
        self.neswCheck = ["n", "s", "e", "w"]
        self.playInput = "would you like to continue? "
        self.gameEnd = False 
        self.puzzleEnd = "not complete"
        self.current = ""

    def mapDriver(self): 
        """
        The main driver for the users movement in the map

        Side effects:
            assigns the map and room at random read from a json file, 
            and then handles movement for the duration of the game. 
        """
        with open ("rooms.json", "r", encoding= "utf-8") as f:
            map = json.load(f)
        
        #picks a random map
        randomMap = random.choice(list(map))
        playRoom = map[randomMap]
        #picks random room in map
        randomRoom= str(random.randint(1, len(map[self.randomMap])))
        #random chance for the puzzle to appear
        #game start
        currentRoom = playRoom[randomRoom]

        self.current = currentRoom["current"]
        print(self.status(self.current))
        userInput = input(self.prompt).lower()
        
        if userInput not in currentRoom:
            userInput = self.playPrompt("nesw")

        if userInput not in self.neswCheck and self.gameEnd == False:
            userInput = self.playPrompt("nesw")
        elif self.gameEnd != True and userInput in currentRoom:
            movement = currentRoom[userInput]

        while(self.gameEnd != True):
            
            previous = currentRoom["current"]

            if userInput not in self.neswCheck:
                 userInput = self.playPrompt("nesw").lower()
            elif self.gameEnd != True:
                currentRoom = playRoom[previous]
                self.current = currentRoom["current"]
                
            prevInput = userInput
            
            if movement == "invalid movement" and self.gameEnd == False:
                userInput = self.playPrompt("invalid")
                while(userInput not in currentRoom and self.gameEnd != True or 
                      prevInput == userInput):
                    prevInput = userInput
                    userInput = self.playPrompt("invalid").lower()
                if self.gameEnd != True and prevInput != userInput:
                    movement = currentRoom[userInput]

            if self.gameEnd == True:
                        break
            else:
                currentRoom = playRoom[previous]
                self.current = currentRoom["current"]

            if movement != "invalid movement":
                currentRoom = playRoom[movement]
                self.current = currentRoom["current"]

            puzzleChance = random.randint(1, 10)
            willGetPuzzle = random.randint(1,3) 
            
            if self.puzzleEnd != "complete":
                if willGetPuzzle == puzzleChance:
                    self.puzzleEnd = p()  
                    
            print(self.status(self.current))
            userInput = input(self.prompt).lower()
        
            if userInput not in currentRoom:
                 userInput = self.playPrompt("nesw")
            if self.gameEnd != True:
                movement = currentRoom[userInput]
    
    def status(self, cr):
        """
        Displays what room the user is currently in

        Args:
        cr: string
            The current room the user is

        Returns:
            returns the in a string explaining current positioning of the user    
        """
        return f"you are currently in room {cr}"
        
    def playPrompt(self, errorChoice):
        """
        Handles errors for movement and invalid inputs.
        Args:
        errorChoice: string
            the type of error to be displayed to the user
        
        Returns:
            Either if the game is over or a valid movement for the user to 
            traverse
        """
        ansFlag = True
        once = False
        if errorChoice == "nesw":
            if once == False:
                print(self.neswError)
                once = True
            answer = input(self.playInput).lower()
        else:
            if once == False:
                print(self.invalidDirection)
                once = True
            answer = input(self.playInput).lower()
        
        while(ansFlag == True):
            if answer == "no":
                self.play = False 
                ansFlag = False
                print("goodbye!")
                self.gameEnd = True
                break
            elif answer == "yes":
                na = input(self.prompt).lower()
                if na in self.neswCheck:
                    ansFlag = False
                    return na
                else:
                    print("invalid answer, please try again.")
                    answer = input(self.playInput).lower()
            else: 
                    print("invalid answer, please try again.")
                    answer = input(self.playInput).lower()

#c = Map()
#c.mapDriver()
