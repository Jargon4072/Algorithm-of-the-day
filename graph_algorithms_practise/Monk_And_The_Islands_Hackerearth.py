from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    # def BFS(self,s):      # check why this is giving TLE
    #     queue=[s]
    #     levels={}
    #     levels[s]=0
    #     visited=[s]
    #
    #     while queue:
    #         node=queue.pop(0)
    #         neighbours=self.graph[node]
    #
    #         for neighbour in neighbours:
    #             if neighbour not in visited:         #this might be the reason for TLE as it is seraching in visited array which takes O(n), thus increasing time.
    #                 queue.append(neighbour)
    #                 visited.append(neighbour)
    #                 levels[neighbour]=levels[node]+1
    #
    #     return levels
    def BFS(self,s):
        # dist=[0]*10000000
        dist={}
        dist[s]=0

        visited={}
        for i in self.graph.keys():
            visited[i]=False
        queue=[]

        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    dist[i]=dist[s]+1
                    visited[i]=True
        return dist

if __name__=="__main__":
    t=int(input())
    while t:
        n,m=map(int, input().split())
        g=Graph()
        while m:
            u,v=map(int, input().split())
            g.addedge(u,v)
            g.addedge(v,u)
            m=m-1
        res=g.BFS(1)
        print(res[n])
        t=t-1