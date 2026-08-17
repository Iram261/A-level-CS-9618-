#RECURSIVE?
import random
TheArray=[]
TheArray= random.sample(range(0,101),20)
def PrintArray(DataArray):
    Output=""
    for Item in DataArray:
        Output=Output+ str(Item) + " "
    print(Output)
def BubbleSort(DataArray):
    Swap= True
    while  Swap== True:
        Swap= False
        for y in range(0,len(DataArray)-1):
            if DataArray[y]>DataArray[y+1]:
                DataArray[y],DataArray[y+1]=DataArray[y+1],DataArray[y]
                Swap= True
    return DataArray

PrintArray(TheArray)
SortedArray=BubbleSort(TheArray)
print("Sorted")
PrintArray(SortedArray)

def RecursiveBinarySearch(DataArray,Lower,Upper,DataToFind):
    if Upper>=Lower:
        Middle= Lower+ (Upper-Lower)//2
        if DataArray[Middle] == DataToFind:
            return Middle
        elif DataArray[Middle] > DataToFind:
            return RecursiveBinarySearch(DataArray,Lower,Middle-1,DataToFind)
        else:
            return RecursiveBinarySearch(DataArray,Middle+1,Upper,DataToFind)
    else:
        return -1

DataToFind= int(input("Enter the number to find "))
Location= RecursiveBinarySearch(SortedArray,0,19,DataToFind)
if Location == -1 :
    print("Not found")
else:
    print("Found at position", Location)
    
    


    
            



                
        
    
        
    
