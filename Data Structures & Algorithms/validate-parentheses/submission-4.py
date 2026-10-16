class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif p == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif p == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(p)
        if len(stack) > 0:
            return False
        return True