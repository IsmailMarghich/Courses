# Implement queue class which implements a queue using two stacks
class Stack():
  def __init__(self):
    self.list = []

  def __len__(self):
    return len(self.list)

  def push(self, item):
    self.list.append(item)

  def pop(self):
    if len(self.list) == 0:
      return None
    return self.list.pop()


class QueueviaStack():
  def __init__(self):
    self.inStack = Stack()
    self.outStack = Stack()

  def enqueue(self, item):
    self.inStack.push(item)

  def dequeue(self):
    while len(self.inStack):
      self.outStack.push(self.inStack.pop()) #were moving all our items in Instack to Outstack
    result = self.outStack.pop() #now we get the last element of outstack, which is the first element of Instack
    while len(self.outStack):
      self.inStack.push(self.outStack.pop()) #now we push the elemnts back to Instack
    return result


customQueue = QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
customQueue.enqueue(4)
print(customQueue.dequeue())
