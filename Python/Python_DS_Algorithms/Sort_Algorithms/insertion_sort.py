#insertion sort
#take the first element from unsorted array and find its correct position in sorted array
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i-1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList
#Nested loop so O(n^2) time complexity
lst = [2,1,7,6,5,3,4,9,8]
#insertionSort(lst)
