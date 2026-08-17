import random ##'random' library

def PrintArray(ArrayData):
    for x in range (0,10):
        for y in range(0,10):
            print(ArrayData[x][y], " ", end='') ###'end'
        print("")
    
#main
ArrayData = [[0]*10 for i in range(10)] # integer
for x in range(0,10):
    for y in range(0,10):
        ArrayData[x][y] = random.randint(1,100)

print("Before")
PrintArray(ArrayData) ##sorting??
ArrayLength = 10
for X in range(0, ArrayLength):
    for Y in range(0, ArrayLength-1):
        for Z in range(0, ArrayLength-Y-1):
            if (ArrayData[X][Z] > ArrayData[X][Z+1]):
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempValue

print("After")
PrintArray(ArrayData)

def BinarySearch(SearchArray, Lower, Upper, SearchValue): ##recursive
    if Upper >= Lower:
        Mid = int((Lower + Upper) / 2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1

FirstCheck = int(input("Enter the number: "))
print(BinarySearch(ArrayData, 0, 9, FirstCheck))
SecondCheck = int(input("Enter the number: "))
print(BinarySearch(ArrayData, 0, 9, SecondCheck))

    
    
                   

