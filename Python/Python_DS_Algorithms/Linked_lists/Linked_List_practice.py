from LinkedListClass import Node
from LinkedListClass import LinkedList
#1 Remove duplicates from an unsorted linked list
def removeduplicates(ll):
    if ll.head is None: #check if list exists
        return
    else:
        currentNode = ll.head #attach to first node
        visited = set([currentNode.value]) #make a set where we add our duplicated values
        while currentNode.next:
            if currentNode.next.value in visited: #if node already in duplicate set
                currentNode.next = currentNode.next.next #continue
            else:
                visited.add(currentNode.next.value) #otherwise add it to duplicates set
                currentNode = currentNode.next #continue
        return ll
customLL = LinkedList()
customLL.randomlist(15, 0, 10)
print(customLL)
removeduplicates(customLL)
print(customLL)
print('-------------')
#2 Find the n'th element from the last element of singly linked list, i.e second element when u start from end of list counting to left
def nthToLast(ll,n):
    pointer1 = ll.head #have 2 points iterating over the list
    pointer2 = ll.head

    for i in range(n): #this will iterate pointer 2 until n
        if pointer2 is None:
            return None
        pointer2 = pointer2.next #keep iterating until end of list
    
    while pointer2: # keep iterating pointer 1 until pointer reaches end of list
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1
print(nthToLast(customLL, 3))# this function works by keeping n distance between pointer 1 and 2, 
#and when pointer 2 reaches the end, pointer 1 is at n'th element from last element in list
print('-------------')

# 3 create a function that takes value x, and arranges the list in a way where all values less than x come before than values greater or qual to x
def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        if curNode.value < x: #if the current node is smaller than x we add it to beginning of list
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode #if current node is greater or equal to x we add it at the end of list
            ll.tail = curNode
        curNode = nextNode
    if ll.tail.next is not None: #if all values are less than x we stop
        ll.tail.next = None
partition(customLL, 5)
print(customLL)
print('-------------')

#4 you have 2 numbers represented by a linked list, where each digit is a node in the linked list
#write a function which takes these digits, puts them together as numbers and add them together
#then make the result a linkedlist where each node is a digit
def sumlist(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10)) #gives 10s digit
        carry = result /10 #adds the first digit of 10s
    return ll

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()

llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sumlist(llA, llB))
print('-------------')

#5 Given two singly linked lists, determine if the two lists intersect and return the intersecting node
# if the k'th node of a linked list refers to the same node as the j'th node.next ereference in the other linkedlist , 
# and from then theyre referncing the same nodes, then they are intersecting

def intersection(llA, llB):
    if llA.tail is not llB.tail: #checking wether nodes intersect by just looking at tail
        return False
    lenA = len(llA) #getting the length of both lists
    lenB = len(llB)
    shorter = llA if lenA < lenB else llB #determine which one is smaller
    longer = llB if lenA < lenB else llA
    diff = len(longer) - len(shorter) #get the difference
    longerNode = longer.head #start with pointers at each list
    shorterNode = shorter.head

    for i in range(diff): #start iterating
        longerNode = longerNode.next

    while shorterNode is not longerNode: #keep comparing until u find the matching node
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode #return the node where the intersect starts


def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.randomlist(3, 0, 10)

llB = LinkedList()
llB.randomlist(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))
print('-------------')
