
def RecursiveInsertion(IntegerArray,NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray,NumberElements-1)
        LastItem=IntegerArray[NumberElements-1]
        CheckItem=NumberElements-2
    LoopAgain= True
    if CheckItem<0:
        LoopAgain= False
    elif IntegerArray[CheckItem] < LastItem:
        LoopAgain= False
    while (LoopAgain):
        IntegerArray[CheckItem+1]=IntegerArray[CheckItem]
        CheckItem= CheckItem-1
        if CheckItem < 0:
            LoopAgain= False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain= False
    IntegerArray[CheckItem+1]= LastItem
    return IntegerArray

NumberArray=[100,85,644,22,15,8,1]
SortedArray= RecursiveInsertion(NumberArray,len(NumberArray))
print("Recursive")
for x in range(len(SortedArray)):
    print(SortedArray[x])

def IterativeInsertion(IntegerArray,NumberElements):
    CurrentSize=2
    while CurrentSize<= NumberElements:
        LastItem=IntegerArray[CurrentSize-1]
        CheckItem=CurrentSize-2
        LoopAgain= True
        if CheckItem<0:
            LoopAgain= False
        elif IntegerArray[CheckItem] <= LastItem:
            LoopAgain= False
        while (LoopAgain):
            IntegerArray[CheckItem+1]=IntegerArray[CheckItem]
            CheckItem= CheckItem-1
            if CheckItem < 0:
                LoopAgain= False
            elif IntegerArray[CheckItem] <= LastItem:
                LoopAgain= False
        IntegerArray[CheckItem+1]= LastItem
        CurrentSize = CurrentSize +1
    return IntegerArray


NumberArray=[100,85,644,22,15,8,1]
Sorted2Array= IterativeInsertion(NumberArray,len(NumberArray))
print("Iterative")
for x in range(len(Sorted2Array)):
    print(Sorted2Array[x])

def BinarySearch(IntegerArray,First,Last,ToFind):
    if First > Last:
        return -1
    else:
        Middle = int((First+Last)/2)
        if IntegerArray[Middle] == ToFind:
            return Middle
        elif IntegerArray[Middle] > ToFind:
            return BinarySearch(IntegerArray,First,Middle-1,ToFind)
        else:
            return BinarySearch(IntegerArray,Middle+1,Last,ToFind)

Position= BinarySearch(Sorted2Array,0,len(NumberArray)-1,644)
if Position == -1:
    print("Not found")
else:
    print("Index of 644 is" ,Position)
            
    




        
        
        
        
        
