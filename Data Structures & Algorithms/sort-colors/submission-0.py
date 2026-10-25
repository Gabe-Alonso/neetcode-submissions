class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0,0,0]
        for n in nums:
            freq[n] += 1
        i = 0
        j = 0
        for f in freq:
            for k in range(f):
                nums[j] = i
                j += 1
            i += 1