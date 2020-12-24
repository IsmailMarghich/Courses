import math
import insertion_sort as sort
#create buckets and distribute elements of array into buckets(square root number of elemtns) is the amount of buckets
#sort the buckets induvidually, merge the buckets afterwards
#to determine which elemnts go to which bucket, we use the formula ceil(Value * numbers of buckets / max value) where the ouput is which bucket it has to go to


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)

    for i in range(numberofBuckets):
        arr[i] = sort.insertionSort(arr[i])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList
# in this case our bucket sort algorithm our has a O(n^2) complexity
# however if we use a more efficient sorting algorithm, bucket sort is great for if there is little variation between the elements
# bucket sort does use O(n) space complexity

lst = [2, 1, 7, 6, 5, 3, 4, 9, 8]
bucketSort(lst)
print(lst)