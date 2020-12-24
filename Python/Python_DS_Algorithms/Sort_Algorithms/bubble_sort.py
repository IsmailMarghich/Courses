#repeatedly compare each of pair of adjest items and swap them if they are in the wrong order

def bubbleSort(customList):
    for i in range(len(customList)-1): #O(n)
        for j in range(len(customList)-i-1): #O(n)
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)
#a nested loop of O(n) each is a time complexity of O(n^2)
#space complexity is O(1) because no extra space is required
lst = [2,1,7,6,5,3,4,9,8]
bubbleSort(lst)