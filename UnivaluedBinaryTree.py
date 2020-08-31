# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        # Base case
        if not root: return True
        
        node_set = set()
        
        def bfs(root): 
            if not root: return
            
            bfs(root.left)
            node_set.add(root.val)
            bfs(root.right)
        
        bfs(root)
        return len(node_set) == 1

                
        