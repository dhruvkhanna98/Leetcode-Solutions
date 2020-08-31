class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        if n == 0: return ["FizzBuzz"]
        
        res = []
        
        for num in range(1, n+1):
            num_3 = num % 3 == 0
            num_5 = num % 5 == 0
            
            if num_3 and num_5:
                res.append("FizzBuzz")
            elif num_3 and  not num_5: 
                res.append("Fizz")
            elif not num_3 and num_5:
                res.append("Buzz")
            else: 
                res.append(str(num))
        
        return res
        