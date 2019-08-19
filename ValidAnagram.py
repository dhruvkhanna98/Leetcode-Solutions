class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n = len(s)
        m = len(t)
        
        # Base Case
        if n == 0 and m == 0: 
            return True
        
        if n != m: 
            return False
        
        s_map = collections.Counter(s)
        t_map = collections.Counter(t)
        
        for key in s_map: 
            if t_map.get(key, -1) == -1 or s_map[key] != t_map[key]: 
                return False
        
        return True
        
        
       
      
        

        
        
        
        
        
       
    