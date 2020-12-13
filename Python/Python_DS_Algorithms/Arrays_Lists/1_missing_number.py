# find the missing number in an integer list of 1 to 100

my_list = [i for i in range(1, 100)]
my_list.remove(50) # 50 is missing number
def findmissing(list, n): #input list and size of list
    sumoflist = 100 * n / 2 #what the sum of a normal 1-100 list would be
    currentsum = sum(list)
    print(sumoflist - currentsum)
findmissing(my_list, 99)# our list has 99 entries because it misses 1 value
