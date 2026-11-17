class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curOpen: int, curClosed: int, curS: str):
            if curOpen == 0 and curClosed == 0:
                res.append(curS)
                return
            if curOpen == curClosed:
                dfs(curOpen-1,curClosed, curS + "(")
            else:
                if curOpen > 0:
                    dfs(curOpen-1,curClosed, curS + "(")
                if curOpen < curClosed:
                    dfs(curOpen,curClosed-1, curS + ")")
        dfs(n, n, "")
        return res