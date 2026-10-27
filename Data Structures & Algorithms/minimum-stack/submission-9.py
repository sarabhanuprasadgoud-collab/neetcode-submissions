class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # a stack carrying the minimum history

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]) if self.min_stack else val)

    def pop(self) -> None:
        if not self.stack:
            return 
        val = self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]