class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # Base case 
        if len(nums) == 0: 
            return nums
        
        n = len(nums)
        nums = set(nums)
        o = []
   
        for i in range(1, n+1):
            if i not in nums:
                o.append(i)
        
        return o
                