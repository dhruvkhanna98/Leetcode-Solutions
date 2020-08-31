class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # Base case 
        if num1 == "0" and num2 == "0": 
            return "0"
        elif num1 == "0" and num2 != "0":
            return num2
        elif num1 != "0" and num2 == "0":
            return num1
        
        n = len(num1)
        m = len(num2)
        
        n1 = 0
        n2 = 0
        
        for i in num1: 
            n1 += (ord(i) - 48) * (10**(n-1))
            n -= 1
        
        for j in num2: 
            n2 += (ord(j) - 48) * (10**(m-1))
            m -= 1
        
        return str(n1 + n2)
        
       
        
        
        