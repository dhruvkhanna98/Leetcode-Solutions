# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        n = len(nums)
        
        # Base case 
        if n == 0: return None
        
        m = max(nums)
        i = nums.index(m)
        
        root = TreeNode(m)
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i+1:])
        
        return root
        