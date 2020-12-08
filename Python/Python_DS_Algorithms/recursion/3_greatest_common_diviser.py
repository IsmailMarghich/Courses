def gcd(a, b): #create a recursive function to calculate the greatest commmon divisor of 2 numbers
    assert int(a) ==  a and int(b) == b, 'the number must be an integer'
    if a < 0:
        a = a * - 1
    if b < 0:
        b = b * -1
    if b == 0:
        return a
    return gcd(b, a % b) #the euclidian algorithm is used here
print(gcd(48, 18)) # 6