#Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree. 
# You may assume that each node has a link to its parent.
#Note that we HAVE to use in order traversal
from typing import MappingView


class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node
       return node
#in order traversal is Left -> root -> right
#if right subtree of node is Not None, successor lies in right subtree
#if right subtree of node is None, successor lies in one of the ancestors


def minValue(node): #helper function to find minimum value
    current = node
    while (current is not None):
        if current.left is None:
            break
        current = current.left
    return current
def inOrderSuccessor(root, n):
    if n.right is not None:
        # if right subtree of node is Not None, successor lies in right subtree
        return minValue(n.right)
        #if right subtree of node is None, successor lies in one of the ancestors
    
    p = n.parent
    while p is not None: #loop to find parent
        if n != p.right:
            break
        n = p
        p = p.parent
    return p

root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.left.right #3

successor = inOrderSuccessor(root, temp)
if successor is not None:
    print('in order succesor of',temp.data, 'is', successor.data)
else:
    print('inorder succesor does not exist')