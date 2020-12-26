#implement a function to check if binary tree is a binary search tree
#a binary tree is a binary search if the left subtree of a node contains only nodes smaller than this node
# and if the right subtree of a node contains only nodes smaller than this node
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def helper(node, minValue = float('-inf'), maxValue = float('inf')):
    if not node:
        return True
    val = node.val
    if val <= minValue or val >= maxValue: #checker wether its outside of min and max
        return False
    
    if not helper(node.right, val, maxValue): #check wether right child is outside of boundary
        return False

    if not helper(node.left, minValue, val): #check wether left child is outside of boundary
        return False
    
    return True
def isValidBST(root):
    return helper(root)
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4) #this tree is binary search tree
print(isValidBST(root1)) #returns true

root2 = TreeNode(4)
root2.left = TreeNode(1)
root2.right = TreeNode(3)  # this tree is not balanced
print(isValidBST(root1))  # returns False
