class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                total_area += max(min(maxL, maxR) - height[l], 0)
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total_area += max(min(maxL, maxR) - height[r], 0)
        return total_area