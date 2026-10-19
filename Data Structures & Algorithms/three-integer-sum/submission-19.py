class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                pass
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r and nums[r] >= 0:
                    total = nums[l] + nums[i] + nums[r]
                    if total == 0:
                        res.append([nums[l], nums[i], nums[r]])
                        curL = nums[l]
                        while l < r and nums[l] == curL:
                            l += 1
                    if total < 0:
                        l += 1
                    else:
                        r -= 1
        return res
        