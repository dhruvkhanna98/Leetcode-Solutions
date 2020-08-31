class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        o = [None] * n 
        
        for i in range(n):
            t = (i+k) % n 
            o[t] = nums[i]
        
        for i in range(n):
            nums[i] = o[i]
        