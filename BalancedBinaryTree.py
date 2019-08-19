# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # Base Case 
        if not root: return True
        
        def height(root): 
            if not root: 
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        left = height(root.left)
        right = height(root.right)
        
        if abs(left - right) > 1: return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)