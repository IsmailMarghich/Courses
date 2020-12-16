class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None #this value refers to previous node

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The double linked list has been created'
    def insertNode(self, nodeValue, location):  # function to insert in linked list
        
        if self.head is None:  # if there are no nodes
            print('the node cannot be inserted')
        else:
            newNode = Node(nodeValue)
            if location == 0:  # if inserting before the head
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:  # if adding a tail
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:  # inserting any node in between head and tail
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    def traverseDLL(self):  # function to traverse a linked list
        if self.head is None:
            return 'The linked list is empty'
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next
    def reversetraverseDLL(self):  # function to traverse a linked list
        if self.head is None:
            return 'The linked list is empty'
        else:
            tempNode = self.tail
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.prev
    def searchDLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return 'the value does not exist in this list'

    def deleteNode(self, location):
        if self.head is None:  # function to delete a node in list
           return "There is no element in this list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print('The node has been deleted')
    def deleteEntireDLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            tempNode = self.head
            while tempNode is not None:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None

doublylinkedlist = DLinkedList()
doublylinkedlist.createDLL(1)
doublylinkedlist.insertNode(0, 0)
doublylinkedlist.insertNode(4, -1)
doublylinkedlist.insertNode(2, 2)
doublylinkedlist.insertNode(3, 3)

print([node.value for node in doublylinkedlist])
doublylinkedlist.traverseDLL()
doublylinkedlist.reversetraverseDLL()
print(doublylinkedlist.searchDLL(3))
doublylinkedlist.deleteNode(3)
print([node.value for node in doublylinkedlist])
doublylinkedlist.deleteEntireDLL()
print([node.value for node in doublylinkedlist])
