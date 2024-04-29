import json
import random
import sys
from argparse import ArgumentParser
#from puzzle import puzzle as p
"""Functionality check-list for map
-building rooms
-linking/pointing to appropriate rooms
-sorting out move limitations 
-when move specified correct room is applied
-add non square/rectangle rooms
-add the items to each of the rooms after functionality for such has been 
created
-add all the .upper shit to standardize the answers 
-add main function
"""

class Map:
    def __init__(self):
        #self.choice = choice
        self.prompt = "Which direction would you like to go? "
        self.invalidDirection = "invalid choice, please choose another directon"
        self.neswError = "please choose a movement of nesw" 
        self.neswCheck = ["n", "s", "e", "w"]
        self.playInput = "would you like to continue? "
        self.gameEnd = False 
        #item and puzzle random and flag to say they already did it

    def mapDriver(self, filepath):

        with open (filepath, "r", encoding= "utf-8") as f:
            map = json.load(f)
        

        #picks a random map
        randomMap = random.choice(list(map))
        playRoom = map[randomMap]
        #picks random room in map
        randomRoom= str(random.randint(1, len(map[randomMap])))

        #game start
        currentRoom = playRoom[randomRoom]

        #below for testing
        #playRoom = map["1x5"]
        #currentRoom = playRoom["4"]
        current = currentRoom["current"]
        print(self.status(current))
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
                current = currentRoom["current"]

            if movement == "invalid movement" and self.gameEnd == False:
                userInput = self.playPrompt("invalid")
                while(userInput not in currentRoom and self.gameEnd != True):
                    userInput = self.playPrompt("invalid").lower()
                if self.gameEnd != True:
                    movement = currentRoom[userInput]

            if self.gameEnd == True:
                        break
            else:
                currentRoom = playRoom[previous]
                current = currentRoom["current"]

            if movement != "invalid movement":
                currentRoom = playRoom[movement]
                current = currentRoom["current"]
           

            print(self.status(current))
            userInput = input(self.prompt).lower()
            
        
            if userInput not in currentRoom:
                 userInput = self.playPrompt("nesw")
            if self.gameEnd != True:
                movement = currentRoom[userInput]
           
        
    #def __repr__(self) -> str:
        #return self.choice
    
    def status(self, cr):
        return f"you are currently in room {cr}"
        
    def playPrompt(self, errorChoice):
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
                  
def main(filepath):
    m = Map()
    userInput = input("would you like to play? ").lower()
    if userInput == "yes":
        m.mapDriver(filepath)
    else:
        print("goodbye!")
        
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("filepath", help = "path to the map(s)")
    return parser.parse_args(arglist)

if __name__ == "__main__":  
    args = parse_args(sys.argv[1:])
    main(args.filepath)

#c = Map("3x3")
#c.mapDriver()
