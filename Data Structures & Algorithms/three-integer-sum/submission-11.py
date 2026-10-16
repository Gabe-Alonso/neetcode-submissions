class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        looking = True
        i = 0
        while looking:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    prev_l = nums[l]
                    l += 1
                    while l < r and nums[l] == prev_l:
                        l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            prev_i = nums[i]
            i += 1
            while i < len(nums) - 2 and nums[i] == prev_i:
                i += 1
            if i >= len(nums) - 2:
                looking = False
        return res
