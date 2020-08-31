class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        # Base case 
        if nums == [] or k < 0: return 0
        
        res = 0
        if k == 0: 
            nums_map = collections.Counter(nums)
            for key,value in nums_map.items():
                if value > 1:
                    res += 1
            return res

        numset = set(nums)
        for num in nums: 
            if num in numset: 
                if num-k in numset: 
                    res+=1
                if num + k in numset:
                    res+=1
                numset.remove(num)
 
        return res