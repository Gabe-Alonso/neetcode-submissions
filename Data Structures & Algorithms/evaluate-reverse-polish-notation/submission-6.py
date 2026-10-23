class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isdigit() or (len(t) > 1 and t[0] == "-" and t[1:].isnumeric()):
                stack.append(int(t))
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                if t == "+":
                    stack.append(o1 + o2)
                elif t == "-":
                    stack.append(o1 - o2)
                elif t == "*":
                    stack.append(o1 * o2)
                elif t == "/":
                    stack.append(int(float(o1) / o2))
        return stack.pop()