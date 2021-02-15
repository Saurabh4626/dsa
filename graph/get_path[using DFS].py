class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)]
                        for j in range(self.nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __get_path_Helper(self,v1,v2,visited_array,path):
        if self.adjMatrix[v1][v2] >0:
            path.append(v2)
            path.append(v1)
            return path
        visited_array[v1]=True
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] and visited_array[i] is False:
                if self.__get_path_Helper(i,v2,visited_array,path):
                    path.append(v1)
                    return path
        return None
    def get_path(self,v1,v2):
        visited_array=[False]*(self.nVertices)
        path=self.__get_path_Helper(v1,v2,visited_array,[])
        return path
    def __str__(self):
        return str(self.adjMatrix)
g=Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,4)
g.addEdge(1,5)
g.addEdge(3,6)
g.addEdge(2,4)
g.addEdge(4,6)
print(g)
print(g.get_path(1,6))
