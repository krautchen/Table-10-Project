
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
            choice = 5
            self.defaultVal = False
        if choice == 5:
            self.currentRoom = 5
            print(self.status(self.currentRoom))
            userInput = input("Which direction would you like to go? ") 
            p5 = {"n": 2, "e": 6, "s": 8, "w": 4}
            choice = p5.get(userInput)

        if choice == 1:
            p1 = {"n": 1, "e": 2, "s": 4, "w": None} #p1 = {"n": 1, "e": 2, "s": 4, "w": 1}
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

        elif choice == 3:
            p3 = {"n": None, "e": None, "s": 6, "w": 2}
            self.currentRoom = 3
            print(self.status(self.currentRoom))
            userInput = input("Which direction would you like to go? ") 
            choice = p3.get(userInput)
            self.threeByThree(choice)

        elif choice == 4:
            p4 = {"n": 1, "e": 5, "s": 6, "w": None}
            self.currentRoom = 4
            print(self.status(self.currentRoom))
            userInput = input("Which direction would you like to go? ") 
            choice = p4.get(userInput)
            self.threeByThree(choice)

        elif choice == 6:
            p6 = {"n": 3, "e": None, "s": 9, "w": 5}
            self.currentRoom = 6
            print(self.status(self.currentRoom))
            userInput = input("Which direction would you like to go? ") 
            choice = p6.get(userInput)
            self.threeByThree(choice)

        elif choice == 7:
            p7 = {"n": 4, "e": 8, "s": None, "w": None}
            self.currentRoom = 7
            print(self.status(self.currentRoom))
            userInput = input("Which direction would you like to go? ") 
            choice = p7.get(userInput)
            self.threeByThree(choice)

        elif choice == 8:
            p2 = {"n": 5, "e": 9, "s": None, "w": 7}
            self.currentRoom = 8
            print(self.status(self.currentRoom))
            userInput = input("Which direction would you like to go? ") 
            choice = p2.get(userInput)
            self.threeByThree(choice)

        elif choice == 9:
            p2 = {"n": 6, "e": None, "s": None, "w": 8}
            self.currentRoom = 9
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
