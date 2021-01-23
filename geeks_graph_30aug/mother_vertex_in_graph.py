'''
What is a Mother Vertex?
A mother vertex in a graph G = (V,E) is a vertex v such that
all other vertices in G can be reached by a path from v.
'''

# Solution: find all strongly connected components and return the components which contains number of
#           element equal to the number of vertex in the graph.

from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.graph=defaultdict(list)
        self.V=V
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSutil(self,u,visited,res):
        visited[u]=True
        res.append(u)
        for i in self.graph[u]:
            if visited[i]==False:
                self.DFSutil(i,visited, res)
    def get_transpose(self):
        g=Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
    def fillfinisorder(self,u,visited,stack):
        visited[u]= True
        for i in self.graph[u]:
            if visited[i]==False:
                self.fillfinisorder(i,visited,stack)
        stack.append(u)
    def get_scc(self,res):
        visited=[False]*(self.V)
        stack=[]
        for i in range(self.V):
            if visited[i]==False:
                self.fillfinisorder(i,visited,stack)
        gt=self.get_transpose()
        visited=[False]*(self.V)
        while stack:
            i=stack.pop()
            if visited[i]==False:
                rdfs=[]
                self.DFSutil(i,visited,rdfs)
                res.append(rdfs)

    def find_mother(self):
        res=[]
        self.get_scc(res)
        for item in res:
            if len(item)==self.V:
                print("mother found!")
                print(item[0])
if __name__=="__main__":
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(6, 4)
    g.addEdge(5, 6)
    g.addEdge(5, 2)
    g.addEdge(6, 0)

    print("FINDING MOTHER Vertex .....")
    g.find_mother()
