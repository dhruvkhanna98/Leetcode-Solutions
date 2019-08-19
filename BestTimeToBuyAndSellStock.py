# Examples

# Base Case: [] -> 0
# Example 1: [1,2,3,4] -> 3
# Example 2: [4,3,2,1] -> 0
# Example 3: [9,2,1,2,3] -> 2 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_price = 2**31 - 1
        
        # Base case
        if len(prices) == 0:
            return 0
        
        for price in prices: 
            transaction = price - min_price
            if price < min_price:
                min_price = price
            elif transaction > max_profit: 
                max_profit = transaction

        return max_profit

                