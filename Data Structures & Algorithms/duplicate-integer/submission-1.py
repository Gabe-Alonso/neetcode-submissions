class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        for n in nums:
            if n in exists:
                return True
            else:
                exists[n] = 0
        return False