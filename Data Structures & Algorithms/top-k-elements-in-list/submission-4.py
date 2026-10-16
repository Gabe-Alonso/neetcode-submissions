class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        buckets = [[] for _ in range(len(nums))]
        for key, value in freq.items():
            buckets[value - 1].append(key)
        res = []
        ind = len(buckets) - 1
        while k > 0:
            if len(buckets[ind]) > 0:
                res.append(buckets[ind].pop())
                k -= 1
            else:
                ind -= 1
        return res
