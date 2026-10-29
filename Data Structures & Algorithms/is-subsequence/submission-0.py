class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sInd = 0
        if len(s) == 0:
            return True
        for l in range(len(t)):
            if t[l] == s[sInd]:
                sInd += 1
                if sInd == len(s):
                    return True
        return False
        