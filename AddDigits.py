class Solution:
    def addDigits(self, num: int) -> int:
        
        num_str = str(num)
        
        # Base Case 
        if len(num_str) == 1:
            return int(num_str)
        
        s = 0
        
        for c in num_str: 
            s += int(c)
        
        return self.addDigits(s)
            
        
        