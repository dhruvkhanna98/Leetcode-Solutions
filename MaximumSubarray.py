class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # Base case
        if n == 0: return nums
        
        for i in range(1,len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
            
        return max(nums)
        
        
        
    
        
     