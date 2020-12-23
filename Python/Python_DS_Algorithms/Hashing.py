#Hashing is a method of storing and indexing data
#The idea behind hasing to allow large amounts of data to be indexed using keys
#These keys are commonly created by formulas, an example of this are the dictionaries in python
def mod(number, celNumber):
    return number % celNumber

def modASCII(string, celNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % celNumber
print(mod(740, 40))
print(modASCII('ABC', 24))
#Properties of good Hash functions:
#It distributes hash values uniforml across hash tables (to preverent collision)
#It has to use all the input data (to reduce chanceof collision)

#iF there is collision, there is different techniques we can use to solve the issue 
#Direct Chaining:
#Here we add a reference to a inkedlist to a cell where collision occurs, this way we can store multiple values in one cell
#-Never gets full, but huge linkedlists can cause performance leaks

#Open Adressing: Coliding elements are stored in other cells, during storage and lookup these are fround through a process called 'probing'
#- Easy implementation, but when hash table gets full, performance drops a lot
#Linear Probing
#We place a new key into the closet following empty cell
#Quadratic Probing
#We place a new key into a cell location where everytime a new collision occurs you add 1 to 1^2 for cell location
#e.g: 2 is full -> 2 + 1^2 = 3 new cell location, 3 is full -> 2+2^2 = 6 as new cell location
#Double hashing
#Here the intervals between insertions in the same memory cell is the cell location of the first hash + second hash times 2 = cell location

#Hash table getting full
#With direct chaining the hash table cant become full, as it can endlessly chain linkedlists 
#With open adressing the hash table will continue getting bigger and bigger, this will take a toll on the performance, but it wont become full

#if the input size is known we always use 'Open Adressing' because we know it will stay constantly performant since the hash table wont get full
#If we perform deletion, we use directon chaining, because if we used open adressing many empty cells from deletion will lower performance

#Pros of hashing:
#On average insertion/deletion/search operations O(1) time.

#Cons of hashing:
#When hash function is not good enough, intsertion/deletion/search can take up to O(N) time

#It will come down to wether your hashing function can achieve good enough performance with your data, otherwise you wanna use other datastructures like Trees and Linked Lists
#Hashing is used in the dictionary datastructure in python, check out that section for more