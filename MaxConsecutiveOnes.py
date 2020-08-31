class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    
        # Base case 
        if len(nums) == 0: return 0
        res = 0
        curr = 0
        
        for num in nums: 
            if num == 1: 
                curr += 1
                if curr > res: res = curr
            else: 
                curr = 0

        return res
                
        