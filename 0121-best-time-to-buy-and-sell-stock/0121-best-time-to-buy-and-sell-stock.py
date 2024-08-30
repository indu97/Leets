class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        candidate = prices[0]
        max_profit = 0
        for price in prices:
            if price < candidate:
                candidate = price
            else: 
                max_profit = max(price - candidate, max_profit)
        return max_profit
