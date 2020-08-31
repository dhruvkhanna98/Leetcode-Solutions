class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str1 = str.split(" ")
        word_map = dict()
        word_set = set()
        
        if len(pattern) != len(str1): return False
        
        for i in range(len(pattern)):
            if pattern[i] not in word_map and str1[i] not in word_set:
                word_map[pattern[i]] = str1[i]
                word_set.add(str1[i])
            elif pattern[i] not in word_map and str1[i] in word_set: return False
            else:
                if word_map[pattern[i]] != str1[i]: return False
        
        return True
        