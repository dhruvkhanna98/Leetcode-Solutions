# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
   
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        nodes = [] 
        self.inOrder(nodes, root)
        
        return nodes[k-1]
    
    def inOrder(self, nodes, root):
        
        # Base Case
        if not root: return 
        
        self.inOrder(nodes, root.left)
        nodes.append(root.val)
        self.inOrder(nodes, root.right)
        
       
        
       


        
       
            
        
        
        
        
        
        
    
        