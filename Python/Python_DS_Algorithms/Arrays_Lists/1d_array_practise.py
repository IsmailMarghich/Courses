from array import *
# 1. Create an array and traverse
my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)
# 2. Access induvidual elements through indexes
print(my_array[0])
#3. Append any value to array using append() method
my_array.append(6)
print(my_array)
# 4. Insert value into array using insert method
my_array.insert(0, 0)
print(my_array)
# 5. Extend python array using extend() method
extendarray = array('i', [7]) #takes an iterable or array
my_array.extend(extendarray)
print(my_array)
# 6. Add items from list into array using fromlist() method
lst = [8]
my_array.fromlist(lst)
print(my_array)
# 7. Remove any array element using remove() method
my_array.remove(8)
print(my_array)
# 8. Remove last array element using pop() methid
my_array.pop(7)
print(my_array)
# 9. Fetch any element through its index using index() method
element = my_array.index(0)
print(element)
# 10. reverse a python array using reverse() method
my_array.reverse()
print(my_array)
my_array.reverse() #reverse it back
# 11. Get array buffer information through buffer_info() method
print(my_array.buffer_info()) # first output is memory location, and second is how large the array is
# 12. Get array number of occurrences of an element using count() method
print(my_array.count(6))
# 13. Convert an array to string using tostring() method
#stringarray  = my_array.tostring() Does not work in python 3.9
#print(stringarray)
#ints = array('i')
#ints.fromstring(stringarray)
#print(ints)

# 14. Convert array to a python list using tolist() method
print(my_array.tolist())
# 15. Slice elements from an array
print(my_array[0:3])