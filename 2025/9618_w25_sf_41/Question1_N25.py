Stack=[None for x in range(30)]
TopOfStack= -1
def Push(DataToPush):
    global Stack
    global TopOfStack
    if TopOfStack<29:
        TopOfStack=TopOfStack+1
        Stack[TopOfStack]=DataToPush
        return True
    else:
        return False

def Pop():
    global Stack
    global TopOfStack
    if TopOfStack == -1:
        return -999
    else:
        DataReturn=Stack[TopOfStack]
        TopOfStack=TopOfStack-1
        return DataReturn

def FindValues():
    Highest=Pop()
    Lowest=Highest
    ReturnValue=Lowest
    while (ReturnValue != -999):
        if ReturnValue>Highest:
            Highest=ReturnValue
        if ReturnValue<Lowest:
            Lowest=ReturnValue
        ReturnValue=Pop()
    print("The highest value is", Highest, "and the lowest value is", Lowest)

import random
for x in range(40):
    Pushed=Push(random.randint(0,1000))
    if Pushed== False:
        print("Stack full")
        break

FindValues()
        
    
    
    
        
        
    

