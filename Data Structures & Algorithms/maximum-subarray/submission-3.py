class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]
        if curSum < 0:
            curSum = 0
        for i in range(1, len(nums)):
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0

        return maxSum