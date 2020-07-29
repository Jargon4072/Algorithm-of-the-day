from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,v,res,size,d):
        # visited=[False]*(max(self.graph)+1)
        visited=[False]*(size+1)
        self.dfs_visited(v,visited,res,d)

    def dfs_visited(self,v,visited,res,d):
        visited[v]=True
        res.append(v)
        for u in self.graph[v]:
            if visited[u]==False:
                self.dfs_visited(u,visited,res,d)
                d[v]+=d[u]

if __name__=="__main__":
    n,q=map(int,input().split())
    d={}
    s=[str(x) for x in input().strip().split()]
    for i in range(1,n+1):
        d[i]=s[i-1]
    g=Graph()
    size=n
    while n-1:
        u,v=map(int,input().split())
        g.addedge(u,v)
        g.addedge(v,u)
        n=n-1
    res=[]
    g.dfs(1,res,size,d)
    # print("d: ")
    # print(d)
    #print(res)
    fstr=""

    #print(fstr)
    #print(len(fstr))
    while q:
        r=[x for x in input().strip().split()]
        x=int(r[0])
        s=r[1]
        #print(str(x)+" " +s)
        gstr=d[x]
        #print(gstr)
        #res=''.join(set(s).intersection(gstr))
        # ans=len(s)-len(res)
        s=list(s)
        gstr=list(gstr)
        for i in gstr:
            if i in s:
                s.remove(i)
        print(len(s))
        q=q-1