class Queue:
    def __init__(self):
        self.QueueArray=[]
        for x in range(0,100):
            self.QueueArray.append(-1)
        self.HeadPointer=-1 #integer
        self.TailPointer=0 #integer
        
TheQueue= Queue()

def Enqueue(AQueue, TheData):
    if AQueue.HeadPointer == -1:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.HeadPointer = 0
        AQueue.TailPointer += 1
        return 1
    elif AQueue.TailPointer >99:
        return -1
    else:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.TailPointer = AQueue.TailPointer + 1
        return 1

def ReturnAllData(TheQueue):
    Temp = ""
    for X in range(TheQueue.HeadPointer,TheQueue.TailPointer):
        Temp= Temp+ str(TheQueue.QueueArray[X])+ " "
    return Temp

def Dequeue(AQueue):
    if AQueue.HeadPointer == 100 or AQueue.HeadPointer == -1 or AQueue.HeadPointer == AQueue.TailPointer:
        return -1
    else:
        Temp= AQueue.QueueArray[AQueue.HeadPointer]
        AQueue.HeadPointer= AQueue.HeadPointer + 1
        return Temp

for x in range(0,10):
    Continue = True
    while (Continue == True):
        DataInput= int(input("Enter an integer that is 0 or more"))
        if DataInput > -1:
            Continue = False
    ReturnValue= Enqueue(TheQueue, DataInput)
    if (ReturnValue == -1):
        print("Queue full")
    else:
        print("Item inserted")

print(ReturnAllData(TheQueue))

ReturnValue= Dequeue(TheQueue)
if ReturnValue == -1:
    print("Queue empty")
else:
    print(ReturnValue, "is returned")
ReturnValue= Dequeue(TheQueue)
if ReturnValue == -1:
    print("Queue empty")
else:
    print(ReturnValue, "is returned")
print(ReturnAllData(TheQueue))



    






            

        

        
