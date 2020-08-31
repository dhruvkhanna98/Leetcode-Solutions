class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Base case 
        if nums == []: return
        
        j = 0
        
        for i,n in enumerate(nums): 
            if n != 0: 
                temp = nums[j]
                nums[j] = n
                nums[i] = temp
                j += 1
            