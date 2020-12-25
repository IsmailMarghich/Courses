#prims algorithm is a greedy algorithm to find the minimum spanning tree for unweighted undirected graph
#-take any vertex as source, set it weight as zero and all other vertices weight as infinity
#-for every adjacent vertices if the current weight is more than current edge, then we sit it to current edge
#-then we mark current vertex as visited
#repeat these steps for all vertices in increasing order of weight
import sys


class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.MST = []  # our minimum spanning tree

    def printSolution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def prims(self):
        visited = [0] * self.vertexNum
        edgeNum = 0
        visited[0] = True
        while edgeNum < self.vertexNum-1: #iterate E times, index starts from zero so we do -1
            min = sys.maxsize #infinity
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if ((not visited [j]) and self.edges[i][j]): #if adjestent vertex isnt visited and has edges
                            if min > self.edges[i][j]: #if infinity is larger than adjacent edge we set it that vertex as new weight
                                min = self.edges[i][j]
                                s = i #start
                                d = j #destination
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])#append our start and destination to our minimum spanning tree
            visited[d] = True #set destination to visited
            edgeNum +=1 #increase our edge number
        self.printSolution()

#we have a three nested loop so time complexity is O(V^3) where V is amount of vertices
#space complexity is O(V) because we store our vertices

edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]
nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.prims()
#Kruskal's algorithm concentrates on edges, and finalizes an edge in eacch iteration
#Prinm's algorithm concetrates on vertices, and finalizes a vertex in each iteration