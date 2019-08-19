class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Base case 
        if x < 0 or (x % 10 == 0 and x != 0): return False
        elif x < 9: return True

        rev_x = 0
        
        while rev_x < x: 
            rev_x = rev_x * 10 + x % 10
            x = x//10
            
        return x == rev_x or x == rev_x//10
        
        
    
        
        
        
        
        
        