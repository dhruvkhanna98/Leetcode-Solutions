class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:

        # Base Case 
        if nums == []: return 0
        
        curr = 1
        max_seq = -2**31
        prev = nums[0]

        for n in nums: 
            if n > prev: 
                curr += 1
            elif n <= prev: 
                curr = 1
            max_seq = max(curr, max_seq)
            prev = n
            
        return max_seq

