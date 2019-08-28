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
        
        def inOrder(root): 
            if not root: return
            
            # Left
            inOrder(root.left)
            # This if statement only runs for the smallest node (In order traveersal)
            if not self.tail: 
                # Saving the smallest Node
                self.head = root
            else: 
                # Setting current node top point to next of tail 
                self.tail.right = root
            # Setting current node as tail
            self.tail = root
            # Right
            inOrder(root.right)
        
        self.tail.right = self.head
        self.head.left = self.tail

        return self.head
        

    






 