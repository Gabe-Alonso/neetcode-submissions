class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            i = (l + r) // 2
            print("L: " + str(l) + ", R: " + str(r) + ", i: " + str(i))
            if nums[i] == target:
                return i
            if nums[i] >= nums[l]:
                if target > nums[i] or target < nums[l]:
                    l = i + 1
                else:
                    r = i - 1   
            else:
                if target < nums[i] or target > nums[r]:
                    r = i - 1  
                else:
                    l = i + 1 
        return -1