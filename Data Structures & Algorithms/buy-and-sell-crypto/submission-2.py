class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        mp = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                profit = prices[r] - prices[l]
                mp = max(mp, profit)
                r += 1
        return mp