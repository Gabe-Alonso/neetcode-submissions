class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.temp:
            while self.stack:
                self.temp.append(self.stack.pop())
        res = self.temp.pop()
        return res


    def peek(self) -> int:
        if not self.temp:
            while self.stack:
                self.temp.append(self.stack.pop())
        res = self.temp[-1]
        return res


    def empty(self) -> bool:
        if len(self.stack) > 0 or len(self.temp) > 0:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()