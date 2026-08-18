DataArray=[0,3,4,56,67,44,43,32,31,345,45,6,54,1]

def InsertionSort(DataArray):
    if (len(DataArray))<=1:
        return DataArray
    for X in range(1,len(DataArray)):
        CurrentValue=DataArray[X]
        Y=X-1
        while Y>=0 and CurrentValue<DataArray[Y]:
            DataArray[Y+1]=DataArray[Y]
            Y=Y-1
        DataArray[Y+1]=CurrentValue
    return DataArray

def OutputArray(DataArray):
    Output=""
    for Item in DataArray:
        Output=Output+str(Item)+" "
    print(Output)

def Search(DataArray,ItemToFind):
    Low=0
    High= len(DataArray)-1
    Middle=0
    while Low<=High:
        Middle=(High+Low)//2
        if DataArray[Middle]<ItemToFind:
            Low=Middle+1
        elif DataArray[Middle]>ItemToFind:
            High=Middle-1
        else:
            return Middle
    return -1

OutputArray(DataArray)
DataArray=InsertionSort(DataArray)
OutputArray(DataArray)

Location=Search(DataArray,0)
if Location == -1:
    print("Data not found")
else:
    print("Data found at", Location)
Location=Search(DataArray,345)
if Location == -1:
    print("Data not found")
else:
    print("Data found at", Location)
Location=Search(DataArray,67)
if Location == -1:
    print("Data not found")
else:
    print("Data found at", Location)
Location=Search(DataArray,2)
if Location == -1:
    print("Data not found")
else:
    print("Data found at", Location)



            
            
            
        

        
        
    
            
        
