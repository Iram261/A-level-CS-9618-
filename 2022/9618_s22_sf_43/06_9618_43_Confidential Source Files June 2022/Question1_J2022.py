global FileData
FileData = [[""]*2 for i in range(11)] #string

def ReadHighScores():
    global FileData
    Filename = "HighScore.txt"
    try:
        File = open(Filename,'r')
        for x in range(0,10):
            FileData[x][0] = File.readline()[:3]
            FileData[x][1] = File.readline().strip()
        File.close()
    except:
        print("Could not read file")

def OutputHighScores():
    global FileData
    for x in range(0,11):
        Output = FileData[x][0] + " " + FileData[x][1]
        print(Output)

def Arrange(Username, Score):
    global FileData
    for x in range(0,10):
        if Score > int(FileData[x][1]):
            Temp1 = FileData[x][0]
            Temp2 = FileData[x][1]
            FileData[x][0] = Username
            FileData[x][1] = str(Score)
            Count = x + 1
            while (Count < 10):
                Second1 = FileData[Count][0]
                Second2 = FileData[Count][1]
                FileData[Count][0] = Temp1
                FileData[Count][1] = Temp2
                Temp1 = Second1
                Temp2 = Second2
                Count = Count + 1
            break

print("Before")
ReadHighScores()
OutputHighScores()

Username = "ABCD"
while len(Username) != 3:
    Username = input("Enter your Username")

score = -1
while score < 0 or score > 100000:
    score = int(input("Enter score"))

Arrange(Username, score)
print("After")
OutputHighScores()

def WriteTopTen():
    global FileData
    Filename = "NewHighScore.txt"
    try:
        Filename = open(Filename,'w')
        for x in range(0,10):
            Filename.write(str(FileData[x][0]) + '\n')
            Filename.write(str(FileData[x][1]) + '\n')
        Filename.close()
    except:
        print("Could not write to file")



        
        
    
    
        
               


    



        
        
            
        
