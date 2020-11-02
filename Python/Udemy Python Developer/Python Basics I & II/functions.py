#find the highest even in a list
highest = []
def highest_even(li):
    for i in li: #iterate through list
        if i % 2 == 0: #gets even numbers
            highest.append(i) #append each even number to the list
    return max(highest) #return maximum number in the list
print(highest_even([2,10,2,3,4,8,11]))