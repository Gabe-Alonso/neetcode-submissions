class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}
        l = 0
        res = 0
        for r in range(len(s)):
            # print(f'r: {r}')
            # print(f's[r]: {s[r]}')
            if s[r] in ht:
                old = ht[s[r]]
                while l <= old:
                    del ht[s[l]]
                    l += 1
                    # print(f'l: {l}')
            ht[s[r]] = r
            res = max(res, (r - l + 1))
        return res