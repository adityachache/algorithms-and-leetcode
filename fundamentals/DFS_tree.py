from typing import Counter


class Node():
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree():
    
    def __init__(self):
        self.root = None
        
    def __str__(self):
        return str(self.__dict__)
              
    def insert(self,data):
        newnode = Node(data)
        if self.root == None:
            self.root = newnode
            
        else:
            currentnode = self.root
            while True:
                if data < currentnode.data:
                    # we go left
                    if currentnode.left == None:
                        currentnode.left = newnode
                        return
                    else:
                        currentnode = currentnode.left
                        
                elif data > currentnode.data:
                    # we go right
                    if currentnode.right == None:
                        currentnode.right = newnode
                        return
                    else:
                        currentnode = currentnode.right

    
    # DEPTH FIRST SEARCH INORDER
    def DFSInorder(self,node,mylist):
        # print(node.data)
        if node.left:
            self.DFSInorder(node.left,mylist)
        mylist.append(node.data)
        if node.right:
            self.DFSInorder(node.right,mylist)
        return f"DFS INORDER ---> {mylist}"
    
    # DEPTH FIRST SEARCH PREORDER
    def DFSPreorder(self,node,mylist):
        # print(node.data)
        mylist.append(node.data)
        if node.left:
            self.DFSPreorder(node.left,mylist)
        if node.right:
            self.DFSPreorder(node.right,mylist)
        return f"DFS PREORDER ---> {mylist}"
    
    # DEPTH FIRST SEARCH POSTORDER
    def DFSPostorder(self,node,mylist):
        # print(node.data)
        if node.left:
            self.DFSPostorder(node.left,mylist)
        if node.right:
            self.DFSPostorder(node.right,mylist)
        mylist.append(node.data)
        return f"DFS POSTORDER ---> {mylist}"


    def DFSIN(self):
        currentnode = self.root
        mylist = []
        while currentnode.left and currentnode.right:
            while currentnode.left:
                currentnode = currentnode.left
            mylist.append(currentnode.data)
            while currentnode.right:
                currentnode = currentnode.right
        
        # if currentnode.left:
        #     currentnode = currentnode.left
        #     mylist.append(currentnode.data)
        # else:
        #     currentnode = currentnode.right
        #     mylist.append(currentnode.data)
                
        return mylist


mytree = BinarySearchTree()
mytree.insert(23)
mytree.insert(5)
mytree.insert(75)
mytree.insert(1)
mytree.insert(7)
mytree.insert(45)
mytree.insert(80)

#         23
#    5          75
# 1     7    45     80


# print(mytree.DFSInorder(mytree.root,[]))
# print(mytree.DFSPreorder(mytree.root,[]))
# print(mytree.DFSPostorder(mytree.root,[]))

print(mytree.DFSIN())