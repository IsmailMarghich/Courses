#we repeadetly find the minimum element and move it to the sorted part of array until the array is sorted

def selectionSort(customList):
    for i in range(len(customList)): # O(n)
        min_index = i
        for j in range(i+1, len(customList)):#O(n) #loop to find the minimum of the list, and then in outerloop we add it to our sorted part of the list
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i] #here we swap the minium wth current element until the list is sorted
    print(customList)
#nested loop so O(n^2) time complexity, space complexity is O(1) because no additional memory is required
lst = [2,1,7,6,5,3,4,9,8]
selectionSort(lst)