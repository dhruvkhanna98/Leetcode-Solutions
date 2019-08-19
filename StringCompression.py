class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        
        # Base case 
        if n == 0: return 0
        elif n == 1: return 1
        
        counts = ""
        curr = 0
        prev = chars[0]
        
        for c in chars: 
            if c == prev: 
                curr += 1
            else:
                if curr == 1: 
                    counts += prev
                else: 
                    counts += prev
                    counts += str(curr)
                curr = 1
                prev = c
                
        if curr == 1: 
            counts += prev
        else: 
            counts += prev
            counts += str(curr)
        
        
        for i,c in enumerate(counts):
            chars[i] = c
        
        return len(counts)
        