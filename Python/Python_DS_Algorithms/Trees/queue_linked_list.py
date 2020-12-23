class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):  # making our datastructure iterable
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedlist.head == None: #if there is no elements in queue
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
    def dequeue(self):
        if self.isEmpty():
            return 'There is no element in the queue'
        else:
            tempNode = self.linkedlist.head 
            if self.linkedlist.head == self.linkedlist.tail: #if this is the only element in queue
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempNode
    def peek(self):
        if self.isEmpty():
            return 'There is no element in the queue'
        else:
            return self.linkedlist.head
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None
