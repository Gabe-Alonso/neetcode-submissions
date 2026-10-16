class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def perm(cur: List[int], rem: List[int]):
            if len(cur) >= len(nums):
                res.append(cur.copy())
                return
            for i in range(len(rem)):
                cur.append(rem[i])
                rc = rem.copy()
                del rc[i]
                perm(cur, rc)
                cur.pop()
        perm([], nums)
        return res