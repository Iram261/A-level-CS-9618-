
class Train():
    def __init__(self,pNumber,pRoute):
        self.__TrainIDNumber=pNumber #string
        self.__Route=pRoute #integer
    def GetTrainIDNumber(self):
        return self.__TrainIDNumber
    def GetRoute(self):
        return self.__Route

class Station():
    def __init__(self,pID,pNumberOfPlatforms):
        self.__StationID=pID #string
        self.__NumberPlatforms=pNumberOfPlatforms #integer
        self.__Trains=[] #train 10 elements
        self.__NumberTrains=0 #integer
    def AddTrain(self,NewTrain):
        if self.__NumberTrains >= self.__NumberPlatforms:
            return False
        else:
          self.__Trains.append(NewTrain)
          self.__NumberTrains +=1
          return True
    def GetTrains(self):
        if  self.__NumberTrains==0:
            return "There are no trains"
        OutputLine= "The trains at station "+self.__StationID+" are: \n"
        for x in range(self.__NumberTrains):
            OutputLine=OutputLine+self.__Trains[x].GetTrainIDNumber()+" on route number "+str(self.__Trains[x].GetRoute())+"\n"
        return OutputLine

FirstTrain=Train("12ADV",134)
SecondTrain=Train("33ART",20)
ThirdTrain=Train("9FKF",3)
FourthTrain=Train("21VBC",24)

SouthStation=Station("STH",2)
NorthStation=Station("NTH",1)

ReturnValue=SouthStation.AddTrain(FirstTrain)
if ReturnValue== False:
    print("Station is full")
ReturnValue=SouthStation.AddTrain(SecondTrain)
if ReturnValue== False:
    print("Station is full")
ReturnValue=SouthStation.AddTrain(ThirdTrain)
if ReturnValue== False:
    print("Station is full")
ReturnValue=NorthStation.AddTrain(FourthTrain)
if ReturnValue== False:
    print("Station is full")
print(SouthStation.GetTrains())
print(NorthStation.GetTrains())



    
            
        
          
          
        
        
    
