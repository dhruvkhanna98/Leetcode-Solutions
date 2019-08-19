class Solution:
    def isValid(self, s: str) -> bool:
        
        # Base case
        if len(s) == 0: 
            return True
        
        if len(s) % 2 != 0: 
            return False
        
        
        stack = list()
        
        for c in s: 
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            if len(stack) > 0:
                if c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
        
        if len(stack) > 0: 
            return False
        else: 
            return True
        
         
         