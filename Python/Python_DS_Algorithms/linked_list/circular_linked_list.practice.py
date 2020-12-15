#creating a circular linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):  # making our datastructure iterable
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
            
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return 'The circular single linked list has been made'
    def insertCSLL(self, value, location):
        if self.head == None:
            return 'linked list doesnt exist'
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return 'The node has been inserted'

    def traverseCSLL(self):  # function to traverse a linked list
        if self.head is None:            
            return 'The linked list is empty'
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    def searchCSLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return 'Node does not exist in this CSLL'


    def deleteNode(self, location):
        if self.head is None:  # function to delete a node in list
           return "The list does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                    
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head.next
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.tail.next = None
            self.head = None
            self.tail = None
            
circularSLL = CircularLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(4, -1)
circularSLL.insertCSLL(2, 2)
circularSLL.insertCSLL(3, 3)
circularSLL.insertCSLL(5, -1)
print([node.value for node in circularSLL])
circularSLL.traverseCSLL()
print(circularSLL.searchCSLL(3))
circularSLL.deleteNode(5)
print([node.value for node in circularSLL])
circularSLL.deleteEntireSLL()
print([node.value for node in circularSLL])
