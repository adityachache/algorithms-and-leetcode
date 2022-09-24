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

    
    # BREADTH FIRST SEARCH ITERATIVE
    def BreadthFirstSearch(self):
        currentnode = self.root
        mylist = []
        queue = []
        queue.append(currentnode)
        while len(queue) > 0:
            currentnode = queue.pop(0)
            mylist.append(currentnode.data)
            if currentnode.left:
                queue.append(currentnode.left)
            if currentnode.right:
                queue.append(currentnode.right)
        return mylist

    # BREADTH FIRST SEARCH RECURSIVE
    def BFSRecursive(self,queue,mylist):
        if len(queue) == 0:
            return mylist
        currentnode = queue.pop(0)
        mylist.append(currentnode.data)
        if currentnode.left:
            queue.append(currentnode.left)
        if currentnode.right:
            queue.append(currentnode.right)
        return self.BFSRecursive(queue,mylist)
    

tree = BinarySearchTree()
tree.insert(23)
tree.insert(5)
tree.insert(75)
tree.insert(1)
tree.insert(7)
tree.insert(45)
tree.insert(80)


#         23
#    5          75
# 1     7    45     80


print(tree.BreadthFirstSearch())
print(tree.BFSRecursive(queue=[tree.root],mylist=[]))