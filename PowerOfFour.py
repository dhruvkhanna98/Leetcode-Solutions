class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        # Base case
        if num == 1: return True
        if num == 0 or num % 2 != 0: return False
        
        while num > 1: 
            num = num/4
        
        return num == 1
        