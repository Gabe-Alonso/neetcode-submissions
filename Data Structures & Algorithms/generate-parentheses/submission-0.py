class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.genPar("(", n)

    def genPar(self, cur: str, n: int) -> List[str]:
        o = 0
        c = 0
        poss = []
        if len(cur) > 2 * n:
            return []
        elif len(cur) == 2 * n:
            return [cur]
        for p in cur:
            if p == "(":
                o += 1
            else:
                c += 1
        if c < o:
            poss.extend(self.genPar(cur + ")", n))
        if o < n:
            poss.extend(self.genPar(cur + "(", n))
        return poss
        