class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(nums)):
            if target - nums[i] in ht:
                return [ht[target - nums[i]], i]
            else:
                ht[nums[i]] = i
        return [0, 0]