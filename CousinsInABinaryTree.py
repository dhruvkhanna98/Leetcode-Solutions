# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        # Base case 
        if not root: return False
        
        parent_map = dict()
        parent_map[root.val] = root.val
        depth_map = dict()
        depth_map[root.val] = 0
        
        def dfs(root): 
            if not root: return
            # Anotating parent and depth
            if root.left: 
                parent_map[root.left.val] = root.val
                depth_map[root.left.val] = depth_map[root.val] + 1
            if root.right: 
                parent_map[root.right.val] = root.val
                depth_map[root.right.val] = depth_map[root.val] + 1
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return depth_map[x] == depth_map[y] and parent_map[x] != parent_map[y]
            
            
        
        
        
    
            
            
            
        
        
        
        
        
        
        
        
        
        
        