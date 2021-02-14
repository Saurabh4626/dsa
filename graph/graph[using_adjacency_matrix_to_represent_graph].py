class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)]
                        for j in range(self.nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEgde(self,v1,v2):
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def isConnected(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    def __str__(self):
        return str(self.adjMatrix)
g=Graph(3)
g.addEdge(0,1)
g.addEdge(2,2)
print(g)
print(g.isConnected(2,2))
