class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.sub(r'[^a-zA-Z0-9]', '', "".join(s.split())).lower()
        print(ss)
        l = 0
        r = len(ss) - 1
        while l < r:
            
            if ss[r] != ss[l]:
                return False
            l +=1
            r -= 1
        return True