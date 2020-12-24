#merge sort is a divide and conquer algorithm
#we didivde input array into two halves and recursively keep halving until they become too small
#and then we merge the halves by sorting them


def merge(customList, l, m, r):
    n1 = m - l + 1 #we set our dimensions for the left and right half
    n2 = r - m

    L = [0] * (n1) #we divide our array into 2 sub arrays
    R = [0] * (n2)

    for i in range(0, n1): # we append our elements into these sub arrays
        L[i] = customList[l+i]

    for j in range(0, n2):
        R[j] = customList[m+1+j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2: #we merge them together into an array but sorted
        if L[i] <= R[j]: 
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1: #here we check if any element is left
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l, m) # T(n/2)
        mergeSort(customList, m+1, r) #T(n/2) #becomes O(NLogN)
        merge(customList, l, m, r)
    return customList
#merge sort is faster than other sorting algorithms like selection or insert sort because its time complexity is O(NLogN)
#however it does take O(n) space complexity because were sorting the halved arrays
#merge sort is stable
lst = [2, 1, 7, 6, 5, 3, 4, 9, 8]
mergeSort(lst, 0, 8) #our list starts from 0 and ends on index 8
print(lst)
