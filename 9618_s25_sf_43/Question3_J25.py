class Node:
    def __init__(self,NodeData):
        self.__TheData=NodeData #integer
        self.__NextNode= None #node

    def GetData(self):
        return self.__TheData
    def GetNextNode(self):
        return self.__NextNode
    def SetNextNode(self,pNextNode):
        self.__NextNode=pNextNode

class LinkedList:
    def __init__(self):
        self.__HeadNode= None #node
    def InsertNode(self,NodeData):
        TheNode=Node(NodeData)
        TheNode.SetNextNode(self.__HeadNode)
        self.__HeadNode=TheNode
    def Traverse(self): 
        ReturnValue=""
        CurrentNode=self.__HeadNode
        while(CurrentNode != None):
            ReturnValue= ReturnValue+ str(CurrentNode.GetData())+" "
            CurrentNode=CurrentNode.GetNextNode()
        return ReturnValue
    def RemoveNode(self,DataToRemove):
        if self.__HeadNode== None:
            return False
        elif self.__HeadNode.GetData()== DataToRemove:
            self.__HeadNode= self.__HeadNode.GetNextNode()
            return True
        Found=False
        CurrentNode=self.__HeadNode
        while not(Found) and CurrentNode != None:
            if ((CurrentNode).GetNextNode()).GetData() ==DataToRemove:
                CurrentNode.SetNextNode(CurrentNode.GetNextNode().GetNextNode())
                Found=True
            else:
                CurrentNode=CurrentNode.GetNextNode()
        return Found

CreateList= LinkedList()
CreateList.InsertNode(10)
CreateList.InsertNode(20)
CreateList.InsertNode(30)
CreateList.InsertNode(40)
CreateList.InsertNode(50)
ReturnValue1=(CreateList.Traverse())
CreateList.RemoveNode(30)
ReturnValue2=(CreateList.Traverse())
print(ReturnValue1)
print(ReturnValue2)




                
                
                
            
            
    
            
            
        
        
        
    
