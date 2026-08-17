global arrayData

def linearSearch(searchValue):
    global arrayData
    for x in range(0, 10):
        if arrayData[x] == searchValue:
            return True
    return False

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
searchValue = int(input("Enter the number to search for "))
returnValue = linearSearch(searchValue)
if returnValue == True:
    print("It was found")
else:
    print("It was not found")

def bubbleSort():
    global arrayData
    for x in range(0,10):
        for y in range(0,9):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp




