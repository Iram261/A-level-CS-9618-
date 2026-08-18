global Queue, QueueHead, QueueTail, NumberItems
Queue=[]
for x in range(100):
    Queue.append("")

QueueHead= -1
QueueTail= -1
NumberItems=0

def Enqueue (TheData):
    global Queue, QueueHead, QueueTail, NumberItems
    if QueueHead== -1:
        Queue[0]= TheData
        QueueHead= 0
        QueueTail= 0
        NumberItems +=1
        return True
    elif QueueTail < 99:
        Queue[QueueTail+1]= TheData
        QueueTail +=1
        NumberItems +=1
        return True
    else:
        return False

def Dequeue():
    global Queue, QueueHead, QueueTail, NumberItems
    if NumberItems == 0:
        return False
    else:
        ReturnData= Queue[QueueHead]
        QueueHead += 1
        NumberItems -=1
        return ReturnData

def ReadData():
    try:
        TheFile= open("BinaryData.txt")
        for Line in TheFile:
            ReturnValue= Enqueue(Line.strip())
            if ReturnValue == False:
                break #WHY?
        TheFile.close()
    except:
        print("No file found")


def Compress():
    global NewString #NumberItems NOT DECLARED?
    First=Dequeue()
    NewString= ""
    while NumberItems>0 and First != False: #'First != False' OPTIONAL?
        Count = 1
        NextChar = Dequeue()
        while NextChar == First:
            Count += 1
            First = NextChar
            NextChar = Dequeue()
        NewLine = First + str(Count)
        NewString = NewString + NewLine
        First = NextChar

NewString= ""
Queue=[]
for x in range(100):
    Queue.append("")
QueueHead= -1
QueueTail= -1
NumberItems=0
ReadData()
Compress()
print(NewString)




        
            
            
    
    
    
        
        
    


    
    
        
        
        
        
        
        
        
    
   
   
    
       
