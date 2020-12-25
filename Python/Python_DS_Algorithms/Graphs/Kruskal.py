#kruskal's algorithm is an greedy algorithm that finds the minimum spanning tree for weighted undirected graphs in two ways
#-add increasing cost edges at each step
#-avoid any cycle at each step (our answer should be a tree, which dont have cycles) 
#to avoid cycles we will be using disjointed sets, this way cycles cant come in, since sets cannot have duplicates
import disjoint_set as dst


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = [] #our minimum spanning tree

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def kruskal(self):
        i, e = 0, 0 #our iterable variables
        ds = dst.DisjointSet(self.nodes) #create our disjointed set with nodes
        self.graph = sorted(self.graph, key=lambda item: item[2]) #sort the graph
        while e < self.V - 1:
            s, d, w = self.graph[i] #start, destination, weight
            i += 1
            x = ds.find(s) #find source of start
            y = ds.find(d) #find source of distance
            if x != y: #if they dont have the same parent we add them to our minimum spanning tree
                e +=1 #increase our iterable
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSolution(s,d,w)


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskal()
#Kruskal's algorithm concentrates on edges, and finalizes an edge in eacch iteration
#Prinm's algorithm concetrates on vertices, and finalizes a vertex in each iteration
