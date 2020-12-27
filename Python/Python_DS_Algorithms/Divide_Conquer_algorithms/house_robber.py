#Given N number of houses along the street with some amount of money
#Find the maximum amount of money that can be stolen
#Adjacent houses cannot be stolen

#because we cannot rob adjacent houses, we have to make sure the house we do pick, is the most amount of money

def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2) #steal first and third house
        skipFirstHouse = houseRobber(houses, currentIndex+1) #skip first house and rob second
        return max(stealFirstHouse, skipFirstHouse)

houses = [6,7,1,30,8,2,4]
print(houseRobber(houses, 0))