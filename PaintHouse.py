class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        # Base case 
        if len(costs) == 0: return 0

        cost = 0
        flag = -1
        
        for i,n in enumerate(costs): 
            temp = -1
            min_c = 2**31 - 1
            for j,m in enumerate(costs[i]): 
                if j != flag and m < min_c: 
                    min_c = m
                    temp = j
            
            cost += min_c
            flag = temp
            print(min_c)
        
        return cost
            
