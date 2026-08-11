class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = i + 1
        for j in range(0, len(prices)):
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
        return max_profit