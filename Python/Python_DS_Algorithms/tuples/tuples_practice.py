# creating a tuple
t = ('a','b','c','d','e')
print(t)
#accessing a tuple
print(t[0:3])
#traversing a tuple
for i in t:
    print(i)
#searching through a tuple
def linearsearch(tuple, element):
    for i in tuple:
        if i == element:
            return tuple.index(i)
    return 'The element does not exist in the tuple'
print(linearsearch(t, 'd'))
#tuple operations and functions
t2 = ('f','g','h','i','j')
print(t + t2) #concatenate
print(t * 2) #creates a new tuple and adds it
print('a' in t) #checks wether item is in tuple and returns True
tdouble = t + t
print(tdouble.count('a')) #counts occurences of element
print(t.index('a')) #returns the index of element
print(len(t)) #length of tuple
print(max(t)) #returns max value, in this case character with highest ASCII value
print(min(t)) #returns min value
print(tuple([1,2,3,4,5])) #convert list to tuple
#differences tuples and lists
#lists are mutable, tuples are immutable
#this means functions like sort(), reverse() and append() do not work on tuples, but they work on lists
#both datastructures can be stored within each other
tupleinlist = [(2,3)]
print(tupleinlist)
print(type(tupleinlist))
listintuple = ([1],)
print(listintuple)
print(type(listintuple))
#both can be nested
#iterating through a tuple is faster than list
#tuples can be used as immutable elements as keys for a dictionary
#if you have data that doesnt cahnge, implementing it in a tuple will gurantee it remains write protected
