import queue_linked_list as queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.data)
    inOrderTraversal(rootNode.right)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                customQueue.enqueue(root.value.left)
            if root.value.right is not None:
                customQueue.enqueue(root.value.right)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.left.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.left, nodeValue)
    else:
        if rootNode.right.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.right, nodeValue)
def getHeight(rootNode): #helper function to get the height of a node
    if not rootNode:
        return 0
    return rootNode.height
def rightRotate(disbalanceNode): #rotates the nodes to the right
    newRoot = disbalanceNode.left
    disbalanceNode.left = disbalanceNode.left.right
    newRoot.right = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right)) #we update the hieght of the node
    newRoot.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    return newRoot

def leftRotate(disbalanceNode):  # rotates the nodes to the left
    newRoot = disbalanceNode.right
    disbalanceNode.right = disbalanceNode.right.left
    newRoot.left = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    newRoot.height = 1 + max(getHeight(disbalanceNode.left), getHeight(disbalanceNode.right))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.left = insertNode(rootNode.left, nodeValue)
    else:
        rootNode.right = insertNode(rootNode.right, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.left.data: #LL
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.left.data: #LR
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.right.data: #RR
        return leftRotate(rootNode)
    if balance < -1  and nodeValue < rootNode.right.data: #RL
        rootNode.right = rightRotate(rootNode.right)
        leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.left is None:
        return rootNode
    return getMinValueNode(rootNode.left)

def deleteNode(rootNode,nodeValue): 
    if not rootNode: #these first bits of code are if there is no balacning required, same as binary tree deletion
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.left = deleteNode(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteNode(rootNode.right, nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        elif rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteNode(rootNode.right, temp.data)
    balance = getBalance(rootNode) #these if statements are for if there is a need for balancing
    if balance > 1 and getBalance(rootNode.left) <=0:  # LL
        return rightRotate(rootNode)

    if balance < -1 and getBalance(rootNode.right)<=0:  # RR
        return leftRotate(rootNode)

    if balance > 1 and getBalance(rootNode.left) < 0:  # LR
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)

    if balance < -1 and getBalance(rootNode.right) < 0:  # RL
        rootNode.right = rightRotate(rootNode.right)
        leftRotate(rootNode)
    return rootNode
def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return 'The AVL tree has been succesfully deleted'
AVLtree = AVLNode(5)
AVLtree = insertNode(AVLtree, 10)
AVLtree = insertNode(AVLtree, 15)
AVLtree = insertNode(AVLtree, 20)
levelOrderTraversal(AVLtree) #5 was the first rootNode, but there was an unbalance on the right side
#so the program rotates it to the left so 10 becomes the new rootNode
print('----after deleting 15--------')
AVLtree = deleteNode(AVLtree, 15)
levelOrderTraversal(AVLtree)
print(deleteAVL(AVLtree))
levelOrderTraversal(AVLtree)