from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.graph= []
        self.V = V
    def addEdge(self,u,v,w):        # Edges will have weights too
        self.graph.append([u,v,w])
    def FIND_SET(self,parent, i):       #func to find set (parent) to which i belongs to.
        if parent[i]==i:
            return i
        return self.FIND_SET(parent,parent[i])
    def UNION(self,parent,rank,x,y):         # merges the sets of safe edges.
        xp= self.FIND_SET(parent,x)
        yp=self.FIND_SET(parent,y)
        if rank[xp]<rank[yp]:
            parent[xp]=yp
        elif rank[xp]> rank[yp]:
            parent[yp]=xp
        else:
            parent[yp]=xp
            rank[xp]+=1          #rank incriment happens here.

    def Krushkal(self):
        res=[]        # variable to store final results.
        self.graph=sorted(self.graph,key=lambda w: w[2])        #sorting graph by edges weights.
        parent=[]
        rank=[]
        for vertex in range(self.V):            # creation of initial disjoint set
            parent.append(vertex)
            rank.append(0)
        i=0   #for sorted edges
        j=0   # for res[]
        while j<self.V-1:     # A MST has V-1 edges.
            u,v,w=self.graph[i]
            i=i+1
            x= self.FIND_SET(parent,u)
            y= self.FIND_SET(parent,v)
            if x!= y:      # if u and v belongs to different sets then do union and store results 
                j=j+1
                res.append([u,v,w])
                self.UNION(parent,rank,x, y)
        return res

if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    res=g.Krushkal()
    print("Krushkal MST of the given graph, [[u,v,w]], is : ",res)
