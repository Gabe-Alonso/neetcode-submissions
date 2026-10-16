class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first_letters = {}
        for i in range(len(s)):
            if s[i] in first_letters:
                first_letters[s[i]] += 1
            else:
                first_letters[s[i]] = 1
        for i in range(len(t)):
            if t[i] in first_letters:
                first_letters[t[i]] -= 1
                if first_letters[t[i]] < 0:
                    return False
            else:
                return False
        return True      
        