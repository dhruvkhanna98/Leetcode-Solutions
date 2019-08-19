class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        # Base case 
        if n == 0: 
            return -1
        elif n == 1: 
            if nums[0] == target: return 0
            else: return -1
        
        
            
        def findRotationIndex(start, end): 
            
            if nums[start] < nums[end]: 
                return 0
            
            while start <= end: 
                mid = (start + end) // 2
                if nums[mid] > nums[mid + 1]: 
                    return mid + 1
                elif nums[mid] < nums[start]: 
                    end = mid - 1
                else: 
                    start = mid + 1

        
        def BinarySearch(start, end): 
            
            while start <= end: 
                mid = (start + end) // 2
                
                if nums[mid] == target: 
                    return mid
                elif nums[mid] > target: 
                    end = mid - 1
                else: 
                    start = mid + 1
            
            return -1
        
        k = findRotationIndex(0, n-1)
        
        # No Rotation
        if k == 0: 
            return BinarySearch(0, n - 1)
    
        # Search the Right side
        if target < nums[0]: 
            return BinarySearch(k, n-1)
        # Search the left side
        else: 
            return BinarySearch(0, k-1)
            
        
        
 
        
            
            
        
        
        
        