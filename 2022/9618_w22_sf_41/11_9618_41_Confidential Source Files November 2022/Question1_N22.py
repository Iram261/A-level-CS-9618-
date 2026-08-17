global DataArray
DataArray = [0 for I in range(100)]
def ReadFile():
    global DataArray
    try:
        TextFile = "IntegerData.txt"
        File = open(TextFile, 'r')
        for X in range(0,100):
            DataArray[X] = File.readline()
            DataArray[X].rstrip('\n') ###'rstrip()'???
            DataArray[X] = int(DataArray[X]) ###
        File.close()
    except IOError:
        print("Could not find file")

def FindValues():
    global DataArray
    DataToFind = -1
    while (DataToFind < 1 or DataToFind > 100): 
        DataToFind = int(input("Enter a number between 1 and 100"))
    Total = 0
    for X in range(0,100):
        if DataArray[X] == DataToFind:
            Total = Total + 1
    return Total

def BubbleSort():
    global DataArray
    N = 100
    for I in range(N-1):
        for J in range(0, N-I-1):
            if DataArray[J] > DataArray[J+1]:
                DataArray[J], DataArray[J+1] = DataArray[J+1], DataArray[J]
    print(DataArray)

#main
ReadFile()
print("The number appears " + str(FindValues()) + " times")
BubbleSort()
    



            
    

    
            
            
    
