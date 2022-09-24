class Graph():
    
    def __init__(self):
        self.numberofnodes = 0 
        self.adjacentlist = {}
        
    def addvertex(self,node):
            self.adjacentlist[node] = []
            self.numberofnodes += 1
            
    def addedge(self,node1,node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)
        
    
    def showconnections(self):
        for node in self.adjacentlist:
            print(f'{node} -->> {" ".join(map(str,self.adjacentlist[node]))}')
            


    # Graph Traversal
    # BreadthFirstSearch
    def BFSGraph(self,vertex):
        # a boolean array to mark the nodes we visit
        visited = [False] * self.numberofnodes
        queue= []
        mylist = []
        queue.append(vertex)
        visited[vertex] = True
        while queue:
            currentnode = queue.pop(0)
            mylist.append(currentnode)

            # get all adjacent vertices of the
            # dequeued vertex. If an adjacent is
            # not visited then visit it and enqueue it
            for i in self.adjacentlist:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        
        return mylist
        
        
        
my_graph = Graph()
my_graph.addvertex(0)
my_graph.addvertex(1)
my_graph.addvertex(2)
my_graph.addvertex(3)

my_graph.addedge(0, 1)
my_graph.addedge(0, 2)
my_graph.addedge(1, 2)
my_graph.addedge(2, 0)
my_graph.addedge(2, 3)
my_graph.addedge(3, 0)
my_graph.showconnections()

# 0 -->> 1 2 2 3
# 1 -->> 0 2
# 2 -->> 0 1 0 3
# 3 -->> 2 0

my_graph.BFSGraph(0)

# [0, 1, 2, 3]