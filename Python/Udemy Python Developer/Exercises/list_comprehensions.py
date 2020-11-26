some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)
#this program stores the duplicates
#based on the code above, remake this program with list comprehension
duplicates =[item for item in some_list if some_list.count(item)> 1] #append everything that which appears more than once time in the orignal list
print(set(duplicates)) #print it out as a set so it removes duplicates from the duplicate list