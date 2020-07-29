# @Author: Dwivedi Chandan
# @Date:   2020-07-22T09:58:11+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-07-27T17:50:10+05:30



from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,v):
        visited=[False]*(max(self.graph)+1)
        self.dfs_visit(v,visited)

    def dfs_visit(self,u,visited):
        visited[u]=True
        print(u, end=" ")

        for v in self.graph[u]:
            if visited[v]==False:
                self.dfs_visit(v,visited)


g = Graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(2)
