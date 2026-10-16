class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        for i in range(len(nums)):
            if nums[i] in exists:
                return True
            exists[nums[i]] = 0
        return False
        