class Solution:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("The stack is empty")
            
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("The stack is empty")

    def calPoints(self, operations: List[str]) -> int:
        position = 0
        length = len(operations)
        sum_of_scores = 0
        while (position < length):
            if operations[position] == '+':
                second = self.pop()
                first = self.peek()
                self.push(second)
                sum_val = first + second
                self.push(sum_val)
                sum_of_scores = sum_of_scores + sum_val
            elif operations[position] == 'D':
                double = 2 * self.peek()
                self.push(double)
                sum_of_scores = sum_of_scores + double
            elif operations[position] == 'C':
                last = self.pop()
                sum_of_scores = sum_of_scores - last
            else:
                score = int(operations[position])
                self.push(score)
                sum_of_scores = sum_of_scores + score
            position = position + 1
        return sum_of_scores