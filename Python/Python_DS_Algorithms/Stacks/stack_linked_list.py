class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):  # making our datastructure iterable
        node = self.head
        while node:
            yield node
            node = node.next
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):   
        values = [str(x.value)for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    def push(self, value): #when we push we add the value to the beginning of the list
        node = Node(value)
        node.next = self.LinkedList.head #we set the next reference of the node to the head
        self.LinkedList.head = node #we make our new node our head
    def pop(self):
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            nodeValue = self.LinkedList.head.value #
            self.LinkedList.head = self.LinkedList.head.next #we set our head as the next node in the list
            return nodeValue
    def peek(self):
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            nodeValue = self.LinkedList.head.value #we grab the value of the head to get the top value
            return nodeValue
    def delete(self):
        self.LinkedList.head = None
customStack = Stack()
print(customStack.isEmpty())
customStack.push(3)
customStack.push(2)
customStack.push(1)
print(customStack)
print('-------')
customStack.pop()
print(customStack)
print(customStack.peek())
print('------')
customStack.delete()
print(customStack.isEmpty())