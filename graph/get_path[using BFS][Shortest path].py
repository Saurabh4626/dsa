class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)]
                        for j in range(self.nVertices)]
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __get_path_Helper(self,v1,v2,visited_array):
        q=[]
        q.append(v1)
        visited_array[v1]=True
        path={}
        while q:
            u=q.pop(0)
            if u==v2:
                return path
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] >0 and visited_array[i] is False:
                    visited_array[i]=True
                    q.append(i)
                    path[i]=u

        return False
    def get_path(self,v1,v2):
        visited_array=[False]*(self.nVertices)
        return self.__get_path_Helper(v1,v2,visited_array)
    def __str__(self):
        return str(self.adjMatrix)
g=Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(2,4)
g.addEdge(4,6)
g.addEdge(3,6)
print(g)
v1,v2=0,6
dict_path=g.get_path(v1,v2)
list=[v2]
prev=dict_path[v2]
list.append(prev)
while(True):
    prev=dict_path[prev]
    list.append(prev)
    if prev==v1:
        break
print("bfs (shortest) path is  ",*list,sep="---->")
