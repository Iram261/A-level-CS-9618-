QueueArray = ['','','','','','','','','',''] #string
HeadPointer = 0 #integer
TailPointer = 0 #integer
NumberItems = 0 #integer

def Enqueue(DataToAdd): ###'byval & by ref""??
    global QueueArray 
    global HeadPointer
    global TailPointer
    global NumberItems
    if NumberItems == 10:
        return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    NumberItems = NumberItems + 1
    return True

def Dequeue():
    global QueueArray 
    global HeadPointer
    global TailPointer
    global NumberItems
    if NumberItems == 0:
        return "FALSE"
    else:
        ReturnValue = QueueArray[HeadPointer]
        HeadPointer = HeadPointer + 1
        if HeadPointer > 9:
            HeadPointer = 0
        NumberItems = NumberItems - 1
        return ReturnValue

for x in range(0,11):
    InputString = input("Enter a string")
    ReturnValue = Enqueue(InputString)
    if ReturnValue == True:
        print("Successful")
    else:
        print("Unsuccessful")

ReturnValue = Dequeue()
print(ReturnValue)
ReturnValue = Dequeue()
print(ReturnValue)
        


        

        
    
    

