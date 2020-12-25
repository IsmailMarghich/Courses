#Disjoint sets is a datastructure that is partinioned into a number of disjoint and non overlapping sets

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item]) #recursively look for the parent
    
    def union(self, x, y): #uniting X and Y
        xroot = self.find(x) #find the parent of both
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:  # here we check wether the rank of x is higher or lower, and depending on that change the ranks of x or y
            self.parent[xroot] = yroot
        elif self.rank[xroot] < self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot #if both of them have same ranks, increase the rank of X by 1 since its the first item
            self.rank[xroot] +=1
vertices = ["A", "B", "C", "D", "E"]

ds = DisjointSet(vertices)
ds.union("A", "B")
ds.union("A", "C")
print(ds.find("C"))
