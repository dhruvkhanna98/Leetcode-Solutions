class Solution:
    def rotatedDigits(self, N: int) -> int:
        
        # Base case
        if N == 0:  return 0
        
        num_map = {"0" : "0",
                   "1" : "1", 
                   "2" : "5", 
                   "5" : "2",
                   "6" : " 9",
                   "8" : "8",
                   "9" : "6"}
        
        res = 0
        
        for i in range(N+1):
            num_str = str(i)
            num_r = ""
            num_good = True
            for s in num_str: 
                if s in num_map: 
                    num_r += num_map[s]
                else: 
                    num_good = False
                    break
            
            if num_str == num_r: 
                num_good = False
            
            if num_good: res += 1
        
        
        return res
                    
   
                