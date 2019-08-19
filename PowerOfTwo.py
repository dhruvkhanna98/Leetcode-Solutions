class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # Base case
        if n == 1: 
            return True 
        
        if n % 2 != 0 or n == 0: 
            return False
        
        num = 1
        while num < n: 
            num *= 2
        
        return num == n
        