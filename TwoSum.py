class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i,num in enumerate(nums):
            n = target - num
            if n in dic: 
                return [dic[n], i]
            dic[num] = i
            
        return