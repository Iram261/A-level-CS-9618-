class Character:
    #self.__XPosition integer
    #self.__YPosition integer
    #self.__Name string
    def __init__(self, XPositionP, YPositionP, NameP):
        self.__XPosition= XPositionP
        self.__YPosition= YPositionP
        self.__Name= NameP
    def GetXPosition(self):
        return self.__XPosition
    def GetYPosition(self):
        return self.__YPosition
    def SetXPosition(self, Value):
        self.__XPosition= self.__XPosition + Value
        if (self.__XPosition > 10000):
            self.__XPosition= 10000
        elif (self.__XPosition < 0):
            self.__XPosition= 0
    def SetYPosition(self, Value):
        self.__YPosition= self.__YPosition + Value
        if (self.__YPosition > 10000):
            self.__YPosition= 10000
        elif (self.__YPosition < 0):
            self.__YPosition= 0
    def Move(self,Direction):
        if (Direction == "up"):
            self.SetYPosition(10)
        elif (Direction == "down"):
            self.SetYPosition(-10)
        elif (Direction == "right"):
            self.SetXPosition(10)
        else:
            self.SetXPosition(-10)

Jack = Character(50, 50, "Jack")

class BikeCharacter(Character):
    def __init__(self, XPositionP, YPositionP, NameP):
        super().__init__(XPositionP, YPositionP, NameP)
    def Move(self,Direction):
        if (Direction == "up"):
            super().SetYPosition(20)
        elif (Direction == "down"):
            super().SetYPosition(-20)
        elif (Direction == "right"):
            super().SetXPosition(20)
        else:
            super().SetXPosition(-20)

Karla = BikeCharacter(100, 50, "Karla")

CharacterToMove = input("Would you like to move Jack or Karla?").lower()
while CharacterToMove != "jack" and CharacterToMove != "karla":
    CharacterToMove= input("Invalid try again").lower()
Direction = input("Which direction? Up, down, left or right?")
while Direction != "up" and Direction != "down" and Direction != "left" and Direction != "right":
    Direction = input("Invalid try again")
if CharacterToMove == "jack":
    Jack.Move(Direction)
    print("Jack's new X position is X =", Jack.GetXPosition(), "Y=", Jack.GetYPosition())
else:
    Karla.Move(Direction)
    print("Karla's new X position is X =", Karla.GetXPosition(), "Y=", Karla.GetYPosition())

    
    
    
    

    
    
            
            
    
            
            
        
    
