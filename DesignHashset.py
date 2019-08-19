class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        

    def add(self, key: int) -> None:
        self.data[key] = True
        

    def remove(self, key: int) -> None:
        if self.contains(key): 
            self.data.pop(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.data.get(key, False)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)