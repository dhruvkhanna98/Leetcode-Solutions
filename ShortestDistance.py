class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        word1_idx = []
        word2_idx = []
        
        for i,word in enumerate(words): 
            if word == word1: word1_idx.append(i)
            elif word == word2: word2_idx.append(i)
        
        res = 2**31 - 1
        
        for i in word1_idx: 
            for j in word2_idx: 
                res = min(res, abs(i-j))
        
        return res