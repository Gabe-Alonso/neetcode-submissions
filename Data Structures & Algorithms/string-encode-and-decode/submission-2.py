class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        for s in strs:
            res += "" + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ind = 0
        res = []
        while ind < len(s) - 1:
            numStart = ind
            while s[ind] != "#":
                ind += 1
            wordLen = int(s[numStart: ind])
            res.append(s[ind + 1: ind + wordLen + 1])
            ind += wordLen + 1
        return res