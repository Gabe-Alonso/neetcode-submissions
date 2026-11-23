class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur: str, o: int, c: int):
            if o == 0 and c == 0:
                res.append(cur)
                return
            if o == c:
                dfs(cur + "(", o - 1, c)
            else:
                if o > 0:
                    dfs(cur + "(", o - 1, c)
                if c > 0 and c > o:
                    dfs(cur + ")", o, c - 1)
        dfs("", n, n)
        return res