# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        n = len(nums)
        
        # Base Case
        if n == 0: 
            return None
        
        start = 0
        end = n-1
        mid = (start + end + 1)//2
        val = nums[mid]
        
        root = TreeNode(val)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
            
        