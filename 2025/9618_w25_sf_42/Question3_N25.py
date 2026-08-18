TreeArray=[]
for x in range(50):
    TreeArray.append([-1,-1,-1])
RootPointer= -1
FreeNode= 0

def AddNode(NodeData):
    global FreeNode
    global TreeArray
    global RootPointer
    if FreeNode <= 49:
        TreeArray[FreeNode][0]=-1
        TreeArray[FreeNode][1]=NodeData
        TreeArray[FreeNode][2]=-1
        if RootPointer== -1:
            RootPointer= 0
        else:
            Placed= False
            CurrentNode= RootPointer
            while Placed== False:
                if NodeData< TreeArray[CurrentNode][1]:
                    if TreeArray[CurrentNode][0] == -1:
                        TreeArray[CurrentNode][0]= FreeNode
                        Placed= True
                    else:
                        CurrentNode= TreeArray[CurrentNode][0]
                else:
                    if TreeArray[CurrentNode][2] == -1:
                        TreeArray[CurrentNode][2]= FreeNode
                        Placed= True
                        
                    else:
                        CurrentNode= TreeArray[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("The tree is full")


def WriteAllToFile():
    try:
        File= open("Tree.txt","a+")
        for x in range(0,50):
            Line= str(TreeArray[x][0]) + "," + str(TreeArray[x][1]) + "," + str(TreeArray[x][2]) + "\n"
            File.write(Line)
        File.close()
    except:
        print("Cannot write to file")

try:
    File= open("TreeData.txt")
    for Line in File:
        AddNode(int(Line.strip()))
    File.close()
except:
    print("Error cannot open file")

WriteAllToFile()


            


    
        
        
            
                    

                    
                    
                  
                    
                        
                        
                        
        
    


    
