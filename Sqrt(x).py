class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Base case 
        if x == 1 or x == 0: return x
        
        start = 0
        end = x 
        
        while start <= end: 
            mid = (start + end)//2
            temp = mid*mid
            
            if temp <= x < (mid + 1) * (mid + 1): return mid
            elif temp > x: end = mid - 1
            else: start = mid + 1
        
        
        
            
            
            
            
        