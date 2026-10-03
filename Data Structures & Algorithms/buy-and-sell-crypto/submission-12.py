class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maximum = 0
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] >= 0:
                maximum = max(maximum, prices[j] - prices[i])
            else:
                i = j
        return maximum