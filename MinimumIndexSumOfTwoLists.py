class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        common = set(list1) & set(list2)
        if len(common) == 1: return list(common)
        
        andy = dict()
        for i,r in enumerate(list1): 
            andy[r] = i
        
        doris = dict()
        for i,r in enumerate(list2): 
            doris[r] = i
        sum_map = dict()
        res = []
 
        for c in common: 
            curr = andy[c] + doris[c]
            sum_map[c] = curr
        
        min_sum = min(sum_map.values())
        
        for key,value in sum_map.items():
            if value == min_sum: res.append(key)
        
        return res
   