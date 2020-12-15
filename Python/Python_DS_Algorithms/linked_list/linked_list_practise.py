#creating a linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self): #making our datastructure iterable
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLL(self, value, location): #function to insert in linked list
        newNode = Node(value)
        if self.head is None: #if there are no nodes
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #if inserting before the head
                newNode.next = self.head
                self.head = newNode
            elif location == -1: #if adding a tail
                newNode.next = None
                self.tail.next = newNode 
                self.tail = newNode
            else: #inserting any node in between head and tail
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    def traverseSSL(self): #function to traverse a linked list
        if self.head is None:
            return 'The linked list is empty'
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    def searchSSL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return 'the value does not exist in this list'
    def deleteNode(self, location):
        if self.head is None: #function to delete a node in list
           return "The list does not exist"
        else:
            if location == 0:
                if self.head == self.tail:    
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
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
            self.head = None
            self.tail = None


linkedlist = SLinkedList()
linkedlist.insertSLL(1, 0)
linkedlist.insertSLL(7, -1)
linkedlist.insertSLL(2, 1)
linkedlist.insertSLL(3, 2)
linkedlist.insertSLL(4, 3)
linkedlist.insertSLL(5, 4)
linkedlist.insertSLL(6, 5)
linkedlist.insertSLL(7, -1)

print([node.value for node in linkedlist])
linkedlist.deleteNode(0)
linkedlist.deleteEntireSLL()
print([node.value for node in linkedlist])
