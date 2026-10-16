class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for s in strs:
            freq = [0 for _ in range(26)]
            for c in s:
                freq[ord(c) - ord('a')] += 1
            password = tuple(freq)
            if password in ht:
                ht[password].append(s)
            else:
                ht[password] = [s]

        return list(ht.values())