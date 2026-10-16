import array

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            freq = [0 for _ in range(26)]
            for c in s:
                freq[ord(c) - ord('a')] += 1
            hashable = tuple(freq)
            if hashable in groups:
                groups[hashable].append(s)
            else:
                groups[hashable] = [s]
        return list(groups.values())
            