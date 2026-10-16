class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present = {}
        i = 0
        for n in nums:
            present[n] = i
            i += 1
        sequences = {}
        longest = 0
        for n, i in present.items():
            if n - 1 not in present:
                sequences[n] = [n]
                m = 1
                while n + m in present:
                    sequences[n].append(n + m)
                    m += 1
                longest = max(len(sequences[n]), longest)
        return longest