from collections import deque
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()
        num_right_parent = 0
        for par in s:
            if par == '(':
                stack.append(par)
            else:
                if len(stack):
                    stack.pop()
                else:
                    num_right_parent += 1
        
        return len(stack) + num_right_parent
        