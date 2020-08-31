class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = list()
        product = 1
        num_zero = 0
        
        # Calculating Product
        for num in nums:
            if num != 0:
                product *= num
            else:
                num_zero += 1
            
        
        for i,n in enumerate(nums): 
            if num_zero == 0:
                output.append(product//n)
            elif num_zero == 1: 
                if n == 0:
                    output.append(product)
                else: 
                    output.append(0)
            else: 
                output.append(0)
                
           
        return output
            