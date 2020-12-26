#Given a set of items, each with a weight and value, determine the number of each to include in a collection
# so that the total weight is less than or equal to a given limit and the total value is as large as possible
# e.g we have a bunch of boxes of different amounts and weights, we try to find the highest density first and it and continue for other boxes
# in this case we want as much value (amount of items) in as little weight as possible

#-calculate the density or ratio for each item
#-sort items based on this ratio
#-take items with the highest ratio until weight allows
#-add last item as fractionaly as possible

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsackMethod(items, capacity):
    items.sort(key=lambda  x: x.ratio, reverse = True) #sort the items based on ratio
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity: #if whole item can be added, add it
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedweight = capacity - usedCapacity #otherwise we only add a fraction that still fits
            value = i.ratio * unusedweight
            usedCapacity += unusedweight
            totalValue += value
        if usedCapacity == capacity: #if capacity is reached we stop and print total value
            break
    print('total value obtained: ' + str(totalValue))


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)
