# one dimensional array
array1d = [1,2,3,4,5,6]
#two dimensional array
array2d = [[1, 2, 3, 4, 5, 6], 
          [[1, 2, 3, 4, 5, 6], 
          [1, 2, 3, 4, 5, 6]]]
print(type(array2d))
from array import *
array1d = array('i', [1,2,3,4])
print(array1d)
array1d.insert(1, 5)
print(array1d)
array1d.remove(5)
print(array1d)