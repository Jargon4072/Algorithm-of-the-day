from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s,y,n):
        # dist=[0]*10000000
        for z in self.graph.keys():
            self.graph[z].sort()
        dist={}
        dist[s]=0
        explored=[]
        visited={}
        for i in range(1,n+1):
            visited[i]=False
        queue=[]

        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            if s not in explored:
                explored.append(s)

            for i in self.graph[s]:
                if i==y:
                    explored.append(i)
                    return explored
                if visited[i]==False:
                    queue.append(i)
                    dist[i]=dist[s]+1
                    visited[i]=True
        return explored

if __name__=="__main__":
    temp=[int(x) for x in input().strip().split()]
    n=temp[0]
    m=temp[1]
    t=temp[2]
    c=temp[3]
    g=Graph()
    while m:
        u,v=map(int, input().split())
        g.addedge(u,v)
        g.addedge(v,u)
        m=m-1
    x,y=map(int,input().split())
    res=g.BFS(x,y,n)
    print(len(res))
    for i in range(len(res)-1):
        print(res[i],end=" ")
    print(res[len(res)-1])