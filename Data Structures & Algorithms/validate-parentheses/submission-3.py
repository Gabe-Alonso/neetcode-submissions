class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            elif p == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
            elif p == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    return False
            elif p == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        return False
        