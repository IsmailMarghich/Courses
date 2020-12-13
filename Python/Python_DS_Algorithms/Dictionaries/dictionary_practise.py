#creating a dictonary
dictionary = {'A':2}
print(dictionary)
#inserting and updating a dictionary
dictionary['A'] = 1
print(dictionary)
dictionary['B'] = 2
dictionary['C'] = 3
print(dictionary)
#traversing through a dictionary
for key in dictionary:
    print(key, dictionary[key])
#searching through a dictionary
def linearsearch(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
print(linearsearch(dictionary, 2))
#remove an element of a dictionary
dictionary.pop('A') #delete a specific key
print(dictionary)
dictionary.popitem() #deletes and returns
print(dictionary)
dictionary.clear() #delete everything
print(dictionary)
#dictionary methods
dictionary['A'] = 1
dictionary['B'] = 2
dictionary['C'] = 3
copy = dictionary.copy() #copying a dictionary
print(dictionary, copy)
newdict = {}.fromkeys(['A', 'B', 'C'], 0)#create a dictionary from keys and a value
print(newdict)
print(dictionary.get('D', 4)) #returns value of key, and if key doesnt exist, returns second argument as default value
print(dictionary.items()) #returns all items in dictionary
print(dictionary.keys()) #returns all keys in dictionary
print(dictionary.values()) #returns all values in dictionary
dictionary.setdefault('D', 4) #sets a default value for if a key doesnt exist
print(dictionary['D'])
update = {'D':'4'} #adds a key value pair if key doesnt exist, if key exist, update existing key with new value
dictionary.update(update)
print(dictionary)
#dictionary operations and functions
print('A' in dictionary) #in operator checks if value is in keys of dictionary
print(1 in dictionary.values()) #you can check values with in and using dictionary.values
print(all(dictionary)) #returns True if all values are either True or empty
print(any(dictionary)) #returns True if any element is True, and False if all elements are False or empty
print(sorted(dictionary, reverse=True)) #returns the input as a sorted datastructure, when reverse = True, it will be reversed
#we can also add a key= parameter to specify on which basis to sort
