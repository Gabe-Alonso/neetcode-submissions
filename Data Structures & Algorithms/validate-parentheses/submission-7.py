class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openSet = set(["(", "{", "["])
        for p in s:
            if p in openSet:
                stack.append(p)
            elif p == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif p == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif p == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True