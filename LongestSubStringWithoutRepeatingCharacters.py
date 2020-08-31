## Examples
#  "" -> 0 
# "abc" -> 2 
# "aaabc" -> 3
# "abcaa" -> 3
# "aabca" -> 3
# ""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        # Base case 
        if len(s) == 0:
            return 0
        
        temp = ""
        max_len = 0
        
        for c in s:
            if c in temp:
                i = temp.find(c)
                temp = temp [i+1:]
            temp += c
            
            if len(temp) > max_len:
                max_len = len(temp)
        return max_len
            



                
            

    
        
        

        