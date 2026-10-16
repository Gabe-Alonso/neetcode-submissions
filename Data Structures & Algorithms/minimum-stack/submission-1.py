class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minimum = [] 

    def push(self, val: int) -> None:
        print("Push")
        self.stack.append(val)
        if len(self.minimum) > 0:
            self.minimum.append(min(self.minimum[len(self.minimum) - 1], val))
        else:
            self.minimum.append(val)
        print("Stack:")
        print(self.stack)
        print("Min:")
        print(self.minimum)

    def pop(self) -> None:
        print("Pop")
        self.stack.pop()
        self.minimum.pop()
        print("Stack:")
        print(self.stack)
        print("Min:")
        print(self.minimum)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minimum[len(self.minimum) - 1]
        
