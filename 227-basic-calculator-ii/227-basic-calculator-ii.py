from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                ch = ''
                while i < len(s) and s[i].isnumeric():
                    ch = ch + s[i]
                    i += 1
                stack.append(int(ch))
            elif s[i] == '-':
                i += 1
                while i < len(s) and not s[i].isnumeric():
                    i += 1
                ch = ''
                while i < len(s) and s[i].isnumeric():
                    ch = ch + s[i]
                    i += 1
                stack.append(-int(ch))
            elif s[i] == '+':
                i += 1
            elif s[i] in ['*', '/']:
                op = s[i]
                i += 1
                while i < len(s) and not s[i].isnumeric():
                    i += 1
                ch = ''
                while i < len(s) and s[i].isnumeric():
                    ch = ch + s[i]
                    i += 1
                num_2 = int(ch)
                num_1 = stack.pop()
                if op == '*':
                    stack.append(num_1 * num_2)
                else:
                    stack.append(int(num_1 / num_2))
            elif s[i] == ' ':
                i += 1

        return sum(stack)
                
                
                    
                
                
        