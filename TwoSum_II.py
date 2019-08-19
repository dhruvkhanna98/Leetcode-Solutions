class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Base case
        if len(numbers) == 0: 
            return []
        
        num_dic = dict()
        
        for i,num in enumerate(numbers): 
            t = target - num
            if num_dic.get(t, -1) != -1:
                return [num_dic[t], i+1]
            num_dic[num] = i + 1
        return []
        