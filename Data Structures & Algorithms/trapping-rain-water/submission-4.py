class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        cur = l
        if maxR < maxL:
            cur = r
        res = 0
        while l < r:
            water = max(0, min(maxL, maxR) - height[cur])
            res += water
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
            else:
                r -= 1
                maxR = max(maxR, height[r])
            cur = l
            if maxR < maxL:
                cur = r
        return res