class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = 0
        s = 0
        s2 = 0
        s = nums[s]
        f = nums[s]
        while s != f:
            s = nums[s]
            f = nums[f]
            f = nums[f]
        i = s
        while s != s2:
            s = nums[s]
            s2 = nums[s2]
        return s