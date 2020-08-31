class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        # Base case 
        if len(A) == 0: 
            return A
        
        
        for i,a in enumerate(A): 
            n = len(a)
            start = 0
            end = n - 1
            
            while (start <= end): 
                
                # Flip
                t = a[start]
                a[start] = a[end]
                a[end] = t
                
                s = a[start]
                e = a[end]
                
                # Invert
                if s == 0: 
                    a[start] = 1
                else: 
                    a[start] = 0 
                
                if e == 0: 
                    a[end] = 1
                else: 
                    a[end] = 0 
                
                start += 1
                end -= 1
                
        return A
                
        
        
        
       
    
                
            
        
        