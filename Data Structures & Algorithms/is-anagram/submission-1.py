class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char = {}
        for c in s:
            if c in s_char:
                s_char[c] += 1
            else:
                s_char[c] = 1
        for c in t:
            if c in s_char and s_char[c] > 0:
                s_char[c] -= 1
            else:
                return False
        return True