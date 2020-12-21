import queue_linked_list as queue #here we import our queue class implemented with a linked list in another file
class TreeNode: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


binarytree = TreeNode('Drinks')
leftchild = TreeNode('Hot')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
rightchild = TreeNode('Cold')
binarytree.left = leftchild
binarytree.right = rightchild
leftchild.left = tea
leftchild.right = coffee
#Root Node -> Left subtree -> Right subtree
def preOrderTraversal(rootNode): #this function traverses through the tree via recursion
    if not rootNode: #if we reach the end of a branch, stop
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)
preOrderTraversal(binarytree)

print('----------')
#Left subtree -> Root Node -> Right subtree
def InOrderTraversal(rootNode):# this function traverses through the tree via recursion
    if not rootNode:  # if we reach the end of a branch, stop
        return
    else:
        InOrderTraversal(rootNode.left)
        print(rootNode.data)
        InOrderTraversal(rootNode.right)
InOrderTraversal(binarytree)

print('------------')

# Left subtree -> Right subtree -> Root node
def PostOrderTraversal(rootNode):  # this function traverses through the tree via recursion
    if not rootNode:  # if we reach the end of a branch, stop
        return
    else:
        PostOrderTraversal(rootNode.left)
        PostOrderTraversal(rootNode.right)
        print(rootNode.data)
      
PostOrderTraversal(binarytree)

print('-----------')
def LevelOrderTraversal(rootNode): #here we constantly queue and dequeue the values of the tree to do level order traversal
    if not rootNode:  # if we reach the end of a branch, stop
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)
LevelOrderTraversal(binarytree)
    
def search(rootNode, nodeValue):
    if not rootNode:
        return 'The binary tree does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return 'The node exists in binary tree'
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)

            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)
        return 'The node could not be found in the binary tree'
print(search(binarytree, 'Coffee'))

def insertNode(rootNode, NewNode): #function to insert node
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue() #we use level traversal to find a level with empty spots
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left is not None:
                customQueue.enqueue(root.value.left) #first we add to left (because level traversal is left to right)
            else:
                root.value.left = newNode
                return 'Successfully inserted'
            if root.value.right is not None:
                customQueue.enqueue(root.value.right) #if left is full, we add to right
            else:
                root.value.right = newNode
                return 'Successfully inserted'
#newNode = TreeNode('Cola')
#print(insertNode(binarytree, newNode))
#print('----------')
#LevelOrderTraversal(binarytree)

def getDeepestNode(rootNode): #this function will bring us the deepest node in the tree
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left is not None:
                customQueue.enqueue(root.value.left) 

            if root.value.right is not None:
                customQueue.enqueue(root.value.right)
        deepestNode = root.value
        return deepestNode
deepestNode = getDeepestNode(binarytree)
print('--------')
print(deepestNode.data)

def deleteDeepestNode(rootNode, dNode): #this function will delete the deepest node from the tree
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.right:
                if root.value.right is dNode:
                    root.value.right = None
                    return
                else:
                    customQueue.enqueue(root.value.right)
            if root.value.left:
                if root.value.left is dNode:
                    root.value.left = None
                    return
                else:
                    customQueue.enqueue(root.value.left)
def deleteNode(rootNode, node): #this function will use the other functions to delete a node from the tree
    if not rootNode:
        return 'The binary does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return 'The node has been succesfully deleted'
            if (root.value.left is not None):
                customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                customQueue.enqueue(root.value.right)
        return 'Failed to delete'
print('--------')
deleteNode(binarytree, 'Tea')
LevelOrderTraversal(binarytree)

def deleteTree(rootNode): #this function will delete the whole tree by setting the rootnode, rootnode.left and rootnode.right to None
    if not rootNode:
        return
    else:
        rootNode.data = None
        rootNode.left = None
        rootNode.right = None
        return 'The binary tree has been deleted'
deleteTree(binarytree)
print('----------')
LevelOrderTraversal(binarytree) #prints none because binary tree is now empty