class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = []
        for i in range(len(nums)):
            if i == 0 or i == 1:
                cache.append(nums[i])
            elif i == 2:
                cache.append(nums[i] + cache[i - 2])
            else:
                cache.append(nums[i] + max(cache[i - 2], cache[i - 3]))
        if len(cache) == 1:
            return cache[0]
        else:
            return max(cache[-1], cache[-2])
            