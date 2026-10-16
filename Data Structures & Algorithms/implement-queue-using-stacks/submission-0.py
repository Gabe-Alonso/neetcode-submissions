class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        res = temp.pop()
        while temp:
            self.stack.append(temp.pop())
        return res


    def peek(self) -> int:
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        res = temp[-1]
        while temp:
            self.stack.append(temp.pop())
        return res


    def empty(self) -> bool:
        if len(self.stack) > 0:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()