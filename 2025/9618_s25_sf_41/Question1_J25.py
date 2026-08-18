Queue=[-1 for x in range(20)]
HeadPointer=-1
TailPointer=-1
NumberItems=0
def Enqueue(InputData):
    global Queue
    global HeadPointer
    global TailPointer
    global NumberItems
    if NumberItems>=20:
        return False
    if  TailPointer <= -1: 
        HeadPointer=0
        TailPointer=0
        Queue[TailPointer]=InputData
    else:
        TailPointer=TailPointer+1
        if TailPointer==20:
            TailPointer=0
        Queue[TailPointer]=InputData
    NumberItems+=1
    return True

def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    global NumberItems
    if NumberItems<=0: 
        return -1
    else:
        ReturnValue=Queue[HeadPointer]
        HeadPointer+=1
        if HeadPointer>=20:
            HeadPointer=0
        NumberItems-=1
        if NumberItems==0:
           HeadPointer=-1
           TailPointer=-1
        return ReturnValue

for X in range (1,26):
    ReturnValue= Enqueue(X)
    if ReturnValue==True:
        print(X,"Successful")
    else:
        print(X,"Unsuccessful")
NextValue=Dequeue()
print(NextValue)
NextValue=Dequeue()
print(NextValue)
    
    
        
        
        
        
        
    
    
    



    
