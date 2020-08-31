class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        S = S.split("-")
        temp = ""
        for s in S: 
            temp += s
        S = temp
        if len(S) == 0: return ""
        res = ""
        
        if len(S) % K == 0: 
            count = 0
            for i,s in enumerate(S):
                res += s.upper()
                count += 1
                if count == K and i < len(S) - 1: 
                    count = 0
                    res += "-"
        else: 
            count = 0
            S = S[::-1]
            for s in S:
                res += s.upper()
                count += 1
                if count == K: 
                    count = 0
                    res += "-"
            res = res[::-1]
        
        return res