class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = 1
        for j in range(len(prices)):
            profit = prices[j] - prices[i]
            while profit < 0:
                profit = 0
                i = j
            
            max_profit = max(max_profit, profit)
        
        return max_profit
