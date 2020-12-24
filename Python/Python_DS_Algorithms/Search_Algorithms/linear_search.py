#linear search
#a function that loops through an array and checks if the current array element is equal to target value
#if value is found, return index, otherwise return -1

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1
print(linearSearch([20,40,30,50,90], 50)) #returns 3 because 50 is at index 3
print(linearSearch([20, 40, 30, 50, 90], 100)) #returns -1 because 100 is not in array
#time complexity is O(N) because in worst case we iterate over whole list
#space complexity is O(1) because no extra space is required
#works for unsorted and sorted
