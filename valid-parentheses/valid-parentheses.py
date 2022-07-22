from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        for ch in s:
 
            if ch in ['{', '(', '[']:
                stack.append(ch)
            elif ch in ['}', ')', ']']:
                if len(stack) > 0:
                    prev_parent = stack.pop()
                    if ch == ')' and prev_parent != '(':
                        return False
                    if ch == '}' and prev_parent != '{':
                        return False
                    if ch == ']' and prev_parent != '[':
                        return False
                else:
                    return False
        
        return len(stack) == 0