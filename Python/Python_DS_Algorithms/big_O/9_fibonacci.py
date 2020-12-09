def allFib(n):
    for i in range(n):                       # O(N)
        print(str(i)+":, " + str(fib(i)))    # O(2^N)   

def fib(n):
    if n <= 0:
        return 0
    elif n == 1: #recursive that gets called twice -> O(2^N)
        return 1
    return fib(n-1) + fib(n-2)
# O(2^N) + O(2^N) = O(2^N)
 
