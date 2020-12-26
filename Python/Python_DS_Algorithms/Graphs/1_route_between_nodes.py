#Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode): #breadth first search
        visited = [startNode]
        queue = []
        path = False #wether theres a path between start and end node
        while queue:
            dVertex = queue.pop(0)
            for adjacent in self.gdict[dVertex]:
                if adjacent not in visited:
                    if adjacent == endNode:
                        path = True
                        break
                    else:
                        visited.append(adjacent)
                        queue.append(adjacent)
        return path
