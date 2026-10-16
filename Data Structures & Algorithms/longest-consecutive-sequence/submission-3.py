class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        if len(nums) > 0:
            hs = set([])
            curSeq = 0
            cur = nums[0]
            for n in nums:
                hs.add(n)
            for n in nums:
                curSeq = 1
                if n - 1 in hs:
                    pass
                else:
                    while n + 1 in hs:
                        curSeq += 1
                        n += 1
                maxSeq = max(maxSeq, curSeq)
        return maxSeq