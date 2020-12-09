def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):      #O(n)
        for j in range(len(arrayB)):  #O(n)
            if arrayA[i] < arrayB[j]: #O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j])) #O(n)
#The complexity of this algorithm is O(ab) because the nested loop goes through differnt arrays, 
#complexity is len arrayA * len arrayB = O(ab)

arrayA = [1, 2, 3, 4, 5]
arrayB = [2, 6, 7, 8]
