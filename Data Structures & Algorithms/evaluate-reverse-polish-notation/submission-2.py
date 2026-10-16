class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(t)
            if t.isnumeric() or(len(t) > 1 and t[1:].isnumeric()):
                stack.append(int(t))
                print(stack)
            else:
                print(stack)
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(float(b) / a))
        return stack.pop()