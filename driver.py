
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

    def __repr__(self) -> str:
        return self.choice

class Rooms(Map):
    def __init__(self, choice):
        self.currentRoom = 0
        self.status(self.currentRoom)
        super().__init__(choice)
        

    def selection(self):
        if self.super.choice == "3x3":
           self.threeByThree()
           self.status(self.currentRoom)
           
        
    def threeByThree(self):
        if "1":
            self.neswSetter([False, True, True, False])
            self.currentRoom = 1
            self.status(self.currentRoom)
            
        elif "2":
            self.neswSetter([False, True, True, True])
            self.currentRoom = 2
            
    def oneByFive(self):
        None
    
    def fourByOne(self):
        None

    def status(self, cr):
        return f"you are currently in room {cr}"

   
c = Rooms("1")
print(c.threeByThree())