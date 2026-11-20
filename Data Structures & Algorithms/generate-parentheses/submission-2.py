class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def buildStack(cur: str, oBrack: int, cBrack: int):
            if oBrack == 0 and cBrack == 0:
                res.append(cur)
                return
            if oBrack == cBrack:
                buildStack(cur + "(", oBrack - 1, cBrack)
            else:
                if oBrack > 0:
                    buildStack(cur + "(", oBrack - 1, cBrack)
                if cBrack > 0 and cBrack > oBrack:
                    buildStack(cur + ")", oBrack, cBrack - 1)
        buildStack("", n, n)
        return res