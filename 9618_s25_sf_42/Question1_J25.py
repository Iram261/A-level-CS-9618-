Stack=[]
TopOfStack= -1
#main
for x in range (20):
    Stack.append("-1")
def Push(Data):
    global Stack
    global TopOfStack
    if TopOfStack ==19:
        return -1
    else:
        TopOfStack +=1
        Stack[TopOfStack]=Data
        return 1
def Pop():
    global Stack
    global TopOfStack
    if TopOfStack == -1:
        return "-1"
    else:
        ReturnValue=Stack[TopOfStack]
        TopOfStack -=1
        return ReturnValue
def ReadData(FileName):
    global Stack
    global TopOfStack
    try:
        File=open(FileName)
        for Line in File:
            ReturnValue=Push(Line.strip())
            if ReturnValue== -1:
                print("Stack full")
        File.close()
    except:
        print("Cannot open file")
def Calculate():
    global Stack
    global TopOfStack
    Total=Pop()
    Total=int(Total) 
    Return=0
    LastOperator=""
    Operator= True
    while (Return != "-1"):
        Return=Pop()
        if Operator== False:
            Data = int(Return)
            if LastOperator== "+":
                Total=Total+Data
            elif LastOperator== "-":
                Total=Total-Data
            elif LastOperator== "*":
                Total=Total*Data
            elif LastOperator== "/":
                Total=Total/Data
            elif LastOperator== "^":
                Total=Total**Data
            Operator= True
        else:
            LastOperator=Return
            Operator =False
    return Total

FileName= input("Enter the filename:")
ReadData(FileName)
ReturnValue=Calculate()
print(ReturnValue)


            
                
                
        
    
    



        
    
        
    
    
