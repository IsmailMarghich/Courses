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
customLL.randomlist(10, 0, 10)
print(customLL)
removeduplicates(customLL)
print(customLL)