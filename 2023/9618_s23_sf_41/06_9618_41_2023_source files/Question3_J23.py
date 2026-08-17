global Animal
global Colour
Animal = [] #20 elements
Colour = [] #10 elements
global AnimalTopPointer
global ColourTopPointer
AnimalTopPointer = 0
ColourTopPointer = 0
def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer +=1
        return True

def PopAnimal():
    global Animal
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -=1
        return ReturnData

def PushColour(DataToPush):
    global Colour
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer +=1
        return True

def PopColour():
    global Colour
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -=1
        return ReturnData

def ReadData():
    try:
        global Colour
        global ColourTopPointer
        global Animal
        global AnimalTopPointer
        AnimalFile = open("AnimalData.txt",'r')
        for Line in AnimalFile:
            PushAnimal(Line.strip())
        AnimalFile.close()
        ColourFile = open("ColourData.txt",'r')
        for Line in ColourFile:
            PushColour(Line.strip())
        ColourFile.close()
    except IOError:
        print("Could not find file")

def OutputItem():
    global Colour
    global ColourTopPointer
    global Animal
    global AnimalTopPointer
    ColourReturned = PopColour()
    AnimalReturned = PopAnimal()
    if ColourReturned == "":
        print("No colour")
        PushAnimal(AnimalReturned)
    else:
        if AnimalReturned == "":
            print("No animal")
            PushColour(ColourReturned)
        else:
            print(ColourReturned, AnimalReturned)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
            
            
        
    







            
            
        
    
        
