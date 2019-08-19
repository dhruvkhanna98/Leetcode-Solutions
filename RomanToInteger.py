class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Base case
        if s == "": 
            return 0
        
        num_dict = {"I" : 1,
                    "V" : 5,
                    "X" : 10, 
                    "L" : 50,
                    "C" : 100, 
                    "D" : 500, 
                    "M" : 1000
                   }
        
        num = 0 
        skip = False
        
        for i,c in enumerate(s):

            temp = c
            
            if skip: 
                skip = False
                continue
            
            if i+1 < len(s): 
                temp += s[i+1]

            if temp == "IV" or temp == "IX" or temp == "XL" or temp == "XC" or temp == "CD" or temp == "CM": 
                num += num_dict[temp[1]] - num_dict[temp[0]]
                skip = True
            else: 
                num += num_dict[temp]
        
        return num