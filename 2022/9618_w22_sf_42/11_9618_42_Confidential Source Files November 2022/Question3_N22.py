global Queue
global HeadPointer
global TailPointer
Queue = [ -1 for I in range(100)] #Integer
HeadPointer = -1
TailPointer = 0
def Enqueue(Data):
    global Queue
    global HeadPointer
    global TailPointer
    if (TailPointer < 100):
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = Data
        TailPointer = TailPointer + 1
        return True
    return False

Success = True
for Count in range(1,21):
    Temp = Enqueue(Count)
    if Temp == False:
        Success = False
if (Success == False):
    print("Unsuccessful")
else:
    print("Successful")

def RecursiveOutput(Start): ####
    if (Start == 0):
        return Queue[Start]
    else:
        return Queue[Start] + RecursiveOutput(Start-1)

print(str(RecursiveOutput(TailPointer-1)))
    


    

            
    
