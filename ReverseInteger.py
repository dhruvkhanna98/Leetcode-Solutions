class Solution:
    def reverse(self, x: int) -> int:
        
        num = str(x)
        
        if x < 0:
            num = num[1:]
        
        # Reversing Number
        num = int(num[::-1])
                
        if num > 2**31-1 or num < -2**31:
            return 0
        elif x > 0: 
            return num
        else: 
            return -1 * num
        