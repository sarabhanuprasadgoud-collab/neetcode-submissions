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
        while (position < length):
            if operations[position] == '+':
                second = self.pop()
                first = self.peek()
                self.push(second)
                sum_val = first + second
                self.push(sum_val)
            elif operations[position] == 'D':
                double = 2 * self.peek()
                self.push(double)
            elif operations[position] == 'C':
                self.pop()
            else:
                score = int(operations[position])
                self.push(score)
            position = position + 1
    
        sum_of_scores = 0
        for i in range(len(self.stack)):
            sum_of_scores += self.pop()

        return sum_of_scores