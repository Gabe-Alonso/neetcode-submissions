class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openSet = set(["(", "{", "["])
        for c in s:
            if c in openSet:
                stack.append(c)
            elif len(stack) > 0:
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True