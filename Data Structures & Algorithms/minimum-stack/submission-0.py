class MinStack:

    def __init__(self):
        self.stack = []
        self.min_is = []

    def push(self, val: int) -> None:
        i = len(self.stack)
        self.stack.append(val)
        if i == 0:
            self.min_is.append(0)
        else:
            if val < self.stack[self.min_is[-1]]:
                self.min_is.append(i)
            else:
                self.min_is.append(self.min_is[i - 1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_is.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_is[-1]]
