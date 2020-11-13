def fib(number): #create a function that generates fibonacci numbers using a generator.
    a = 0  #starting variables
    b = 1
    for i in range(number): #iterate how many times with the input
        yield a #hold the original a
        temp = a #create a temp for the new a
        a = b #number moves up
        b = temp + b #add the temp a to the second number b
    return b #return the second number when the iteration is done
for x in fib(10): 
    print(x)