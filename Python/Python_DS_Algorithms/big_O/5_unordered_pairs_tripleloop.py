#Question5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):     #O(a) } #becomes O(ab)
        for j in range(len(arrayB)): #O(b) }
            for k in range(0, 100000): #O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j])) #O(1)

#Time complexity is O(ab), the for in range loop is still only run once, so it doesnt matter.
