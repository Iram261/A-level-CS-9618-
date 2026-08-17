def ReadData():
    Colours=[""]*45
    Count=0
    try:
        File= open("Data.txt")
        for Line in File:
            if Count<45:
                Colours[Count]= Line.strip()
                Count += 1
        File.close()
    except:
        print("No file found")
    return Colours

def FormatArray(DataArray):
    OutputText=""
    for x in range(0,45):
        OutputText= OutputText+ DataArray[x] + " "
    return OutputText



def ComapareStrings(First,Second):
    Count= 0
    while True:
        if First[Count] < Second[Count]:
            return 1
        elif First[Count] > Second[Count]:
            return 2
        else:
            Count = Count + 1

def Bubble(DataArray):
    ArrayLength= len(DataArray)
    for x in range(ArrayLength-1):
        for y in range(0,ArrayLength-x-1):
            Result= ComapareStrings(DataArray[y],DataArray[y+1])
            if Result == 2:
                DataArray[y],DataArray[y+1]=DataArray[y+1],DataArray[y]
    return DataArray

Colours= ReadData() #string array
print(FormatArray(Colours))
BubbleSorted= Bubble(Colours)
print(FormatArray(BubbleSorted))









        


        
