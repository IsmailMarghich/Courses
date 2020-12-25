class Graph:
    def __init__(self, gdict=None):
        if gdict == None: #if theres no dictionary, make one
            gdict = {}
        else:
            self.gdict = gdict
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def BFS(self, vertex): #in breadth first search we go through each level first visiting all the neighbour vertices and then move on to the next level or vertex
        queue = [vertex] #have 2 lists where we store our queue and which vertex we visited already
        visited = [vertex]
        while queue:
            deVertex = queue.pop(0) #dequeue each letter and print it
            print(deVertex)
            for adjacent in self.gdict[deVertex]: #check which vertices its adjacent to
                if adjacent not in visited: 
                    visited.append(adjacent) #append it to visited and the queue if its a new vertex
                    queue.append(adjacent)
#BFS can be used for all sorts of graphs, and has a space and time complexity of O(V+E) where V is the amount of vertices and E is the amount of edges
    def DFS(self, vertex): #with depth first search we try to go as far as possible with each vertex, and then backtrack and do the same with a new vertex 
        visited = [vertex] #2 lists for our stack and visited list
        stack = [vertex]
        while stack:
            popVertex = stack.pop() #here in a stack we use the pop method to remove the last element instead of first
            print(popVertex)
            for adjacent in self.gdict[popVertex]: #we append new vertexes to our stack and visited list
                if adjacent not in visited:
                    visited.append(adjacent)
                    stack.append(adjacent) 
                    #because we use a stack we pop the last element, this way we go as deep as possible
#DFS can be used for all sorts of graphs, and has a space and time complexity of O(V+E) where V is the amount of vertices and E is the amount of edges

customDict = {"a": ["b", "c"],
              "b": ["a", "d", "e"],
              "c": ["a", "e"],
              "d": ["b", "e", "f"],
              "e": ["d", "f"],
              "f": ["d", "e"]
              }
graph = Graph(customDict)
graph.addEdge('e', 'c')
print('-------BFS------')
graph.BFS('a')
print('-------DFS------')
graph.DFS('a')
