# #map, filter, zip, and reduce
from functools import reduce
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize(item):
    return item.upper() #return the iterable capitalized
print(list(map(capitalize,my_pets)))
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(list(zip(my_strings, (sorted(my_numbers))))) #zip the lists together, and sort my_numbers
#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def filterscore(item):
    return item > 50 #our predicate for the filter
print(list(filter(filterscore, scores)))
#4 Combine all of the numbers that are in a list on this file 
# using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item #adds up every new iterable with the initial
print(reduce(accumulator, my_numbers + scores, 0))
