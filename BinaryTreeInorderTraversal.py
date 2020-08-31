# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        output = []
        self.helper(output, root)
        
        return output
    
    def helper(self, output, root):
        
        # Base Case
        if not root: return
        
        self.helper(output, root.left)
        output.append(root.val)
        self.helper(output, root.right)
        
        
        
        