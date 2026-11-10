class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0 for _ in range(26)]
        # ord("A") = 65
        l = 0
        r = 0
        maxFreq = 0
        maxLen = 0
        while r < len(s):
            count[ord(s[r]) - 65] += 1
            maxFreq = max(maxFreq, count[ord(s[r]) - 65])
            if (r - l + 1) - maxFreq <= k:
                maxLen = max(maxLen, (r - l + 1))
                
            else:
                while (r - l + 1) - maxFreq > k:
                    count[ord(s[l]) - 65] -= 1
                    l += 1
            r += 1
        return maxLen