# Check if an array contains a number
import numpy as np
my_array = np.array(([i for i in range(1,21)])) #use comprehension to generate an array with numbers 1-20

def findnumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)
findnumber(my_array, 4) #prints index where an element in the array matches number

