#Given S1 and S2 are strigns
#Convert S2 to S1 to delete, insert or replace operations
#Find the minimimum count of edit operations


def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1): #our base cases
        return len(s2)-index2
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1)
    else:
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1) #our 3 different operations and how they change the indexes
        insertOp = 1 + findMinOperation(s1, s2, index1+1, index2)
        replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
        return min (deleteOp, insertOp, replaceOp)

print(findMinOperation("table", "tbrltt", 0, 0))