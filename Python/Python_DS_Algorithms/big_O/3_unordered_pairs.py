def printUnorderedPairs(array):
    for i in range(0, len(array)):       #O(n)
        for j in range(i+1, len(array)): #O(n)
            print(array[i] + "," + array[j]) #O(1)
printUnorderedPairs([1,2,3]) # Time complexity is O(n^2) because of a nested loop