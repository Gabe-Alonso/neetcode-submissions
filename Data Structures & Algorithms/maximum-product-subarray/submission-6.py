class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ma = 1
        mi = 1
        glob_max = nums[0]
        for i in range(len(nums)):
            print("Min: " + str(mi)) 
            print("Max: " + str(ma))
            temp = ma * nums[i]
            ma = max(nums[i], ma * nums[i], mi * nums[i])
            mi = min(temp, nums[i], mi * nums[i])
            glob_max = max(glob_max, ma)
        return glob_max