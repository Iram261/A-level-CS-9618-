Queue=[] #integer 50 elements
HeadPointer= -1
TailPointer= -1
#main
HeadPointer= -1
TailPointer= -1
for x in range(50):
    Queue.append(-1)

def Enqueue(Data):
    global Queue
    global HeadPointer
    global TailPointer
    if TailPointer<49:
        TailPointer=TailPointer+1
        Queue[TailPointer]=Data
        if HeadPointer== -1:
            HeadPointer= 0
        return True
    else:
        return False
def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    if HeadPointer>-1 and HeadPointer<=TailPointer:
        ReturnValue=Queue[HeadPointer]
        HeadPointer=HeadPointer+1
        return ReturnValue
    else:
        return -1
def CreateQueue():
    try:
        File=open("QueueData.txt")
        for Line in File:
            ReturnValue=Enqueue(int(Line))
            if ReturnValue==False:
                print("Queue full")
                break
        File.close()
    except:
        print("Cannot open or read file")

CreateQueue()
Total=0
ReturnValue=0
while ReturnValue>-1:
    ReturnValue=Dequeue()
    if ReturnValue != -1:
        Total=Total+ReturnValue
print("The total is", Total)


                
    
    
        
        


