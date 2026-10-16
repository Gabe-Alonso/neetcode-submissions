class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            i = (l + r) // 2
            res = min(res, nums[i])
            print("L: " + str(l) + ", R: " + str(r) + ", i: " + str(i))
            if nums[i] >= nums[l]:
                l = i + 1
            else:
                r = i - 1
        return res