class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0 for _ in range(len(height))]
        maxRight = [0 for _ in range(len(height))]
        total = 0
        maxLeft[0] = height[0]
        maxRight[-1] = height[-1]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        print(maxLeft)
        print(maxRight)
        for i, h in enumerate(height):
            total += max(min(maxLeft[i], maxRight[i]) - h, 0)
            print(total)
        return total