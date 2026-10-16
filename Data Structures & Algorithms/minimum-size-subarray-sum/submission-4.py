class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curTotal = 0
        minLen = len(nums) + 1
        while r < len(nums) or l < len(nums):
            #print(f'l: {l}, r: {r}, curTotal: {curTotal}')
            if r < len(nums) and curTotal < target:
                curTotal += nums[r]
                r += 1
            else:
                curTotal -= nums[l]
                l += 1
            if curTotal >= target:
                minLen = min(minLen, r - l)
        if minLen == len(nums) + 1:
            return 0
        return minLen