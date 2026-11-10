class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0 for _ in range(26)]
        count2 = [0 for _ in range(26)]
        # print(count1 == count2)
        for c in s1:
            count1[ord(c) - 97] += 1
        l = 0
        r = 0
        while r < len(s2) and r < len(s1):
            count2[ord(s2[r]) - 97] += 1
            r += 1
        if count1 == count2:
            return True
        while r < len(s2):
            count2[ord(s2[l]) - 97] -= 1
            l += 1
            count2[ord(s2[r]) - 97] += 1
            r += 1
            if count1 == count2:
                return True
        return False