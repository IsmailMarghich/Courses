import numpy as np
# Creating a 2d array
my_array = np.array([
[11,15,10,6],
[10,14,11,5],
[12,17,12,8],
[15,18,14,9]])
print(my_array)
# inserting into a 2d array
inserted_array = np.insert(
    my_array, 0, [[1,2,3,4]], axis=1) # this inserts a column
print(inserted_array)
inserted_array = np.insert(
    my_array, 0, [[1, 2, 3, 4]], axis=0)  # this inserts a row
print(inserted_array)
# accessing an element of 2d array
print(my_array[0][0])
# traversing a 2d array
for i in my_array: #because 2d arrays have rows and columns, we have to use a nested loop
    for j in i:
        print(j)
# searching a 2d array
def linearsearch(array, element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == element:
                return 'element ' + str(element) +  ' has been found at index ' + str(i)+ ' ' +str(j)
    return 'the element is not found'
print(linearsearch(my_array, 9))

#deleting something in a 2d array
deleted_array = np.delete(my_array, 0, axis=1) #deletes column at index 0
print(deleted_array)
deleted_array = np.delete(my_array, 0, axis=0)  # deletes row at index 0
print(deleted_array)