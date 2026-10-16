class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def combine(i: int, cur: List[int]) -> List[List[int]]:
            #print("Current Combination: " + str(cur))
            if sum(cur) > target or i >= len(nums):
                return
            elif sum(cur) == target:
                res.append(cur.copy())
                return
            else:
                #print("not biugger")
                cur.append(nums[i])
                combine(i, cur)
                cur.pop()
                combine(i + 1, cur)

        combine(0, [])
        return res