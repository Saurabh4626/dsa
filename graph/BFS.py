import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)]
                        for j in range(self.nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __bfsHelper(self,starting_vertex,visited_array):
        q=queue.Queue
        q.put(starting_vertex)
        visited_array[s]=True
        while q.empty() is False:
            u=q.get()
            print(u)
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] >0 and visited_array[i] is False:
                    q.put(i)
                    visited_array[i]=True
    def bfs(self):
        visited_array=[False]*(self.nVertices)
        self.__bfsHelper(0,visited_array)
    def __str__(self):
        return str(self.adjMatrix)
g=Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,4)
g.addEdge(2,3)
print(g)
g.dfs()
