#Find the maximum product of 2 integers in an array
import numpy as np
my_array = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

def findmaxproduct(array):
    maxproduct = 0
    for i in range(len(array)): #loop through list twice so each number can be multiplied with each other
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxproduct: #compare pair multiplied with current max
                maxproduct = array[i] * array[j]
                pairs = str(array[i]) + ',' +  str(array[j]) #grab the pair which has max multiplication
    print(pairs) #print both
    print(maxproduct)
findmaxproduct(my_array)