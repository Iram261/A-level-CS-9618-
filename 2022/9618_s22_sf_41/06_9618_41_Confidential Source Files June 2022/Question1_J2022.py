global FileData
FileData = [[""]*2 for i in range(11)] #string

def ReadHighScores():
    FileName = "HighScore.txt"
    try:
        File = open(FileName, 'r')
        for x in range(0,10):
            FileData[x][0] = File.readline()[:3]
            FileData[x][1] = File.readline().strip()
        File.close()
    except IOError:
        print("Could not read file")

def OutputHighScores():
    for x in range(0,11):
        Output = FileData[x][0] + " " + FileData[x][1]
        print(Output)



def Arrange(Username, Score):
    for x in range(0, 10):
        if Score > int(FileData[x][1]):
            Temp1 = FileData[x][0]
            Temp2 = FileData[x][1]
            FileData[x][0] = Username
            FileData[x][1] = str(Score)
            Count = x + 1
            while Count < 10:
                Second1 = FileData[Count][0]
                Second2 = FileData[Count][1]
                FileData[Count][0] = Temp1
                FileData[Count][1] = Temp2
                Temp1 = Second1
                Temp2 = Second2
                Count = Count + 1
            break

print("before")
ReadHighScores()
OutputHighScores()

Username = "ABCD"
while len(Username) != 3:
    Username = input("Enter your Username")

Score  = -1
while Score < 1 or Score > 100000:
    Score = int(input("Enter score"))

Arrange(Username, Score)
print("after")
OutputHighScores()

def WriteTopTen():
    Filename = "NewHighScore.txt"
    try:
        File = open(Filename,'w')
        for x in range(0,10):
            File.write(str(FileData[x][0]) + '\n')
            File.write(str(FileData[x][1]) + '\n')
        File.close()
    except:
        print("Could not write to file")


        
            
                
    
        
        
    
    
        
        
