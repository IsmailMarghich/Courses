def power(base, exp): #create a recursive function that returns the power of a number
    assert exp >= 0 and int(exp) == exp, 'the exponent must be a positive integer'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)
print(power(2, 3)) # 2^3 = 8