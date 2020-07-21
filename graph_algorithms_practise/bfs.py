# @Author: Dwivedi Chandan
# @Date:   2020-07-17T21:14:26+05:30
# @Email:  chandandwivedi795@gmail.com
# @Last modified by:   Dwivedi Chandan
# @Last modified time: 2020-07-19T23:55:52+05:30

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited=[False]*(len(self.graph))

        queue=[]

        queue.append(s)
        visited[s]=True

        while queue:
            u=queue.pop(0)
            print(u, end=" ")
            for i in self.graph[u]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True



if __name__=="__main__":
    # Creating Graph
    '''
         0 _
        / \\
      _/  _\\
      1----_2 ←------ Source (start point for BFS)
      |    `|
     _|     |
      3----_4

      _ at the end of edges repesent the incidence dicrection of edge.
    '''

    g1=Graph()
    g1.addedge(0,1)
    g1.addedge(0,2)
    g1.addedge(1,2)
    g1.addedge(1,3)
    g1.addedge(3,4)
    g1.addedge(4,2)
    g1.addedge(2,0)

    print("BFS Traversal is :")
    g1.BFS(2)


