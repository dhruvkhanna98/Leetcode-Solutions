class Solution:
    def myAtoi(self, s: str) -> int:
        
        n = len(s)
        s_neg = 0
        s_pos = 0
        
        s = s.lstrip(" ")
        
        # Base Case 
        if n == 0: 
            return 0
        
        s_o = ""
        
        for c in s: 

            if c.isdigit(): 
                s_o += c
            elif c.isalpha() or c == "." or c == " " or (len(s_o) > 0 and (c == "-" or c == "+")):
                break
            elif c == "+": 
                s_pos += 1
            elif c == "-": 
                s_neg += 1
            
            if (s_pos > 0 and s_neg > 0) or (s_pos > 1 or s_neg > 1):
                return 0
                    
        
        if s_o == "": 
            return 0
                

        s_o = int(s_o)
        
        if s_neg == 1: 
            s_o = -1 * s_o
        
        int_max = (2**(31)-1)
        int_min = -2**(31)
        
        
        if s_o >= int_min and s_o <= int_max: 
            return s_o
        elif s_o < int_min:
            return int_min
        else: 
            return int_max
            
       