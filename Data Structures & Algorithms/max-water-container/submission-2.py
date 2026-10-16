class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curWater = min(heights[l], heights[r]) * (r - l)
            maxWater = max(curWater, maxWater)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxWater