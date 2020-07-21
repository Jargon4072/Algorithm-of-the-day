from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        # keep track of all visited nodes
        explored=[]
        # keep track of nodes to be checked
        queue=[]
        queue.append(s)
        levels={}            # this dict keeps track of levels
        levels[s]=0          # depth of start node is 0
        visited={}         # to avoid inserting the same node twice into the queue
        for i in self.graph.keys():
            visited[i]=False

        # keep looping until there are nodes still to be checked
        while queue:
            # pop shallowest node (first node) from queue
            node=queue.pop(0)
            if node not in explored:
                explored.append(node)
            neighbours = self.graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                if visited[neighbour]==False:
                    queue.append(neighbour)
                    visited[neighbour]=True
                    levels[neighbour]=levels[node]+1


        # print(levels)
        return explored


if __name__=="__main__":
    print(
    '''
    Graph representation:

     'A': ['B', 'C', 'E'],
     'B': ['A','D', 'E'],
     'C': ['A', 'F', 'G'],
     'D': ['B'],
     'E': ['A', 'B','D'],
     'F': ['C'],
     'G': ['C']
    '''
    )

    g=Graph()
    g.addedge('A','B')
    g.addedge('A','C')
    g.addedge('A','E')
    g.addedge('B','A')
    g.addedge('B','D')
    g.addedge('B','D')
    g.addedge('C','A')
    g.addedge('C','F')
    g.addedge('C','G')
    g.addedge('D','B')
    g.addedge('E','A')
    g.addedge('E','B')
    g.addedge('E','D')
    g.addedge('F','C')
    g.addedge('G','C')

    print("BFS traversal with sources as node A is: ")
    ans=g.BFS('A')
    print(ans)


    # Creating Graph
    print(
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
    )

    g1=Graph()
    g1.addedge(0,1)
    g1.addedge(0,2)
    g1.addedge(1,2)
    g1.addedge(1,3)
    g1.addedge(3,4)
    g1.addedge(4,2)
    g1.addedge(2,0)

    print("BFS Traversal is with source node 2 is :")
    ans1=g1.BFS(2)
    print(ans1)