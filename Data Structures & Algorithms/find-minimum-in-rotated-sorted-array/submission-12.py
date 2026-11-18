class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(f'mid: {mid}, nums[mid]: {nums[mid]}')
            last = mid - 1
            if nums[mid] < nums[last]:
                return nums[mid]
            elif nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
