def sumofdigits(n): #returns the sum of all the digits in a number
    assert n >= 0 and int(n) == n, 'number must be a positive integer'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofdigits(int(n/10))

print(sumofdigits(1120)) # 1+1+2=4