#RECURSIVE
def RecursiveCount(DataToFind,ArrayCopy,NumberElements):
    if NumberElements > 0:
        NewArray= ArrayCopy[1:]
        if ArrayCopy[0] == DataToFind:
            return 1 + RecursiveCount(DataToFind,NewArray,NumberElements-1)
        else:
            return RecursiveCount(DataToFind,NewArray,NumberElements-1)
    else:
        return 0

MyArray = [0,5,1,2,5,9,9,6,5,0]
print(RecursiveCount(0,MyArray,10))


def SplitData(DataString):
    SplitDataArray = []
    Count = 0
    for x in range(4):
        TempString = ""
        try:
            Character = DataString[Count]
            while Character != ";":
                TempString = TempString + Character
                Count += 1
                Character = DataString[Count]
            SplitDataArray.append(TempString)
        except:
            print("No more characters")
        Count += 1
    return SplitDataArray

Code = "x=0;y=1;x=x+y;y++;"
SplitDataArray = SplitData(Code)
for x in range(4):
    print(SplitDataArray[x])
    

            
                
                
                
                
                
                
    
    






    
    
        
            
        
