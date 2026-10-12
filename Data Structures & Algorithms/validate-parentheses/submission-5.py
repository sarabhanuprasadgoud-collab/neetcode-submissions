class Solution:
    def isValid(self, s: str) -> bool:
        index = 0
        length = len(s)
        stack = []
        valid = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        while (index < length):
            if s[index] in '({[':
                if len(stack) == 0 or stack[-1] in '({[':
                    stack.append(s[index])
            elif s[index] in ')}]':
                if len(stack) > 0 and valid[stack[-1]] == s[index]:
                    stack.pop()
                else:
                    return False
            index = index + 1
        if len(stack) == 0:
            return True
        else:
            return False
