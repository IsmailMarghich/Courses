#Given the weight and profits of N items
#Find the maximum profit within given capacity of C
#Items cannot be broken
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zoKnapsack(items, capacity, currentIndex):
    if capacity <=0 or currentIndex < 0 or currentIndex >= len(items): #basecase
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)#profit of current item
        profit2 = zoKnapsack(items, capacity, currentIndex+1) #profit of next item
        return max(profit1, profit2) #grab the highest one
    else:
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0))