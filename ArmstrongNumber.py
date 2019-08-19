class Solution:
    def isArmstrong(self, N: int) -> bool:
        
        N_str = str(N)
        k = len(N_str)
        n = 0
        
        for c in N_str: 
            n += int(c)**k
        
        return n == N
        