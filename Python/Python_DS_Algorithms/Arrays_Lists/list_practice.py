my_list = [1,2,3,4,5]
print(my_list)
#accessing list
print(my_list[0])
#check if item exists in list
print(6 in my_list)
#iterate through a list
for i in my_list:
    print(i)
#updating/inserting through a list
my_list.append(6)
print(my_list)
my_list.insert(0, 0)
print(my_list)
#extending a list with another list
extend_list = [7, 8]
my_list.extend(extend_list)
print(my_list)
#slicing/deleting in a list
sliced_list = my_list[0:3]
print(sliced_list)
del sliced_list[2]
print(sliced_list)
sliced_list.remove(1)
print(sliced_list)
print(my_list)
#searching for an element in a list
if 9 in my_list:
    print(my_list[9])
else:
    print('element doesnt exist in list')
def linearsearch(list, value):
    for i in list:
        if i == value:
            return my_list.index(value)
    return 'The value could not be found in the list'
print(linearsearch(my_list, 7))
