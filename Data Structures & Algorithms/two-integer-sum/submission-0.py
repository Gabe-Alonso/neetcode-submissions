class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 0
        differences = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in differences:
                return [differences[diff], i]
            differences[nums[i]] = i
        return [0, 1]