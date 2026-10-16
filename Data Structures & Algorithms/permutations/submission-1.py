class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(cur):
            print("Subset:" + str(subset))
            if len(subset) >= len(nums):
                res.append(subset.copy())
                print("Res:" + str(res))
                return
            else:
                for n in cur:
                    new_cur = cur.copy()
                    new_cur.remove(n)
                    subset.append(n)
                    dfs(new_cur)
                    subset.pop()
        dfs(nums)
        return res