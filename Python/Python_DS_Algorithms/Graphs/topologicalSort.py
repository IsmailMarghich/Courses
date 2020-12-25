from collections import defaultdict

class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def toplogicalify(self, v, visited, stack): #helper function for topolical sort, marks vertices adjecent to current vertex
        visited.append(v)
        for i in self.graph[v]: 
            if i not in visited:
                self.toplogicalify(i, visited, stack)
        stack.insert(0, v)
    def topologicalSort(self): #topological sort prints how the graph looks like with respect to the graphs dependacies
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited: #if we find a new vertex, send it to helper function
                self.toplogicalify(k, visited, stack)
        print(stack)
#space complexity and time complexity is O(V+E) where V is amount of vertices, and E is amount of edges
customGraph = Graph(8)
customGraph.addEdge('A', 'C')
customGraph.addEdge('C', 'E')
customGraph.addEdge('E', 'H')
customGraph.addEdge('E', 'F')
customGraph.addEdge('F', 'G')
customGraph.addEdge('B', 'D')
customGraph.addEdge('B', 'C')
customGraph.addEdge('D', 'F')
customGraph.topologicalSort()
