class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        m = len(flowerbed)
        
        # Base case 
        if n == 0: return True
        
        if m == 1 and flowerbed[0] == 0: 
            return True
        elif m == 1 and flowerbed[0] == 1: 
            return False
    
        for i,f in enumerate(flowerbed):
            
            if f == 1: continue
            
            # Case for first element
            if i == 0 and flowerbed[i+1] == 0: 
                flowerbed[i] = 1 
                n -= 1
            # Case for last element
            elif i == (m - 1) and flowerbed[i-1] == 0: 
                flowerbed[i] = 1
                n -= 1
            elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0: 
                flowerbed[i] = 1
                n -= 1
            
            if n == 0: return True 
 

        return False