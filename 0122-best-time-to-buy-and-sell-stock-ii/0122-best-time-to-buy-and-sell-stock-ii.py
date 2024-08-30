class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_profit = 0
        global_profit = 0
        candidate = prices [0]
        for price in prices:
            if price < candidate:
                local_profit = 0
                candidate = price
            else:
                if local_profit > price - candidate:
                    local_profit = 0
                    candidate = price
                else:
                    global_profit -= local_profit
                    local_profit = price - candidate
                    global_profit += local_profit
        return global_profit
