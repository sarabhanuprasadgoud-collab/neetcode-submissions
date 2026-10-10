class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, result = [], 0
        idx = 0
        for op in operations:
            if op == '+':
                last_2_sum = stack[-1] + stack[-2]
                result += last_2_sum
                stack.append(last_2_sum)
            elif op == 'D':
                double = 2 * stack[-1]
                result = result + double
                stack.append(double)
            elif op == 'C':
                result = result - stack.pop()
            else:
                val = int(op)
                result = result + val
                stack.append(val)
        return result
            