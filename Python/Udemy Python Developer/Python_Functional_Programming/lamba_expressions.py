#create a lambda expression that will square a list
my_list = [1,2,3]
print(list(map(lambda x: x**2, my_list))) #each item in the list is x, and it gets squared
#sort a list based on the lowest value in a tuple
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1]) #we want the second value in the tumple, so we define x as the second,(1) index of our tuple
print(a)