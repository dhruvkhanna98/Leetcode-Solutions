class Solution:
    def countAndSay(self, n: int) -> str:
        
        # Base case 
        if n == 1: return "1"

        res = "1"


        while n > 1:
            temp = ""
            prev = res[0]
            count = 0

            for c in res: 
                if c == prev: 
                    count += 1
                else: 
                    temp += str(count) + prev
                    prev = c
                    count = 1

            if count != 0: temp += str(count) + prev
            res = temp
            n -= 1

        return res
