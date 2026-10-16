class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, n in enumerate(nums):
            ht[target - n] = i
        #print(ht)
        for i, n in enumerate(nums):
            if n in ht and ht[n] != i:
                return [min(i, ht[n]), max(i, ht[n])]
        return [0, 0]
            