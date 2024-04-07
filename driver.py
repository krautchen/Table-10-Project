
"""Functionality check-list for map
-building rooms
-linking/pointing to appropriate rooms
-sorting out move limitations 
-when move specified correct room is applied
-add non square/rectangle rooms
-add the items to each of the rooms after functionality for such has been 
created
"""
#---------notes for team---------
"""this is a huge fucking mess just give me some time"""

class Map:
    def __init__(self, choice):
        self.nesw = [False, False, False, False]
        self.choice = choice

    def neswSetter(self, roomLimit):
        self.nesw = roomLimit

    def __repr__(self) -> str:
        return self.choice

class Rooms(Map):
    def __init__(self, choice):
        self.currentRoom = 0
        self.status(self.currentRoom)
        super().__init__(choice)
        self.defaultVal = True
        

    def selection(self):
        if self.super.choice == "3x3":
           self.threeByThree("5")
           self.status(self.currentRoom)
    
    #optimize later?
    def threeByThree(self, choice):
        #default starting value is 5
        if self.defaultVal == True:
            userInput = input("Which direction would you like to go? ") 
            p5 = {"n": 2, "e": 6, "s": 8, "w": 4}
            choice = p5.get(userInput)
            self.defaultVal = False

        if choice == 1:
            p1 = {"n": None, "e": 2, "s": 4, "w": None}
            self.currentRoom = 1
            print(self.status(self.currentRoom))
            userInput = input("Which direction would you like to go? ") 
            choice = p1.get(userInput)
            self.threeByThree(choice)

        elif choice == 2:
            p2 = {"n": None, "e": 3, "s": 5, "w": 1}
            self.currentRoom = 2
            print(self.status(self.currentRoom))
            userInput = input("Which direction would you like to go? ") 
            choice = p2.get(userInput)
            self.threeByThree(choice)
           
       
            
    def oneByFive(self):
        None
    
    def fourByOne(self):
        None

    def status(self, cr):
        return f"you are currently in room {cr}"

   
c = Rooms("1")
c.threeByThree("1")
