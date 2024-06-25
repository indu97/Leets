class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for p in prices[1:]:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)            
        return maxProfit