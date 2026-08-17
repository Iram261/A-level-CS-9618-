
class Animal:
    def __init__(self,pName,pSound,pSize,pIntelligence):
        self.Name=pName #string
        self.Sound=pSound #string
        self.Size=pSize #integer
        self.Intelligence=pIntelligence #integer
    def Description(self):
        Message= "The animal's name is "+ self.Name+", it makes a "+self.Sound+", its size is "+str(self.Size)+" and its intelligence level is "+str(self.Intelligence)
        return Message
class Parrot(Animal):
    def __init__(self,pName,pSound,pSize,pIntelligence,pWingSpan,pNumberWords):
        super().__init__(pName,pSound,pSize,pIntelligence)
        self.WingSpan=pWingSpan #integer
        self.NumberWords=pNumberWords #integer
    def ChangeNumberWords(self,Change):
        self.NumberWords=self.NumberWords+ Change
    def Description(self):
        Message= "The animal's name is "+ self.Name+", it makes a "+self.Sound+", its size is "+str(self.Size)+" and its intelligence level is "+str(self.Intelligence)+". It has a wingspan of "+str(self.WingSpan)+"cm and can say "+str(self.NumberWords)+ " words."
        return Message
class Wolf(Animal):
    def __init__(self,pName,pSound,pSize,pIntelligence,pTerritorySize):
       super().__init__(pName,pSound,pSize,pIntelligence)
       self.TerritorySize=pTerritorySize #integer
    def SetTerritorySize(self,Change):
        self.TerritorySize=self.TerritorySize+ Change
    def Description(self):
        Message= "The animal's name is "+ self.Name+", it makes a "+self.Sound+", its size is "+str(self.Size)+" and its intelligence level is "+str(self.Intelligence)+". Its territory is "+ str(self.TerritorySize)+" square miles."
        return Message

Animal1=Parrot("Chewie","Squawk",1,10,30,29)
Animal2=Wolf("Nighteyes","Howl",8,7,100)
Animal3=Animal("Copper","Neigh",10,6)
Animal2.SetTerritorySize(-20)
Animal1.ChangeNumberWords(2)
print(Animal1.Description())
print(Animal2.Description())
print(Animal3.Description())

