class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r != len(prices):
            if prices[r] - prices[l] > max_profit:
                max_profit = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1
        
        return max_profit