class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # Base case 
        if num == 0 or num == 1: return True
        
        start = 0 
        end = num 
        
        while start <= end: 
            mid = (start + end) // 2
            
            if mid*mid > num: 
                end = mid - 1
            elif mid*mid < num: 
                start = mid + 1
            else: 
                return True
        
        return False