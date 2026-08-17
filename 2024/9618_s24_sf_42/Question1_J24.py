def Play():
    global WordArray
    global NumberWords
    Word= WordArray[0]
    print("The word is: ",Word)
    print("There are",NumberWords-1,"words that can be made with 3 or more letters")
    WordArray[0]=""
    Answer= "yes"
    QuantityFound=0
    while Answer != "no":
        Answer= input("Enter your word or no to stop ").lower()
        Found= False
        if Answer != "no":
            for x in range(0,NumberWords):
                if Answer == WordArray[x]:
                    WordArray[x] = ""
                    QuantityFound= QuantityFound+1
                    print("Correct, you have found", QuantityFound, "words")
                    Found= True
            if Found == False:
                print("Sorry that was incorrect")
    Correct= (QuantityFound/(NumberWords-1))*100
    print("You found", Correct,"%")
    if Correct < 100:
        print("The words you missed are")
        for x in range(0,NumberWords):
            if WordArray[x] != "":
                print(WordArray[x])

def ReadWords(FileName):
    global WordArray
    global NumberWords
    try:
        File=open(FileName,'r')
        DataRead=File.read().strip() 
        File.close()
        WordArray=DataRead.split()
        NumberWords=len(WordArray)
    except IOError:
        print("File not found")
    Play()

WordArray=[]
NumberWords=0
Choice= input("Easy, medium or hard? ").lower()
if Choice == "easy":
    File= "Easy.txt"
elif Choice == "medium":
    File= "Medium.txt"
else:
    File= "Hard.txt"
ReadWords(File)


                    
                    
                    
        
    
    
    

        
        
