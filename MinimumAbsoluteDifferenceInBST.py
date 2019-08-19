# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        # Base case 
        if not root: return None
        
        self.res = 2**31 - 1
        self.prev = -2**31
     
        def inOrder(root, prev, res):
            if not root: return
            
            inOrder(root.left, self.prev, self.res)
            curr = root.val - self.prev
            if curr < self.res: self.res = curr
            self.prev = root.val
            inOrder(root.right, self.prev, self.res)
    
        
        inOrder(root, self.prev, self.res)
        return self.res
        
        
  