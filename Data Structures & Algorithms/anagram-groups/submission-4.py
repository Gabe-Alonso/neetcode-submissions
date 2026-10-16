import array

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - 97] += 1
            hashFreq = tuple(freq)
            if hashFreq in groups:
                groups[hashFreq].append(s)
            else:
                groups[hashFreq] = [s]
        return list(groups.values())
        