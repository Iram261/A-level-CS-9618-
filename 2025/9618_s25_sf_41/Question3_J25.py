class Node:
    def __init__(self, pNodeData):
        #PRIVATE NodeData,LeftNode,RightNode
        self.__NodeData=pNodeData #integer
        self.__LeftNode=None #node
        self.__RightNode=None #node
    def GetLeft(self):
        return self.__LeftNode
    def GetRight(self):
        return self.__RightNode
    def GetData(self):
        return self.__NodeData
    def SetLeft(self,NewNode):
        self.__LeftNode=NewNode
    def SetRight(self,NewNode):
        self.__RightNode=NewNode

class Tree:
    def __init__(self,FirstNode):
        self.__FirstNode=FirstNode #node
    def GetRootNode(self):
        return self.__FirstNode
    def Insert(self,NewNode): 
        CurrentNode=self.__FirstNode
        Inserted=True
        while Inserted:
            if NewNode.GetData()<CurrentNode.GetData():
                if CurrentNode.GetLeft()==None:
                    CurrentNode.SetLeft(NewNode)
                    return True
                else:
                    CurrentNode=CurrentNode.GetLeft()
            else:
                if CurrentNode.GetRight()==None:
                    CurrentNode.SetRight(NewNode)
                    return True
                else:
                    CurrentNode=CurrentNode.GetRight()
def OutputInOrder(RootNode):  
    if RootNode.GetLeft() != None:
        OutputInOrder(RootNode.GetLeft())
    print(RootNode.GetData())
    if RootNode.GetRight() != None:
        OutputInOrder(RootNode.GetRight())

FirstNode=Node(10)
SecondNode=Node(20)
ThirdNode=Node(5)
FourthNode=Node(15)
FifthNode=Node(7)
MyTree=Tree(FirstNode)
MyTree.Insert(SecondNode)
MyTree.Insert(ThirdNode)
MyTree.Insert(FourthNode)
MyTree.Insert(FifthNode)
OutputInOrder(MyTree.GetRootNode())



        
    
        
    
    
                    
                    
                    
                    
        
        
    
        
        
        
        
        
        
