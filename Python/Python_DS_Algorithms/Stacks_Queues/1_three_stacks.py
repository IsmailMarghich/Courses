# Describe how you could use a single python list to implement three stacks
""" 
for stack 1 [0][1][2] -> [0, n/3]
for stack 2 [4][5][6] -> [n/3, 2n/3]
for stack 1 [7][8][9] -> [2n/3,n]
 """

class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.custlist = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize
    
    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
    
    def index(self, stacknum): #returns index of top of a list
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum]- 1
    
    def push(self, value, stacknum):
        if self.isFull(stacknum):
            return 'Stack is full'
        else:
            self.sizes[stacknum] += 1
            self.custlist[self.index(stacknum)] = value
    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return 'Stack is full'
        else:
            value = self.custlist[self.index(stacknum)]
            self.custlist[self.index(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return 'Stack is empty'
        else:
            value = self.custlist[self.index(stacknum)]
            return value
threestack = MultiStack(6)
print(threestack.isFull(1))
print(threestack.isEmpty(1))
threestack.push(1, 0)
threestack.push(2, 0)
threestack.push(3, 1)
print(threestack.peek(1))
threestack.pop(0)
print(threestack.peek(0))