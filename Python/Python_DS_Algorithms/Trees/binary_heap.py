
class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
def peekHeap(rootNode):
        if not rootNode:
            return
        else:
            return rootNode.customList[1]
def sizeofHeap(rootNode):
        if not rootNode:
            return
        else:
            return rootNode.heapSize
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1 ):
            print(rootNode.customList[i])
def heapifyTreeInsert(rootNode, index, heapType): #this function will make sure to turn our list into a min or max heap after an insert
    parentIndex = int(index/2)
    if index <=1:
        return
    if heapType == 'Min':
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex)
    elif heapType == 'Max':
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType): #function to insert node, we heapify after each insert so its sorted like a min or max heap
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return 'The binary heap is full'
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)


def extractNode(rootNode, heapType): #function to extract a node from heap, at the end it will heapify the tree so it stays a min or max heap
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode
def deleteEntireHeap(rootNode):
    rootNode.customList = None
    return 'The heap has been deleted'
binaryheap = Heap(5)
insertNode(binaryheap, 4, 'Max')
insertNode(binaryheap, 5, 'Max')
insertNode(binaryheap, 2, 'Max')
insertNode(binaryheap, 1, 'Max')
extractNode(binaryheap, 'Max')
levelOrderTraversal(binaryheap)
deleteEntireHeap(binaryheap)
levelOrderTraversal(binaryheap) #this will error because the heap is empty
