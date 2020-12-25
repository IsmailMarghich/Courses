#floyd warshall algorithm is an algorithm used for an all pair shortest path problem, here we have to calculate the shortest path for all vertices
INF = 9999
# Printing the solution


def printSolution(nV, distance): #helper function to print our solution
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

def floydWarshall(nV, G): #nv is number of vertices, G is our graph
    distance = G
    for k in range(nV): #for each vertex
        for i in range(nV): #for rows 
            for j in range(nV): #for columns
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j]) #were calculating the minimum distance to each vertice for each vertice 
    printSolution(nV, distance)
#a three nested loop, so the floyd warshall algorithm has a time complexity O(V^3)
#space complexity is O(V^2) because we are creating a 2d matrix of V*V dimension
#this algorithm does work for uncyclic negative graphs, but not for negative cycled ones because it would loop, similair to dijkstras algorithm

G = [[0, 8, INF, 1],
     [INF, 0, 1, INF],
     [4, INF, 0, INF],
     [INF, 2, 9, 1]
     ]

floydWarshall(4, G)
