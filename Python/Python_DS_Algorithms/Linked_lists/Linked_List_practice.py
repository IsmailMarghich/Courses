from LinkedListClass import LinkedList
#1 Remove duplicates from an unsorted linked list
def removeduplicates(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll
customLL = LinkedList()
customLL.randomlist(10, 0, 10)
print(customLL)
removeduplicates(customLL)
print(customLL)