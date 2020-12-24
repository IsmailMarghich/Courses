#in binary search we try to eliminate half of the remaining elements in a sorted array
#we check wether our target is less or greater than the middle element, and this way we can find it efficiently
#without needing to iterate over whole array, downside is that it only works for sorted arrays
import math
def binarSearch(array, value): 
    start = 0 #here we try to find the start middle and end of array
    end = len(array) - 1
    middle = math.floor((start+end)/2) 
    print(start, middle, end)
    while not(array[middle]==value): #until our middel meets the target value
        if value < array[middle]: #if our value is smaller than array
            end = middle - 1 #the target value is between start and middle, so we move end
        else: #otherwise value > middle, then we move our start to after middle
            start = middle + 1
        middle = math.floor((start+end)/2) #each time we calculate a new middle
        print(start, middle, end)
    if array[middle] == value: # we make sure our middle is our target and then return it(to prevent infinite loop)
        return middle
    else:
        return -1 #return -1 if cant find the target
customarray = [8,9,12,15,17,19,20,21,28]
print(binarSearch(customarray, 15))
#because we are halving the array each time, our time complexity is O(LogN)
