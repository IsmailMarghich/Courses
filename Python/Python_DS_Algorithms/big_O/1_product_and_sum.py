def foo(array):
    sum = 0             #O(1)
    product = 1         #O(1)

    for i in array:     #O(n)
        sum += i        #O(1)
    
    for i in array:     #O(n)
        product *= i    #O(1)
    print(f'Sum = {str(sum)}, Product = {str(product)}') #O(1)
foo([1,2,3]) # The time complexity of this algorithm is O(n) because it doesnt meaningfully increase
#with each new O(n) or O(1)