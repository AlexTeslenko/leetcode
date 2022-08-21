from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        stack = deque()
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == " ":
                i += 1
            elif ch.isnumeric():
                cur_ch = ""
                while  i < len(s) and s[i].isnumeric():
                    cur_ch = cur_ch + s[i]
                    i += 1 
                stack.append(cur_ch)
            elif ch in ['+', '-']:
                stack.append(ch)
                i += 1
            else:
                num_1 = int(stack.pop())
                while not s[i].isnumeric():
                    i += 1
                cur_ch = ""
                while  i < len(s) and s[i].isnumeric():
                    cur_ch = cur_ch + s[i]
                    i += 1 
                num_2 = int(cur_ch)
                print(cur_ch)
                cur_res = 0
                if ch == '/':
                    cur_res = num_1 // num_2
                elif ch == '*':
                    cur_res = num_1 * num_2
                
                stack.append(str(cur_res))
                #i += 1
        
        print(stack)
        
        cur_res = int(stack.popleft())
        cur_op = '+'
        while stack:
            ch = stack.popleft()
            if ch.isnumeric():
                if cur_op == '+':
                    cur_res += int(ch)
                else:
                    cur_res -= int(ch)
            elif ch == '+':
                cur_op = '+'
            else:
                cur_op = '-'
            
        
        
        return cur_res
                    
                
                
        