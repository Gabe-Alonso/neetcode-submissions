class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #l = 0
        csum = 0
        max_sum = -math.inf
        for r in range(len(nums)):
            csum += nums[r]
            print(csum)
            max_sum = max(csum, max_sum)
            if csum < 0:
                csum = 0
                #l = r + 1
        return max_sum
