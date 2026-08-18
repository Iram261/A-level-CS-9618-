def ReadData():
    DataList=[]
    FileName=input("Enter the filename")
    try:
        File=open(FileName)
        for Line in File:
            DataList.append(Line)
        File.close()
    except:
        print("Cannot open file")
    return DataList

def StoreData(DataToStore,FileName):
    try:
        File=open(FileName,"a+")
        for Item in DataToStore:
            File.write(Item)
            File.write("\n")
        File.close()
    except:
        print("Cannot create or write to file")

def SplitData(DataArray):
    Red=[]
    Green=[]
    Blue=[]
    Orange=[]
    Yellow=[]
    Pink=[]
    for Line in DataArray:
        SplitLine=Line.split(",")
        if SplitLine[1].strip()=="red":
            Red.append(SplitLine[0])
        elif SplitLine[1].strip()=="green":
            Green.append(SplitLine[0])
        elif SplitLine[1].strip()=="blue":
            Blue.append(SplitLine[0])
        elif SplitLine[1].strip()=="orange":
            Orange.append(SplitLine[0])
        elif SplitLine[1].strip()=="yellow":
            Yellow.append(SplitLine[0])
        else:
            Pink.append(SplitLine[0])
    StoreData(Red,"Red.txt")
    StoreData(Green,"Green.txt")
    StoreData(Blue,"Blue.txt")
    StoreData(Orange,"Orange.txt")
    StoreData(Yellow,"Yellow.txt")
    StoreData(Pink,"Pink.txt")

DataFromFile=ReadData()
SplitData(DataFromFile)

    
    
    
    


            
    
            
            
    


            
            
