## to check if there exist a path between given two vertices

class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)]
                        for j in range(self.nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __str__(self):
        return str(self.adjMatrix)

    def hasPath_helper(self,v1,v2,visited_array):
        if self.adjMatrix[v1][v2] >0:
            return True
        visited_array[v1]=True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i]>0 and visited_array[i] is False:
                if self.hasPath_helper(i,v2,visited_array) is True:
                    return True
        return False
    
    def hasPath(self,v1,v2):
        visited_array=[False]*self.nVertices
        return self.hasPath_helper(v1,v2,visited_array)

g=Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,4)
g.addEdge(2,3)
g.addEdge(5,6)
print(g)
print(g.hasPath(1,6))
