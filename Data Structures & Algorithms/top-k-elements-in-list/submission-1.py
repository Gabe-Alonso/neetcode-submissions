class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ft = {}
        res = []
        for n in nums:
            if n in ft:
                ft[n] += 1
            else:
                ft[n] = 1
        count = [[] for i in range(len(nums) + 1)]
        for key, value in ft.items():
            count[value].append(key)
        left = k
        cur = len(nums) - 1
        while left > 0:
            if len(count[cur]) > 0:
                res.append(count[cur].pop())
                left -= 1
            else:
                cur -= 1
        return res
