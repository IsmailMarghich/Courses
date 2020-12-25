from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    def addNode(self, value):
        self.nodes.add(value)
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)
    while nodes:
        minNode = None
        for node in nodes: #this will try to find the smallest node
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break
        nodes.remove(minNode)
        currentWeight = visited[minNode]
        
        for edge in graph.edges[minNode]: #looking at each adjacent edge
            weight = currentWeight + graph.distances[(minNode, edge)] #find the smallest edge
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode) #append it to our path
    return visited, path
#we have 2 nested loop, so time complexity is O(V^2) and space complexity is O(E) where V is vertices/nodes and E is edges (because we store the edges)
#this algorithm does not work with negative weights in a cycled graph becuase the dijkstra algorithm will start to loop as it tries to find the shorest path
customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)
print(dijkstra(customGraph, 'A')) #here we can see the shortest cost of each path from A to a certain node
