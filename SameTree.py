# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # Base case 
        if not p and not q:
            return True 
        elif (not p and q) or (p and not q): 
            return False
        
        if p.val != q.val: 
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
 
        return left and right
        