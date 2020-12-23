import queue_linked_list as queue
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BSTNode(nodeValue)
        else:
            insertNode(rootNode.left, nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right = BSTNode(nodeValue)
        else:
            insertNode(rootNode.right, nodeValue)
    return 'The node has been succesfully inserted'

def preOrderTraversal(rootNode):  # Root Node -> Left subtree -> Right subtree
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)
def InOrderTraversal(rootNode):  # Left subtree -> Root Node -> Right subtree
    if not rootNode:
        return
    InOrderTraversal(rootNode.left)
    print(rootNode.data)
    InOrderTraversal(rootNode.right)
def postOrderTraversal(rootNode):  # Left subtree -> Right subtree -> Root node
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)
def levelOrderTraversal(rootNode):
    if not rootNode:  # if we reach the end of a branch, stop
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)


def binarysearch(rootNode, nodeValue):
    if rootNode.data == nodeValue: #check wether the node we start at is our target
        print('The value is found')
    elif nodeValue < rootNode.data: #check if target is less than node and then go left
        if rootNode.left.data == nodeValue:
            print('The value is found')
        else:
            binarysearch(rootNode.left, nodeValue)
    else: #if target isnt less than node, go right
        if rootNode.right.data == nodeValue:
            print('The value is found')
        else:
            binarysearch(rootNode.right, nodeValue) #this will recursively call itself until node is found 

def minValueNode(bst): #helper function to find lowest value
    current = bst
    while (current.left is not None):
        current = current.left
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp

        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = minValueNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    return rootNode
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return 'The binary search tree has been succesfully deleted'
binarysearchtree = BSTNode(None)
insertNode(binarysearchtree, 70)
insertNode(binarysearchtree, 50)
insertNode(binarysearchtree, 90)
insertNode(binarysearchtree, 30)
insertNode(binarysearchtree, 60)
insertNode(binarysearchtree, 80)
insertNode(binarysearchtree, 100)
insertNode(binarysearchtree, 20)
insertNode(binarysearchtree, 40)
preOrderTraversal(binarysearchtree)
print('----------')
InOrderTraversal(binarysearchtree)
print('---------')
postOrderTraversal(binarysearchtree)
print('-------------')
levelOrderTraversal(binarysearchtree)
binarysearch(binarysearchtree, 60)
print('--------')
deleteNode(binarysearchtree, 20)
levelOrderTraversal(binarysearchtree)
print(deleteBST(binarysearchtree))
print(binarysearchtree)