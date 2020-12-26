# Implement a function to check if a binary tree is balanced. For the purposes of this question, 
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def helperBalanced(root): #helper function to check wether tree is balanced
    if root is None:
        return 0
    leftHeight = helperBalanced(root.left) #recursively look for imbalance
    if leftHeight == -1:
        return -1
    rightHeight = helperBalanced(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1
    
    return max(leftHeight, rightHeight) + 1 #return the difference, if balanced will return > -1


def isBalanced(root):
    return helperBalanced(root) > -1 #if the helper function returns something above -1, the tree is balanced



n1 = Node('N1')
n2 = Node('N2')
n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
print(isBalanced(n1)) #returns true because tree is balanced