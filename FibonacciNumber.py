class Solution:
    def fib(self, N: int) -> int:
        
        f = [0, 1]
        
        while (len(f) < N + 1):
            f.append(f[-1] + f[-2])
            
        return f[N]