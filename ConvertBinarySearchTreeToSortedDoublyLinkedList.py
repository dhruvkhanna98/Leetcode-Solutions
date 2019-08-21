"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        # Base case
        if not root: return None
        
        self.head, self.tail = None, None

        def helper(root): 
            if not root: return
            
            # left
            helper(root.left)
            
            # root 
            if self.tail:
                # link the previous node (self.tail)
                # with the current one (node)
                self.tail.right = root
                root.left = self.tail
            else:
                # keep the smallest node
                # to close DLL later on
                self.head = root        
            self.tail = root
            
            # right
            helper(root.right)
                
        
        helper(root)
        self.head.left = self.tail
        self.tail.right = self.head 

        return self.head






 