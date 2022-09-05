from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        i = 0
        while i < len(s):
            #print(stack)
            #print('idx: ', i)
            #print('ch: ', s[i])
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
                #print(i)
                while i < len(s) and not s[i].isnumeric():
                    i += 1
                #print(i)
                ch = ''
                while i < len(s) and s[i].isnumeric():
                    ch = ch + s[i]
                    i += 1
                num_2 = int(ch)
                #print(num_2)
                num_1 = stack.pop()
                if op == '*':
                    stack.append(num_1 * num_2)
                else:
                    #print(num_1 // num_2)
                    stack.append(int(num_1 / num_2))
                #i += 1
            elif s[i] == ' ':
                i += 1
            #else:
            #    i += 1
        
        #print(stack)
        return sum(stack)
                
                
                    
                
                
        