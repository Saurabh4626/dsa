class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)]
                        for j in range(self.nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __dfsHelper(self,starting_vertex,visited_array):
        visited_array[starting_vertex]=True
        for i in range(self.nVertices):
            if self.adjMatrix[starting_vertex][i]>0 and visited_array[i] is False:
                self.__dfsHelper(i,visited_array)
    def is_connected(self):
        visited_array=[False]*(self.nVertices)
        self.__dfsHelper(0,visited_array)
        print(visited_array)
        if visited_array.count(False) >0:
            return False
        else:
            return True
    def __str__(self):
        return str(self.adjMatrix)
g=Graph(9)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,6)
g.addEdge(7,8)
print(g)
print(g.is_connected())
