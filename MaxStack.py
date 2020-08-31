class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
      
        

    def pop(self) -> int:
        return self.data.pop()
       
        

    def top(self) -> int:
        return self.data[-1]
        
        

    def peekMax(self) -> int:
        
        max_num = -1 * 10**7
        
        for n in self.data: 
            if n > max_num: 
                max_num = n
        
        return max_num
            

    def popMax(self) -> int:
        
        max_num = self.peekMax()
        
        for i in range(len(self.data)-1, -1, -1):
            if self.data[i] == max_num: 
                self.data.pop(i)
                break
        
        return max_num

    
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()