class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
                        
        # Base case
        if digits == "": return []
        
        digits_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        combs = [""]
        for digit in digits:
            temp = []
            for comb in combs:
                for letter in digits_dict[digit]:
                    temp.append(comb + letter)
            combs = temp
            
        return combs
                        
        