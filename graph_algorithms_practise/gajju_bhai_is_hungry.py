# your code goes here
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s,n):
        dist={}
        dist[s]=0
        visited={}
        for i in range(1,n+1):
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
    # print("t: ",t)
    while t:
        n,m=map(int, input().split())
        # print("n: ",n)
        g=Graph()
        for i in range(0,n-1):
            u,v=map(int, input().split())
            # print("u: ",u," v: ",v)
            g.addedge(u,v)
            g.addedge(v,u)
        sum=0
        resturents=[int(x) for x in input().strip().split()]
        # print("resturents: ",resturents)
        res=g.BFS(1,n)
        # print("BFS res: ",res)
        for i in range(len(resturents)):
            d=resturents[i]
            # print("d: ",d)
            edges=2*(res[d])
            # print("total edges travelled: ",edges)
            sum=sum+edges
            # print("sum: ",sum)
        ans=sum/float(m)
        # print(ans)
        print("{:.6f}".format(ans))
        t=t-1