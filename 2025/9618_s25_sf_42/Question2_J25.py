
class NewRecord:
    def __init__(self,pKey,pItem1,pItem2):
        self.__Key=pKey #integer
        self.__Item1=pItem1 #integer
        self.__Item2=pItem2 #integer
    def GetKey(self):
        return self.__Key
    def GetItem1(self):
        return self.__Item1
    def GetItem2(self):
        return self.__Item2
HashTable=[]
Spare=[]
def Initialise():
    global HashTable
    global Spare
    for X in range(200):
        HashTable.append(NewRecord(-1,-1,-1))
    for X in range(100):
        Spare.append(NewRecord(-1,-1,-1))
def CalculateHash(Key):
    return Key% 200
def InsertIntoHash(TheRecord):
    global HashTable
    global Spare
    HashValue=CalculateHash(TheRecord.GetKey())
    if HashTable[HashValue].GetKey()== -1:
        HashTable[HashValue]=TheRecord
    else:
        for x in range(100):
            if Spare[x].GetKey()== -1:
                Spare[x]=TheRecord
                break
def CreateHashTable():
    global HashTable
    global Spare
    try:
        File= open("HashData.txt")
        for Line in File:
            Data=Line.strip()
            Data=Line.split(",")
            InsertIntoHash(NewRecord(int(Data[0]),int(Data[1]),int(Data[2])))
        File.close()
    except:
        print("Cannot open file")

def PrintSpare():
    global Spare
    X=0
    while Spare[X].GetKey() != -1:
        print(Spare[X].GetKey())
        X +=1
Initialise()
CreateHashTable()
PrintSpare()
        
    
    
    
    
                
                
                
        
    
        
        
        
        
