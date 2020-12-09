def powersOf2(n): # This algorithm calculates the powers of 2 under a certain number N
    if n < 1:
        return 0        
    elif n == 1:        #O(1)
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2)) #O(LogN)
        curr = prev*2
        print(curr)      #O(1)
        return curr
#The complexity of this algorithm is LogN becuase the numbers constantly get halved