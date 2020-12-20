# Imagine a stack of plates that falls when there is too much plates on the stack, in this case we would make a new stack if the current stack exceeds a height limit
# Create a datastructure that holds stacks, when a stack reaches its size limit, the datastructure will create a new stack
# Also add a function where u can pop at a specific stack
class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity: #if the current stack is full, then append it to a new one
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None


customStack = PlateStack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop_at(1))
