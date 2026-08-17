#2D array method
class Record:
    def __init__(self,pKey,pData):
        self.Key=pKey #integer
        self.Data=pData #string

HashTable=[]
def InitialiseHashTable():
    global HashTable
    HashTable=[[Record(-1,"")]*10 for i in range (100)]

def Hash(Key):
    return Key % 100

def InsertData(RecordData):
    global HashTable
    HashValue = Hash(RecordData.Key)
    for X in range(0,10):
        if HashTable[HashValue][X].Key == -1:
            HashTable[HashValue][X] = RecordData
            break

def ReadData():
    global HashTable
    try:
        File=open("HashTableData.txt")
        for Line in File:
            Line=Line.strip()
            Data=Line.split(",")
            InsertData(Record(int(Data[0]),Data[1]))
        File.close()
    except:
        print("File not found")

def GetRecord(Key):
    global HashTable
    HashValue = Hash(Key)
    for X in range(0,10):
        if HashTable[HashValue][X].Key == Key:
            return HashTable[HashValue][X].Data
    return "Not found"

InitialiseHashTable()
ReadData()
for x in range(5):
    Key= int(input("Enter the key field "))
    print(GetRecord(Key))


        
    
    
            
            
    
            
            
    
    
        
