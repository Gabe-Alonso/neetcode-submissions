class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for n in nums:
            if n in ht:
                return True
            ht[n] = n
        return False