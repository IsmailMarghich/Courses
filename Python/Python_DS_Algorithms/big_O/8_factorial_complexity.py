def factorial(n):               #M(n)
    if n < 0:
        return -1
    elif n == 0:               # O(1)
        return 1
    else:
        return n * factorial(n-1) #M(n-1)


print(factorial(3))
#M(0) = O(1)
#M(N) = O(N) because recursive function just calls itself once