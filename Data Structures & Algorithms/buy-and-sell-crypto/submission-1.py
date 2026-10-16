class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l
        mp = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            mp = max(mp, profit)
            if r + 1 < len(prices):
                if prices[r + 1] < prices[l]:
                    l = r + 1
                    r = l
                else:
                    r += 1
            else:
                r += 1
        return mp