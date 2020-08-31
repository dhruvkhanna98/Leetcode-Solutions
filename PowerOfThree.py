class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Base case
        if n == 1: 
            return True
        
        if n % 3 != 0 or n == 0: 
            return False
        
        num = 1
        
        while num < n: 
            num *= 3
        
        return num == n
        