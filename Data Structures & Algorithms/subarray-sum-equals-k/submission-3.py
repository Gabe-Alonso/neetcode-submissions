class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        res = 0
        prefixSumCount = {}
        prefixSumCount[0] = 1
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum - k in prefixSumCount:
                res += prefixSumCount[curSum - k]
            if curSum in prefixSumCount:
                prefixSumCount[curSum] += 1
            else:
                prefixSumCount[curSum] = 1
        return res