#a 2D matrix is given
#each cell has a cost associated with it for accessing
#we need to start from cel 0,0 and go till n-1,n-1 cell
#we are given total cost to reach the last cell
#find the number of ways to reach end of matrix with given total cost

#The idea is to check each cell cost to reach, and subtrac tthe cost of cells to the end
#and as long as this is under the maximum cost, its a valid way to reach the end
def numberOfPaths(twoDArray, row, col, cost):
    if cost < 0: #if cost is exceeded
        return 0
    elif row == 0 and col == 0: #base if we are at first cell
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0: #if we are at first row and we cant go to left
        return numberOfPaths(twoDArray, 0, col-1, cost - twoDArray[row][col] )
    elif col == 0: #if we are at the first column we cant go up
        return numberOfPaths(twoDArray, row-1, 0, cost - twoDArray[row][col] )
    else:
        op1 = numberOfPaths(twoDArray, row -1, col, cost - twoDArray[row][col] ) #otherwise we try finding the optimum by going backwards, up and left. until we run out of cost or we find valid way
        op2 = numberOfPaths(twoDArray, row, col-1, cost - twoDArray[row][col] )
        return op1 + op2


TwoDList = [[4,7,1,6],
           [5,7,3,9],
           [3,2,1,2],
           [7,1,6,3]
           ]

print(numberOfPaths(TwoDList, 3,3, 25))
