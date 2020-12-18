from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
    def __iter__(self):
            CurNode = self.head
            while CurNode:
                yield CurNode
                CurNode = CurNode.next
    def __str__(self):
        values = [str(x.value)for x in self] 
        return  '->'.join(values)
    
    def __len__(self):
        node = self.head
        result = 0
        while node:
            result += 1
            node = node.next
        return result
    def add(self, value):
        if self.head == None:
            NewNode = Node(value)
            self.head = NewNode
            self.tail = NewNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    def randomlist(self, n, min, max):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min, max))
        return self

