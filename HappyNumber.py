class Solution:
    def isHappy(self, n: int) -> bool:
        
        # Base case 
        if n == 1: 
            return True
        
        n_str = str(n)
        s = 0
        
        for i in range(10): 
            for c in n_str: 
                s += int(c) * int(c)
            if s == 1: 
                return True
            else: 
                n_str = str(s)
                s = 0
                
        
        return False
            
        
 