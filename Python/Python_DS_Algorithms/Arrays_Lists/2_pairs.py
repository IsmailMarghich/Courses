#write a program to find all pairs of integers who's sum is equal to a given number

def findpairs(list, target):
    for i in range(len(list)): #loop through list 2 times
        for j in range(i+1, len(list)):
            if list[i] == list[j]: # we dont want equal pairs
                continue
            elif list[i] + list[j] == target: #if pair equals target, print it out
                print(i, j)
my_list = [1,2,3,2,3,4,5,6]
findpairs(my_list, 6) #this prints the indexes of pairs which added together are the same value as target
