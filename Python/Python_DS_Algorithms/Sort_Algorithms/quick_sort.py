#quick sort is also a divide and conquer algorithm
#pick a pivot number and make sure smaller numbers are located at the left pf pivot, and bigger numbers on the right
#unlike merge sort, no extra space is required
#we place the pointers Left and Right at the beginning and end of the array(right before Pivot)
#these will start moving and comparing numbers to the pivot and sorting them, until they run into a number thats already sorted
#then the pointers change place and continue, if both the left and right pointer meet, they will replace that element with pivot
#now the array is split into numbers smaller than pivot and larger
#we then recursively call quick sort on each split until the whole array is sorted

def partition(customList, low, high): #helper function to partition array
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot: #if value is smaller than pivot
            i += 1
            customList[i], customList[j] = customList[j], customList[i] #swap values
    customList[i+1], customList[high] = customList[high], customList[i+1] #if value is larger, swap them the other way, (we add +1 because larger elements should be to the right of pivot)
    return (i+1)

def quicksort(customList, low, high):
    if low < high:
        pivot = partition(customList, low, high) # we grab a new pivot
        quicksort(customList, low, pivot-1) #we sort the left of pivot (-1) T(n/2)
        quicksort(customList, pivot+1, high) #we sort the right of pivot (+1) T(n/2)
#quick sort is O(NlogN) time complexity, space complexity is O(n) because quick sort is called recursively
#quick sort is not stable however

lst = [2, 1, 7, 6, 5, 3, 4, 9, 8]
quicksort(lst, 0, 8)
print(lst)
