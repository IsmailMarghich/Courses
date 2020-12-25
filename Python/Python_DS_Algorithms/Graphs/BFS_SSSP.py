class Graph:
    def __init__(self, gdict=None):
        if gdict == None:  # if theres no dictionary, make one
            gdict = {}
        else:
            self.gdict = gdict
    def bfs(self, start, end):#this function will use breadth first search for a single shortest path problem
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1] #if the last node in path is equal to our end, we return path
            if node == end:
                return path
            else:           # otherwise we continue searching
                for adjacent in self.gdict.get(node, []): #we grab the adjacent nodes
                    new_path = list(path)
                    new_path.append(adjacent) #we add them to our path and also to our queue
                    queue.append(new_path)
#Space and time complexity is O(E) where E is the amount of edges
#this algorithms works only for unweighted graphs, as it would not differentiate between the weighted edges of a weighted graph
#we wont try DFS search because that tends to find the longest path instead of the shortest path
customDict = {"a": ["b", "c"],
              "b": ["d", "g"],
              "c": ["d", "e"],
              "d": ["f"],
              "e": ["f"],
              "g": ["f"]
              }
graph = Graph(customDict)
print(graph.bfs('a', 'f'))