#creating a stack using  a list, without limit

class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x)for x in self.list]
        return  '\n'.join(values)
    
    def isEmpty(self): #checking wether stack is empty
        if self.list == []:
            return True
        else:
            return False
    def push(self, value):
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
            return self.list[len(self.list)-1]
    def delete(self):
        self.list = None
customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
customStack.pop()
print(customStack)
print(customStack.peek())
customStack.delete()