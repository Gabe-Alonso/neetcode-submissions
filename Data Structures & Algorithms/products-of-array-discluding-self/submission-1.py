class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [[] for _ in range(len(nums))]
        prefix[0] = nums[0]
        postfix = [[] for _ in range(len(nums))]
        postfix[-1] = nums[-1]
        output = [[] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
            postfix[len(nums) - 1 - i] = postfix[len(nums) - i] * nums[len(nums) - 1 - i]
        for i in range(0, len(nums)):
            if i == 0:
                output[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                output[i] = prefix[i - 1]
            else:
                output[i] = prefix[i - 1] * postfix[i + 1]
        return output