
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
        self.invalidDirection = "invalid choice, please choose another directon"
        self.prompt = "Which direction would you like to go? "
        self.neswError = "please choose a movement of nesw" #are we going to tell them what map theyre on?
        

    def selection(self):
        if self.super.choice == "3x3":
           self.threeByThree("5")
           self.status(self.currentRoom)
    
    #optimize later? my eyes hurt staring at this shit
    def threeByThree(self, choice):
        #default starting room is 5
        if self.defaultVal == True:
            choice = 5
            self.defaultVal = False
        if choice == 5:
            self.currentRoom = 5
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 
            p5 = {"n": 2, "e": 6, "s": 8, "w": 4}

            if userInput not in p5:
                   self.threeByThree(self.neswErrorMethod())

            choice = p5.get(userInput)
            if choice == "invalid movement":
                self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)


        if choice == 1:
            p1 = {"n": 1, "e": 2, "s": 4, "w": "invalid movement"} 
            self.currentRoom = 1
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p1:
                 self.threeByThree(self.neswErrorMethod())

            choice = p1.get(userInput)
            if choice == "invalid movement":
                 self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)

        elif choice == 2:
            p2 = {"n": "invalid movement", "e": 3, "s": 5, "w": 1}
            self.currentRoom = 2
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p2:
                 self.threeByThree(self.neswErrorMethod())
            choice = p2.get(userInput)

            if choice == "invalid movement":
                 self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)

        elif choice == 3:
            p3 = {"n": "invalid movement", "e": "invalid movement", 
                  "s": 6, "w": 2}
            self.currentRoom = 3
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p3:
                 self.threeByThree(self.neswErrorMethod())

            choice = p3.get(userInput)
            if choice == "invalid movement":
                self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)

        elif choice == 4:
            p4 = {"n": 1, "e": 5, "s": 6, "w": "invalid movement"}
            self.currentRoom = 4
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p4:
                self.threeByThree(self.neswErrorMethod())

            choice = p4.get(userInput)
            if choice == "invalid movement":
                 self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)

        elif choice == 6:
            p6 = {"n": 3, "e": "invalid movement", "s": 9, "w": 5}
            self.currentRoom = 6
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p6:
               self.threeByThree(self.neswErrorMethod())

            choice = p6.get(userInput)
            if choice == "invalid movement":
                 self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)

        elif choice == 7:
            p7 = {"n": 4, "e": 8, "s": "invalid movement", 
                  "w": "invalid movement"}
            self.currentRoom = 7
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p7:
                 self.threeByThree(self.neswErrorMethod())

            choice = p7.get(userInput)
            if choice == "invalid movement":
                 self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)

        elif choice == 8:
            p8 = {"n": 5, "e": 9, "s": "invalid movement", "w": 7}
            self.currentRoom = 8
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p8:
                self.threeByThree(self.neswErrorMethod())

            choice = p8.get(userInput)
            if choice == "invalid movement":
                 self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)

        elif choice == 9:
            p9 = {"n": 6, "e": "invalid movement", 
                  "s": "invalid movement", "w": 8}
            self.currentRoom = 9
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p9:
                 self.threeByThree(self.neswErrorMethod())

            choice = p9.get(userInput)
            if choice == "invalid movement":
                 self.threeByThree(self.invalidMovementMethod())

            self.threeByThree(choice)

    def invalidMovementMethod(self):
        print(self.invalidDirection)
        return self.currentRoom
        

    def neswErrorMethod(self):
        print(self.neswError)
        return self.currentRoom
        
        
    def oneByFive(self, choice):
        if choice == 1:
            p1 = {"n": "invalid movement", "e": "invalid movement", "s": 2,
                   "w": "invalid movement"} 
            self.currentRoom = 1
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p1:
                self.oneByFive(self.neswErrorMethod())
                
            choice = p1.get(userInput)
            if choice == "invalid movement":
                self.oneByFive(self.invalidMovementMethod())

            self.oneByFive(choice)

        elif choice == 2:
            p2 = {"n": 1, "e": "invalid movement", "s": 3,
                   "w": "invalid movement"}
            self.currentRoom = 2
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p2:
                self.oneByFive(self.neswErrorMethod())
            choice = p2.get(userInput)

            if choice == "invalid movement":
                self.oneByFive(self.invalidMovementMethod())

            self.oneByFive(choice)

        elif choice == 3:
            p3 = {"n": 2, "e": "invalid movement", 
                  "s": 4, "w": "invalid movement"}
            self.currentRoom = 3
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p3:
                self.oneByFive(self.neswErrorMethod())

            choice = p3.get(userInput)
            if choice == "invalid movement":
                self.oneByFive(self.invalidMovementMethod())

            self.oneByFive(choice)

        elif choice == 4:
            p4 = {"n": 3, "e": "invalid movement", 
                  "s": "invalid movement", "w": "invalid movement"}
            self.currentRoom = 4
            print(self.status(self.currentRoom))
            userInput = input(self.prompt) 

            if userInput not in p4:
                self.oneByFive(self.neswErrorMethod())

            choice = p4.get(userInput)
            if choice == "invalid movement":
                self.oneByFive(self.invalidMovementMethod())

            self.oneByFive(choice)
    
    def fourByOne(self):
        None

    def status(self, cr):
        return f"you are currently in room {cr}"

   
c = Rooms("1")
c.oneByFive(1)
