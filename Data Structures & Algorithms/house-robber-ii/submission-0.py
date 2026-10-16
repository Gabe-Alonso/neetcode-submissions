class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l1 = self.rob_zombie(nums[0:len(nums) - 1])
        l2 = self.rob_zombie(nums[1:len(nums)])
        return max(l1, l2)

    def rob_zombie(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = []
        for i, n in enumerate(nums):
            if i == 0:
                dp.append(n)
            elif i == 1:
                dp.append(max(n, dp[i - 1]))
            else:
                dp.append(max(dp[i - 1], dp[i-2]+ n))
        print(dp)
        return dp[-1]
