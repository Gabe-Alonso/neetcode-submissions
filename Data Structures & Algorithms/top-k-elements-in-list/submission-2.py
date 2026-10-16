class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        bucket = [[] for _ in range(len(nums))]
        for key, value in freq.items():
            bucket[value - 1].append(key)
        print(bucket)
        ind = len(bucket) - 1
        res = []
        while k > 0:
            if len(bucket[ind]) > 0:
                res.append(bucket[ind].pop())
                k -= 1
            else:
                ind -= 1
        return res