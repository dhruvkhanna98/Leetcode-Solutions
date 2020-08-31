# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.next_min = []
        self.helper(root)
        
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.next_min.pop()
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.next_min) > 0
    
    def helper(self, root: TreeNode): 
        
        # Base case 
        if not root: return
        
        self.helper(root.right)
        self.next_min.append(root.val)
        self.helper(root.left)

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()