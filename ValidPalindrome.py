class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Base case
        if s == "":
            return True
        
        s_palin = ""
        
        for c in s: 
            if c.isalnum(): 
                s_palin += c.lower()
        
        return s_palin == s_palin[::-1]