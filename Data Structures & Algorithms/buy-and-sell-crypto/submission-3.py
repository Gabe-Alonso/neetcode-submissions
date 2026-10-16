class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        mProf = 0
        while r < len(prices):
            profit = prices[r]- prices[l]
            mProf = max(profit, mProf)
            if profit < 0:
                l = r
            r += 1
        return mProf