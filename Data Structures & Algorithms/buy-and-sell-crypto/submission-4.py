class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        if len(prices) == 1:
            return res
        curPrice = 0
        while r < len(prices):
            curPrice = prices[r] - prices[l]
            res = max(res, curPrice)
            if curPrice <= 0:
                l = r
            r += 1
        return res