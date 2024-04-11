import json
import random
"""Functionality check-list for map
-building rooms
-linking/pointing to appropriate rooms
-sorting out move limitations 
-when move specified correct room is applied
-add non square/rectangle rooms
-add the items to each of the rooms after functionality for such has been 
created
"""
class Map:
    def __init__(self, choice):
        self.choice = choice
        self.prompt = "Which direction would you like to go? "
        self.invalidDirection = "invalid choice, please choose another directon"
        self.prompt = "Which direction would you like to go? "
        self.neswError = "please choose a movement of nesw" #are we going to tell them what map theyre on?
        
        self.neswCheck = ["n", "s", "e", "w"]
        #item and puzzle random and flag to say they already did it

    def neswSetter(self, roomLimit):
        self.nesw = roomLimit

    def mapDriver(self):
        playInput = "would you like to continue? "

        with open ("rooms.json", "r", encoding= "utf-8") as f:
            map = json.load(f)
        play = True

        #picks a random map
        randomMap = random.choice(list(map))
        playRoom = map[randomMap]

        #picks random room in map
        randomRoom= str(random.randint(1, len(map[randomMap])))

        #game start
        currentRoom = playRoom[randomRoom]
        current = currentRoom["current"]
        print(self.status(current))
        userInput = input(self.prompt)

        if userInput not in currentRoom:
            self.neswErrorMethod()

        if userInput not in self.neswCheck:
            self.neswErrorMethod()
            answer = input(playInput)
            if answer == "no":
                    play = False    
        movement = currentRoom[userInput]
        
        while(play == True):
            previous = currentRoom["current"]
            if userInput not in self.neswCheck:
                self.neswErrorMethod()
                answer = input(playInput)
                if answer == "no":
                    play = False
                    break
                else:
                    currentRoom = playRoom[previous]
                    current = currentRoom["current"]

            if movement == "invalid movement":
                self.invalidMovementMethod()
                answer = input(playInput)
                
                if answer == "no":
                    play = False
                    break
                else:
                    currentRoom = playRoom[previous]
                    current = currentRoom["current"]

            if movement != "invalid movement":
                currentRoom = playRoom[movement]
                current = currentRoom["current"]

            print(self.status(current))
            userInput = input(self.prompt)

            if userInput not in currentRoom:
                self.neswErrorMethod()
                answer = input(playInput)
                if answer == "no":
                    play = False
                    break
            movement = currentRoom[userInput]

            
    def __repr__(self) -> str:
        return self.choice
    
    def status(self, cr):
        return f"you are currently in room {cr}"
    
    def invalidMovementMethod(self):
        print(self.invalidDirection)
        

    def neswErrorMethod(self):
        print(self.neswError)


        
   
c = Map("3x3")
c.mapDriver()

