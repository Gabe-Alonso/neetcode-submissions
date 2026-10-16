class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ht = {}
        ml = 0
        for r, c in enumerate(s):
            if c in ht:
                while l < ht[c]:
                    del ht[s[l]]
                    l += 1 
                l += 1 
            ht[c] = r
            ml = max(ml, r - l + 1)
        return ml
            