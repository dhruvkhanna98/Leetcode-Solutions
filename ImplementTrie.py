import bisect

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = list()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        i = bisect.bisect_left(self.words, word)
        if i == len(self.words): 
            self.words.append(word)
        elif i < len(self.words):
            self.words.insert(i, word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        i = bisect.bisect_left(self.words, word)
        if i < len(self.words) and self.words[i] == word:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        i = bisect.bisect_left(self.words, prefix)
        if i < len(self.words) and self.words[i].startswith(prefix): 
            return True
        
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)