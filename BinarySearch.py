class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        res = -1
        
        # Base case 
        if n == 0:
            return res
        
        start = 0 
        end = n - 1
        
        while (start <= end): 
            mid = (start + end + 1) // 2
            t = nums[mid]
            
            if t == target: 
                return mid
            elif target > t:
                start = mid + 1
            else: 
                end = mid - 1
        
        return res 
        
        
      
    
