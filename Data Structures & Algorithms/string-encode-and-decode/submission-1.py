class Solution:

    def encode(self, strs: List[str]) -> str:
        l_str = ""
        big_str = ""
        for stri in strs:
            big_str += stri
            l_str += str(len(stri)) + "-"
        big_str += "#" + l_str
        print(big_str)
        return big_str

    def decode(self, s: str) -> List[str]:
        i = len(s) - 1
        while s[i] != "#":
            i -= 1
        i += 1
        lens = s[i: len(s)].split("-")
        print(lens)
        strs = []
        j = 0
        i = 0
        while i < len(lens) - 1:
            strs.append(s[j : j + int(lens[i])])
            j += int(lens[i])
            i += 1
        return strs
