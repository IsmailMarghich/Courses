class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None  # this value refers to previous node


class CDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    def createCDLL(self, nodeValue):#  Creating Circular Doubly Linked List
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"


    def insertCDLL(self, value, location):# Inserting in Circular Doubly Linked List
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"


    def traverseCDLL(self):  # function to traverse a linked list
        if self.head is None:
            return 'The linked list is empty'
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
                
    def reversetraverseCDLL(self):  # function to traverse a linked list
        if self.head is None:
            return 'The linked list is empty'
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev
    def searchCDLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next: #make sure if we reach last node we stop, so we dont loop
                    return 'Node does not exist in this CSLL'
    def deleteNode(self, location):
        if self.head is None:  # function to delete a node in list
           return "There is no element in this list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print('The node has been deleted')

    def deleteEntireCDLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            return 'The circular doubly linked list has been deleted'

circularDLL = CDLinkedList()
circularDLL.createCDLL(0)
circularDLL.insertCDLL(5, -1)
circularDLL.insertCDLL(1, 1)
circularDLL.insertCDLL(2, 2)
circularDLL.insertCDLL(3, 3)
circularDLL.insertCDLL(4, 4)
print([node.value for node in circularDLL])
circularDLL.traverseCDLL()
circularDLL.reversetraverseCDLL()
print(circularDLL.searchCDLL(4))
circularDLL.deleteNode(4)
print([node.value for node in circularDLL])
circularDLL.deleteEntireCDLL()
print([node.value for node in circularDLL])
