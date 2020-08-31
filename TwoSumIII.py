class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        num_set = set()
        
        for num in self.nums: 
            target = value - num
            if target in num_set: return True
            
            num_set.add(num)
        
        return False
            
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)