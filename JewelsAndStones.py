class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        # Base case 
        if J == "" or S == "": return 0
        
        J = set(J)
        res = 0
        
        for s in S: 
            if s in J: res += 1
        
        return res
        
