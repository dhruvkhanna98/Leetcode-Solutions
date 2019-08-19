class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        n = len(A)
        
        # Base case 
        if n == 0: return True
        
        m_inc = True
        m_dec = True
        
        for i in range(n - 1):
            curr = A[i]
            next_e = A[i+1]
            
            if next_e < curr: m_inc = False
            if next_e > curr: m_dec = False
            
        return m_inc or m_dec
            
        