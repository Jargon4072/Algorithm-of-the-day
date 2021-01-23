from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.graph = defaultdict(list)
        self.V=V
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def iscycleutil(self,v,visited,recstack):
        visited[v]=True
        recstack[v]=True              #this stores info about if there is a back edge is present or not
        for i in self.graph[v]:
            if visited[i]==False:
                if self.iscycleutil(i, visited, recstack)==True:
                    return True
            elif recstack[i]==True:
                return True
        recstack[v]=False
        return False
    def cycle_detect(self):
        visited=[False]*(self.V)
        recstack=[False]*(self.V)
        for i in range(self.V):
            if visited[i]==False:
                if self.iscycleutil(i, visited, recstack)==True:
                    return True
        return False

if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    if g.cycle_detect() == True:
        print ("Graph has a cycle")
    else:
        print ("Graph has no cycle")
