class TreasureChest:
    def __init__(self, questionP, answerP, pointsP):
        #Private question : String
        #Private answer : Integer
        #Private points : Integer
        self.__question = questionP
        self.__answer = answerP
        self.__points = pointsP
    def getQuestion(self):
        return self.__question
    def checkAnswer(self, answerP):
        if int(self.__answer) == answerP:
            return True
        else:
            return False
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points) // 2
        elif attempts == 3 or attempts == 4:
            return int(self.__points) // 4
        else:
            return 0
        

# arrayTreasure(5) as TreasureChest
arrayTreasure = []
def readData():
    global arrayTreasure
    filename = "TreasureChestData.txt"
    try:
        file = open(filename, "r")
        dataFetched = (file.readline()).strip()
        while (dataFetched != ""):
            question = dataFetched
            answer = (file.readline()).strip()
            points = (file.readline()).strip()
            arrayTreasure.append(TreasureChest(question, answer, points))
            dataFetched = (file.readline()).strip()
        file.close()
    except IOError:
        print("Could not find file")

readData()
choice = int(input("Pick a treasure chest to open"))
if choice > 0 and choice < 6:
    result = False
    attempts = 0
    while result == False:
        print(arrayTreasure[choice-1].getQuestion())
        answer = int(input("Enter the answer: "))
        result = arrayTreasure[choice-1].checkAnswer(answer)
        attempts = attempts + 1
    print(int(arrayTreasure[choice-1].getPoints(attempts)))
        


            
            
            
