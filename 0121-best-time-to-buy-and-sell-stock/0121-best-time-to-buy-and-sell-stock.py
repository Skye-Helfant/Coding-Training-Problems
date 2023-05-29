class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        l, r = 0, 1
        max_profit = 0

        while r <= len(prices) - 1:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            if prices[r] < prices[l]:
                l = r
            
            r = r + 1

        return max_profit