## Examples
# Base Case: n=0 -> 1
# Example 1: x=2.000, n=1 -> 2
# Example 2: x=1.00, n=-2 -> 1
# Example 3: x=2, n=-2 -> -1/4
# Example 4: x=2, n=4 -> 16

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        # Base case
        if n == 0: 
            return 1
        
        n_neg = False
        
        # Checking if n is Negative
        if n < 0: 
            n_neg = True
            n = n * -1

        
        x_n = self.myPow(x, n // 2)
        x_n = x_n * x_n
        
        # Checking if n is Odd
        if n % 2 != 0: 
            x_n = x * x_n
        
        if n_neg: 
            return 1 / x_n
        else: 
            return x_n
            