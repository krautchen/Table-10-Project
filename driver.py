
"""Functionality check-list for map
-building rooms
-linking/pointing to appropriate rooms
-sorting out move limitations 
-when move specified correct room is applied
-add non square/rectangle rooms

"""
#---------notes for team---------
"""this is a huge fucking mess just give me some time"""

class Map:
    def __init__(self, choice):
        self.nesw = [False, False, False, False]
        self.choice = choice

    def neswSetter(self, roomLimit):
        self.nesw = roomLimit

    def roomChoice(self):
        if "1" == self.choice:
            return "3x3"
        if "2" == self.choice:
            return "1x5"
        if "3" == self.choice:
            return "4x1"
        

class Rooms(Map):
    def __init__(self):
        self.currentRoom = 0
        self.status(self.currentRoom)

    def selection(self):
        if self.roomChoice == "3x3":
           self.threeByThree()

        elif self.roomChoice == "1x5":
           self.oneByFive()

        elif self.roomChoice == "4x1":
           self.fourByOne()
    
        
    def threeByThree(self):
        if "1":
            self.neswSetter([False, True, True, False])
            self.currentRoom = 1
            print(f"you are in room {self.currentRoom}")
        elif "2":
            self.neswSetter([False, True, True, True])
            self.currentRoom = 2
            
    def oneByFive(self):
        None
    
    def fourByOne(self):
        None

        

c = Map("1")
print(c.roomChoice())