'''
Problem: Finding Strongly Connected Components
Algorithm name: Kosaraju's Algorithm
Time Complexity: O(V+E)
'''


from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.V=V
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSutil(self,u,visited):         # function to find and print DFS
        visited[u]=True
        print(u,end=" ")
        for i in self.graph[u]:
            if visited[i]==False:
                # visited[i]=True
                self.DFSutil(i,visited)
    def fillorder(self,u,visited,stack):             # function to get thes elements by there finishing times
        visited[u]=True
        for i in self.graph[u]:
            if visited[i]==False:
                # visited[i]= True
                self.fillorder(i,visited,stack)
        stack=stack.append(u)
    def getTranspose(self):                 # function to return transpose of the created graph
        g=Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g
    def getSCC(self):                    # function to get the strongly connected components
        stack=[]
        visited=[False]*(self.V)
        # STEP1: Get the elements by there finishing time using DFS trav. approach
        for i in range(self.V):
            if visited[i]== False:
                self.fillorder(i,visited,stack)
        # STEP2: Get the transpose of the created graph
        gt=self.getTranspose()

        visited=[False]* (self.V)
        # STEP 3: Call DFS on transposed graph, but in the main loop of dfs, considering/ the vertices
        #         in the order of decreasing finishing time.
        while stack:
            i=stack.pop()
            if visited[i]==False:
                gt.DFSutil(i,visited)
                print("")

if __name__ == "__main__":
    g= Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    print("Strongly connected components are: ")
    g.getSCC()
