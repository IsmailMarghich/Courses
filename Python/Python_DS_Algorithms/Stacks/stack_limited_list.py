#creating a stack using  a list, without limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x)for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):  # checking wether stack is empty
        if self.list == []:
            return True
        else:
            return False
    def isFull(self): #check wether list is full
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    def push(self, value):
        if self.isFull(): #if list is full
            return 'The stack is full'
        else: #otherwise append to list
            self.list.append(value)
            return 'The element has been added to the stack'

    def pop(self):
        if self.isEmpty():
            return 'There is not any element in stack'
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'There is not any element in stack'
        else:
            return self.list[len(self.list)-1] #get the last element by len -1 (because index start at 0)

    def delete(self):
        self.list = None


customStack = Stack(4)
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5) #max size is 4, so it cant get printed
print(customStack)
print(customStack.isFull())

