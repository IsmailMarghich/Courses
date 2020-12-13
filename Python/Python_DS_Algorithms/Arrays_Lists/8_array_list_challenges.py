#1 create a function called middle that returns a new list that contains all but the first and last elements
def middle(list):
    return list[1:-1]
print(middle([1,2,3]))
#2 given a 2d list, calculate the sum of digital elements (top left to bottom right)
def sumDiagonal(a):
    return a[0][0] + a[1][1] + a[2][2]
print(sumDiagonal([[1,2,3],[4,5,6], [7,8,9]]))
#3 given a list, print the highest and second highest element
def firstSecond(list):
    first = max(list)
    list.remove(max(list))
    second = max(list)
    return (first, second)
print(firstSecond([1,2,3]))
