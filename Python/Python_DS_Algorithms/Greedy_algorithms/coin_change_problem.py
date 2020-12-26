#You are given coins of different denominations and total amount of money
#find the minimum number of coins that you need to make up the given amount

#find the biggest coin that is less than total number
#add that coin to the result and subtract coin from total number

#if the amount of money becomes zero we print the result
#otherwise we repeat step 1 and 2


def coinChain(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins)-1 #grabbing largest coin at last index

    while True:
        coinValue = coins[index] #minus it with largest coin
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue: #if we cant subtract it, we move on to the next coin
            index -= 1

        if N == 0:
            break
coins = [1,2,5,20,50,100]
coinChain(201, coins)