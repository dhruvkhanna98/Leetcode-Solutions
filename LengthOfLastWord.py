class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # Base case
        if s == "" or s == " ": return 0
        s = s.rstrip(" ")
        
        n = len(s)
        res = 0
        
        for i in range(n-1, -1, -1): 
            if s[i] == " ": break
            res += 1
        
        return res