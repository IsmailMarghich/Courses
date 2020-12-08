#create a recursive function that converts decimals to binary
def decimal_to_binary(num):
    assert int(num) == num, 'decimal must be an integer'
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * decimal_to_binary(int(num/2))
        # Divide the number by 2.
        #Get the integer quotient for the next iteration.
        #Get the remainder for the binary digit.
        #Repeat the steps until the quotient is equal to 0.
print(decimal_to_binary(10))
