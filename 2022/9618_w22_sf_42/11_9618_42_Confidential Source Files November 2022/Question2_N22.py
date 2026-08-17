class Character:
    #private Name as string
    #private XCoordinate as integer
    #private YCoordinate as integer
    def __init__(self, Namep, Xcoord, Ycoord):
        self.__Name = Namep
        self.__XCoordinate = Xcoord
        self.__YCoordinate = Ycoord
    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange
        
Characters = []
TextFile = "Characters.txt"
try:
    File = open(TextFile , 'r')
    for X in range(0,10):
        Name = File.readline().strip()
        Xcoord = File.readline().strip()
        Ycoord = File.readline().strip()
        TempC = Character(Name, int(Xcoord), int(Ycoord))
        Characters.append(TempC)
    File.close()
except:
    print("File not found")

Position = -1
CharacterName = ""
while (Position == -1):
    CharacterInput = input ("Enter the Character to move").rstrip('\n').lower()
    for Count in range(0, 10):
        Temp = str(Characters[Count].GetName().lower().strip())
        if (Temp == CharacterInput):
            Position = Count


IsValid = False
while (IsValid != True):
    Move = input("Enter A for left, W for up, S for down, or D for right")
    if (Move.upper() == "A"):
        Characters[Position].ChangePosition(-1,0)
        IsValid = True
    elif (Move.upper() == "W"):
        Characters[Position].ChangePosition(0,1)
        IsValid = True
    elif (Move.upper() == "S"):
        Characters[Position].ChangePosition(0,-1)
        IsValid = True
    elif (Move.upper() == "D"):
        Characters[Position].ChangePosition(1,0)
        IsValid = True

CharacterName = Characters[Position].GetName() 
print(CharacterName, " has changed coordinates to X = ", str(Characters[Position].GetX())," Y = ", str(Characters[Position].GetY()))
            
















    
