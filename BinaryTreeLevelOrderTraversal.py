# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        # Base case 
        if not root: return []
        
        level_order = []
        level = 0
        
        def dfs(node, level):
            
            if len(level_order) == level: 
                level_order.append([])
            
            level_order[level].append(node.val)
            
            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)
        
        dfs(root, level)
        return level_order
        
   
       