
# Write your code here
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,v,d,n):
        visited=[False]*(n+1)
        self.dfs_visit(v,visited,d,0)
    def dfs_visit(self,u,visited,d,dis):
        visited[u]=True
        d[u]=dis
        for v in self.graph[u]:

            if visited[v]==False:
                self.dfs_visit(v,visited,d,dis+1)
        dis=dis-len(self.graph[u])

if __name__=="__main__":
    size=int(input())-1
    n=size
    g=Graph()
    while n:
        u,v=map(int,input().split())
        # print(u,v)
        g.addedge(u,v)
        g.addedge(v,u)
        n=n-1
    # print(g.graph)
    d={}
    g.dfs(1,d,size+1)
    q=int(input())
    # print(q)
    #print(d)
    g_list=[]
    while q:
        gf=int(input())
        g_list.append(gf)
        q=q-1
    #print(g_list)
    res=d[g_list[0]]
    for gfp in g_list:
    	res=min(res,d[gfp])
    #print(res)
    ans=[]
    for item in g_list:
    	if d[item]==res:
    		ans.append(item)
    ans.sort()
    print(ans[0])