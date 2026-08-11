class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = 1
        for j in range(len(prices)):
            current_profit = prices[j] - prices[i]
            if prices[i] > prices[j]:
                i = j
            max_profit = max(max_profit, current_profit)
        
        return max_profit