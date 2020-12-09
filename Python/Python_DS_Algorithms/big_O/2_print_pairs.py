def printPairs(array):
    for i in array: #   O(n) } becomes O(n^2)
        for j in array:#O(n) }
            print(f'{str(i)}  {str(j)}') #O(1)
printPairs([1,2,3]) #The time complexity of this algorithm is O(n^2)
#because of the nested loop