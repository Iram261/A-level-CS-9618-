global DataStored #integer
global NumberItems #integer 20 items
DataStored=[]
def Initialise():
    global DataStored 
    global NumberItems
    Valid = False
    while (Valid == False):
        NumberItems= int(input("How many numbers will you enter?")) #loop until < 20
        if NumberItems>0  and NumberItems<21:
            Valid = True
    for Count in range(0,NumberItems):
        DataStored.append(int(input("Enter number")))



def BubbleSort():
    global DataStored 
    global NumberItems
    for Count in range(0,NumberItems):
        for Count2 in range(0,NumberItems-1):
            if DataStored[Count2]>DataStored[Count2 +1]:
                DataStored[Count2],DataStored[Count2 +1]=DataStored[Count2 +1],DataStored[Count2]
    


def BinarySearch(DataToFind):
    global DataStored 
    global NumberItems
    First=0
    Last=NumberItems
    while (First<=Last):
        MidValue= int((First+Last)/2)
        if DataToFind == DataStored[MidValue]:
            return MidValue
        if DataToFind < DataStored[MidValue]:
            Last= MidValue-1
        else:
            First= MidValue+1
    return -1

NumberItems=0
Initialise()
print(DataStored)
BubbleSort()
print(DataStored)
Search= int(input("Enter a number to find"))
print(BinarySearch(Search))



    
            
    




        
        
            
        
    

