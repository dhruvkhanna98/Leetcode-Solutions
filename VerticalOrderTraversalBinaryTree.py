# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        # Base case 
        if not root: return []
        
        nodes = collections.defaultdict(lambda: collections.defaultdict(list))
        
        def dfs(root, x, y): 
            if not root:
                return
            
            nodes[x][y].append(root.val)
            dfs(root.left, x-1, y+1)
            dfs(root.right, x+1, y+1)
        
        dfs(root, 0, 0)
        res = [] 
        
        for x in sorted(nodes): 
            temp = []
            for y in sorted(nodes[x]):
                temp.extend(sorted(nodes[x][y]))
            res.append(temp)

        return res
        
  