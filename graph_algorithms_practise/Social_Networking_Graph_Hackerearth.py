from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

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
    n,e=map(int, input().split())
    g=Graph()
    while e:
        u,v=map(int, input().split())
        g.addedge(u,v)
        g.addedge(v,u)
        e=e-1
    m=int(input())
    while m:
        s,d=map(int, input().split())
        res=g.BFS(s)
        count=0
        for i in res.keys():
            if res[i]==d:
                count=count+1
        print(count)
        m=m-1