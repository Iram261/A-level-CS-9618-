class Bird:
    def __init__(self,pDistancePerHour,pSpecies):
        self.__Species=pSpecies #string
        self.__DistancePerHour=pDistancePerHour #real
        self.__XPosition=500.0 #real
        self.__YPosition=500.0 #real
    def GetSpecies(self):
        return self.__Species
    def GetPosition(self):
        ReturnValue= "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)
        return ReturnValue
    def Move(self,Direction,MinsFlying):
        if Direction == "E":
            self.__XPosition=self.__XPosition+ ((self.__DistancePerHour/60)*MinsFlying)
        elif Direction == "W":
            self.__XPosition=self.__XPosition- ((self.__DistancePerHour/60)*MinsFlying)
        elif Direction == "N":
            self.__YPosition=self.__YPosition+ ((self.__DistancePerHour/60)*MinsFlying)
        elif Direction == "S":
            self.__YPosition=self.__YPosition- ((self.__DistancePerHour/60)*MinsFlying)

FirstBird= Bird(71.0,"Cocktiel")
SecondBird= Bird(56.0,"Macaw")

Choice=0
while Choice != 1 and Choice != 2:
    print("Which bird do you want to move")
    print("Enter 1 for", FirstBird.GetSpecies(), "is currently at", FirstBird.GetPosition())
    Choice= -1
    print("Enter 2 for", SecondBird.GetSpecies(), "is currently at", SecondBird.GetPosition())
    Choice = int(input())
Time = -1
while Time <0 or Time > 500:
    Time= int(input("To the nearest minute how long has the bird been flying"))
Valid = False
while Valid == False:
    Valid = True
    Direction= input("Which direction has the bird been flying, North, South, East or West ").upper()
    if Direction=="NORTH" or Direction== "N":
        if Choice==1:
            FirstBird.Move("N",Time)
        else:
            SecondBird.Move("N",Time)
    elif Direction=="SOUTH" or Direction== "S":
        if Choice==1:
            FirstBird.Move("S",Time)
        else:
            SecondBird.Move("S",Time)
    elif Direction=="EAST" or Direction== "E":
        if Choice==1:
            FirstBird.Move("E",Time)
        else:
            SecondBird.Move("E",Time)
    elif Direction=="WEST" or Direction== "W":
        if Choice==1:
            FirstBird.Move("W",Time)
        else:
            SecondBird.Move("W",Time)
    else:
        Valid = False
print(FirstBird.GetSpecies(), "is currently at", FirstBird.GetPosition())
print(SecondBird.GetSpecies(), "is currently at", SecondBird.GetPosition())

        
        
            
            
        
    
    



        
