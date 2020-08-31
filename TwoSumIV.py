# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        # Base case 
        if not root: return False
        self.num_set = set()

        def helper(root): 
            if not root: return
            
            helper(root.left)
            self.num_set.add(root.val)
            helper(root.right)
        
        helper(root)
        
        for e in self.num_set: 
            target = k - e
            if target in self.num_set and target != e: return True
        
        return False
